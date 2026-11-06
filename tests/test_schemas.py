import pytest
from pydantic import ValidationError

from langchain_agent.schemas import CalculatorInput, SearchInput


def test_calculator_rejects_empty() -> None:
    with pytest.raises(ValidationError):
        CalculatorInput(expression="")


def test_search_bounds() -> None:
    with pytest.raises(ValidationError):
        SearchInput(query="x", max_results=0)
    assert SearchInput(query="x").max_results == 3
