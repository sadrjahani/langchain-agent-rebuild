"""Tiny CLI: uv run python -m langchain_agent.main"""

from langchain_agent.agent import build_agent
from langchain_agent.config import load_settings


def main() -> None:
    settings = load_settings()
    agent = build_agent()
    cfg = {"configurable": {"thread_id": "demo"}, "recursion_limit": settings.max_steps * 2}
    while (text := input("you> ").strip()) not in {"", "exit"}:
        out = agent.invoke({"messages": [{"role": "user", "content": text}]}, cfg)
        print(out["messages"][-1].content)


if __name__ == "__main__":
    main()
