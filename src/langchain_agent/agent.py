"""Agent construction (Phases 4-5). UNTESTED against a live model: verify argument names
against the installed langchain version before relying on them."""

from typing import Any

from langchain_agent.config import load_settings
from langchain_agent.tools import ALL_TOOLS

SYSTEM_PROMPT = "You are a helpful assistant. Use tools when needed and answer concisely."


def build_agent(model: Any | None = None, checkpointer: Any | None = None) -> Any:
    from langchain.agents import create_agent
    from langchain_ollama import ChatOllama
    from langgraph.checkpoint.memory import InMemorySaver

    settings = load_settings()
    llm = model or ChatOllama(
        model=settings.ollama_model, base_url=settings.ollama_base_url, temperature=0
    )
    return create_agent(
        model=llm,
        tools=ALL_TOOLS,
        system_prompt=SYSTEM_PROMPT,
        checkpointer=checkpointer or InMemorySaver(),
    )
