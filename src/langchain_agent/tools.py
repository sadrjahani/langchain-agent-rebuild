"""LangChain tool definitions: name + description + input schema + function (Phase 3)."""

from pathlib import Path

from langchain_core.tools import tool

from langchain_agent import tool_logic
from langchain_agent.schemas import CalculatorInput, FileLookupInput, SearchInput

DATA_DIR = Path(__file__).resolve().parents[2] / "data"


@tool("calculator", args_schema=CalculatorInput)
def calculator(expression: str) -> str:
    """Evaluate a math expression using safe arithmetic."""
    try:
        return str(tool_logic.calculate(expression))
    except (ValueError, ZeroDivisionError, SyntaxError) as exc:
        return f"Error: {exc}"


@tool("search", args_schema=SearchInput)
def search(query: str, max_results: int = 3) -> str:
    """Search the small local dataset (not the live web)."""
    hits = tool_logic.search_docs(query, max_results)
    return "\n".join(hits) if hits else "No results."


@tool("file_lookup", args_schema=FileLookupInput)
def file_lookup(filename: str, keyword: str) -> str:
    """Find lines containing a keyword in a file inside the project data directory."""
    try:
        lines = tool_logic.lookup_file(filename, keyword, DATA_DIR)
    except (PermissionError, FileNotFoundError) as exc:
        return f"Error: {exc}"
    return "\n".join(lines) if lines else "No matches."


ALL_TOOLS = [calculator, search, file_lookup]
