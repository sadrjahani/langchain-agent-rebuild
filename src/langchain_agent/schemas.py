"""Pydantic input contracts for the three tools (Phase 3)."""

from pydantic import BaseModel, Field


class CalculatorInput(BaseModel):
    expression: str = Field(
        min_length=1, max_length=200, description="Math expression, e.g. '2*(3+4)'"
    )


class SearchInput(BaseModel):
    query: str = Field(min_length=1, max_length=200, description="Search query")
    max_results: int = Field(default=3, ge=1, le=10, description="Max results to return")


class FileLookupInput(BaseModel):
    filename: str = Field(min_length=1, max_length=100, description="File name in the data dir")
    keyword: str = Field(min_length=1, max_length=100, description="Keyword to find in the file")
