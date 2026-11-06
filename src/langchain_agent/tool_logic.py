"""Framework-free tool logic.

PLACEHOLDER: replace the bodies with the real logic from react-agent-from-scratch so both
projects share equivalent behavior. Keeping this layer free of LangChain makes the
comparison fair and the logic unit-testable.
"""

import ast
import operator
from collections.abc import Callable
from pathlib import Path
from typing import Any

_BIN: dict[type, Callable[[Any, Any], Any]] = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
}


def _eval(node: ast.AST) -> float:
    if isinstance(node, ast.Expression):
        return _eval(node.body)
    if isinstance(node, ast.Constant):
        v = node.value
        if isinstance(v, bool) or not isinstance(v, int | float):
            raise ValueError("only numbers are allowed")
        return float(v)
    if isinstance(node, ast.BinOp) and type(node.op) in _BIN:
        left, right = _eval(node.left), _eval(node.right)
        if isinstance(node.op, ast.Pow) and abs(right) > 100:
            raise ValueError("exponent too large")
        return float(_BIN[type(node.op)](left, right))
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub | ast.UAdd):
        val = _eval(node.operand)
        return -val if isinstance(node.op, ast.USub) else val
    raise ValueError("unsupported expression")


def calculate(expression: str) -> float:
    """Safe arithmetic: AST whitelist, no eval()."""
    return _eval(ast.parse(expression, mode="eval"))


_DOCS = [
    "LangChain is a framework for building LLM applications.",
    "LangGraph provides stateful, graph-based agent runtimes.",
    "Ollama runs open models locally.",
]


def search_docs(query: str, max_results: int = 3) -> list[str]:
    """Search a tiny in-memory dataset (not live web search)."""
    terms = query.lower().split()
    hits = [d for d in _DOCS if any(t in d.lower() for t in terms)]
    return hits[:max_results]


def lookup_file(filename: str, keyword: str, base_dir: Path) -> list[str]:
    """Return lines containing keyword; access is confined to base_dir."""
    base = base_dir.resolve()
    target = (base / filename).resolve()
    if not target.is_relative_to(base):
        raise PermissionError("path escapes the allowed directory")
    if not target.is_file():
        raise FileNotFoundError(filename)
    kw = keyword.lower()
    return [ln for ln in target.read_text(encoding="utf-8").splitlines() if kw in ln.lower()]
