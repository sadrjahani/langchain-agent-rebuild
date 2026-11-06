# ADR 0003: Deterministic tests via fake model; logic separated from framework
- **Context:** Live LLMs are slow and non-deterministic on CPU.
- **Decision:** Keep tool logic in `tool_logic.py` (no LangChain); test the agent loop with a scripted fake chat model; keep live-model runs in `evals/`.
- **Consequences:** Fast CI; a green suite does not prove behavior with a real model.
