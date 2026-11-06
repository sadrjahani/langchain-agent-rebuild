# langchain-agent-rebuild
Rebuild of [react-agent-from-scratch](https://github.com/sadrjahani/react-agent-from-scratch) with LangChain, for a fair side-by-side comparison.

## Status
Skeleton. See roadmap issues on GitHub.

## Quick start
```bash
uv sync
cp .env.example .env
ollama pull phi4-mini
uv run python -m langchain_agent.main
```

## Architecture (target)

```mermaid
flowchart TD
    Q[User Query] --> A[Agent + Conversation State]
    A -.-> C[Conversation Checkpointer]
    C -.-> A
    A --> M[LangChain Chat Model]
    M --> D{Tool required?}
    D -- No --> F[Final Answer] --> U[User]
    D -- Yes --> TC[Tool Calling] --> V[Tool Schema Validation] --> S{{Selected Tool}}
    S --> Calc[Calculator]
    S --> Se[Search]
    S --> FL[File Lookup]
    Calc --> R[Tool Result]
    Se --> R
    FL --> R
    R --> M
```

## Comparison / Limitations
TODO (Phase 7). See `docs/comparison.md`.
