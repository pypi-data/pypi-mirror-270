import functools
from typing import Any

import pandas as pd
from dask.base import DaskMethodsMixin
from dask.sizeof import sizeof
from dask.utils import format_bytes

from dask_expr._expr import Blockwise, Expr
from dask_expr._util import _tokenize_deterministic, is_scalar
from dask_expr.diagnostics._analyze_plugin import (
    AnalyzePlugin,
    ExpressionStatistics,
    Statistics,
    get_worker_plugin,
)
from dask_expr.diagnostics._explain import _add_graphviz_edges, _explain_info
from dask_expr.io.io import FusedIO


def inject_analyze(expr: Expr, id: str, injected: dict) -> Expr:
    if expr._name in injected:
        return injected[expr._name]

    new_operands = []
    for operand in expr.operands:
        if isinstance(operand, Expr) and not isinstance(expr, FusedIO):
            new = inject_analyze(operand, id, injected)
            injected[operand._name] = new
        else:
            new = operand
        new_operands.append(new)
    return Analyze(type(expr)(*new_operands), id, expr._name)


def analyze(
    expr: Expr, filename: str | None = None, format: str | None = None, **kwargs: Any
):
    import graphviz
    from dask.dot import graphviz_to_file
    from distributed import get_client, wait

    from dask_expr import new_collection

    client = get_client()

    client.register_plugin(AnalyzePlugin())

    # TODO: Make this work with fuse=True
    expr = expr.optimize(fuse=False)

    analysis_id = expr._name

    # Inject analyze nodes
    injected = inject_analyze(expr, analysis_id, {})
    out = new_collection(injected)
    _ = DaskMethodsMixin.compute(out, **kwargs)
    wait(_)

    # Collect data
    statistics: Statistics = client.sync(
        client.scheduler.analyze_get_statistics, id=analysis_id
    )  # type: noqa

    # Plot statistics in graph
    seen = set(expr._name)
    stack = [expr]

    if filename is None:
        filename = f"analyze-{expr._name}"

    if format is None:
        format = "svg"

    g = graphviz.Digraph(expr._name)
    g.node_attr.update(shape="record")
    while stack:
        node = stack.pop()
        info = _analyze_info(node, statistics._expr_statistics[node._name])
        _add_graphviz_node(info, g)
        _add_graphviz_edges(info, g)

        if isinstance(node, FusedIO):
            continue
        for dep in node.operands:
            if not isinstance(dep, Expr) or dep._name in seen:
                continue
            seen.add(dep._name)
            stack.append(dep)
    graphviz_to_file(g, filename, format)
    return g


def _add_graphviz_node(info, graph):
    label = "".join(
        [
            "<{<b>",
            info["label"],
            "</b> | ",
            "<br />".join(
                [f"{key}: {value}" for key, value in info["details"].items()]
            ),
            " | ",
            _statistics_to_graphviz(info["statistics"]),
            "}>",
        ]
    )

    graph.node(info["name"], label)


def _statistics_to_graphviz(statistics: dict[str, dict[str, Any]]) -> str:
    return "<BR /><BR />".join(
        [
            _metric_to_graphviz(metric, statistics)
            for metric, statistics in statistics.items()
        ]
    )


_FORMAT_FNS = {"nbytes": format_bytes, "nrows": "{:,.0f}".format}


def _metric_to_graphviz(metric: str, statistics: dict[str, Any]):
    format_fn = _FORMAT_FNS[metric]
    quantiles = (
        "[" + ", ".join([format_fn(pctl) for pctl in statistics.pop("quantiles")]) + "]"
    )
    count = statistics["count"]
    total = statistics["total"]

    return "<BR />".join(
        [
            f"<B>{metric}:</B>",
            f"{format_fn(total / count)} ({format_fn(total)} / {count:,})",
            f"{quantiles}",
        ]
    )


def _analyze_info(expr: Expr, statistics: ExpressionStatistics):
    info = _explain_info(expr)
    info["statistics"] = _statistics_info(statistics)
    return info


def _statistics_info(statistics: ExpressionStatistics):
    info = {}
    for metric, digest in statistics._metric_digests.items():
        info[metric] = {
            "total": digest.total,
            "count": digest.count,
            "quantiles": [digest.sketch.quantile(q) for q in (0, 0.25, 0.5, 0.75, 1)],
        }
    return info


def collect_statistics(frame, analysis_id, expr_name):
    worker_plugin = get_worker_plugin()
    if isinstance(frame, pd.DataFrame):
        size = frame.memory_usage(deep=True).sum()
    elif isinstance(frame, pd.Series):
        size = frame.memory_usage(deep=True)
    else:
        size = sizeof(frame)

    len_frame = len(frame) if not is_scalar(frame) else 1
    worker_plugin.add(analysis_id, expr_name, "nrows", len_frame)
    worker_plugin.add(analysis_id, expr_name, "nbytes", size)
    return frame


class Analyze(Blockwise):
    _parameters = ["frame", "analysis_id", "expr_name"]

    operation = staticmethod(collect_statistics)

    @functools.cached_property
    def _meta(self):
        return self.frame._meta

    @functools.cached_property
    def _name(self):
        return "analyze-" + _tokenize_deterministic(*self.operands)
