"""Runtime settings loaded from environment / .env (never committed)."""

import os
from dataclasses import dataclass

from dotenv import load_dotenv


@dataclass(frozen=True)
class Settings:
    ollama_model: str
    ollama_base_url: str
    max_steps: int


def load_settings() -> Settings:
    load_dotenv()
    return Settings(
        ollama_model=os.getenv("OLLAMA_MODEL", "phi4-mini"),
        ollama_base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"),
        max_steps=int(os.getenv("MAX_STEPS", "8")),
    )
