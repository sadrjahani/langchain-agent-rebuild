from pathlib import Path

import pytest

from langchain_agent import tool_logic
from langchain_agent.tools import calculator, file_lookup


def test_calculate_ok() -> None:
    assert tool_logic.calculate("2*(3+4)") == 14


@pytest.mark.parametrize("expr", ["__import__('os')", "2**10000", "a+1"])
def test_calculate_rejects_unsafe(expr: str) -> None:
    with pytest.raises(ValueError):
        tool_logic.calculate(expr)


def test_calculator_tool_handles_div_zero() -> None:
    assert calculator.invoke({"expression": "1/0"}).startswith("Error")


def test_lookup_blocks_traversal(tmp_path: Path) -> None:
    with pytest.raises(PermissionError):
        tool_logic.lookup_file("../x.txt", "a", tmp_path)


def test_file_lookup_tool_finds_keyword() -> None:
    assert "Project H" in file_lookup.invoke({"filename": "sample.txt", "keyword": "name"})
