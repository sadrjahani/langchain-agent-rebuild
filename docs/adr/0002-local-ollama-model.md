# ADR 0002: Local Ollama model (phi4-mini) by default
- **Context:** CPU-only, older machine; free and offline requirement.
- **Decision:** Default to a small local model via Ollama; configurable via `.env`.
- **Consequences:** Tool-calling quality is model-dependent and may be weaker; tests must not depend on a live model. Check each model's license before redistributing anything.
