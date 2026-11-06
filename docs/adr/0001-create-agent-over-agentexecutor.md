# ADR 0001: Use create_agent, not AgentExecutor
- **Context:** This project must reflect current LangChain practice; AgentExecutor is legacy.
- **Decision:** Build the agent with `create_agent` (LangGraph-based). Study AgentExecutor only for reading old code.
- **Consequences:** Checkpointer/thread support comes built in; API may change, so versions are locked in `uv.lock`.
