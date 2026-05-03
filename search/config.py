"""
Configuration module for Knowledge OS search system.

Provides centralized settings management using Pydantic for validation
and type safety. All configuration is loaded from environment variables.
"""

import os
from pathlib import Path
from typing import Optional

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class SearchConfig(BaseSettings):
    """
    Configuration settings for the Knowledge OS search system.

    All settings are loaded from environment variables with fallback defaults.
    For development, create a .env file in the project root.

    Attributes:
        api_key: DeepSeek API key for LLM-powered answers.
        model_name: Name of the DeepSeek model to use.
        max_tokens: Maximum tokens in LLM response.
        temperature: Sampling temperature for LLM (0.0-1.0).
        n_results: Number of search results to retrieve.
        chroma_db_path: Path to ChromaDB vector store.
        model_name_embed: Name of embedding model for semantic search.
        knowledge_os_root: Root directory of Knowledge OS project.
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_prefix="",
        extra="ignore",
    )

    api_key: str = Field(
        default="",
        description="DeepSeek API key for RAG queries",
    )

    model_name: str = Field(
        default="deepseek-chat",
        description="DeepSeek model for generating answers",
    )

    max_tokens: int = Field(
        default=1500,
        ge=100,
        le=4000,
        description="Maximum tokens in LLM response",
    )

    temperature: float = Field(
        default=0.7,
        ge=0.0,
        le=1.0,
        description="LLM sampling temperature",
    )

    n_results: int = Field(
        default=5,
        ge=1,
        le=20,
        description="Number of search results to retrieve",
    )

    chroma_db_path: Path = Field(
        default=Path(__file__).parent / "knowledge_db",
        description="Path to ChromaDB persistent storage",
    )

    model_name_embed: str = Field(
        default="all-MiniLM-L6-v2",
        description="Sentence transformer model for embeddings",
    )

    knowledge_os_root: Path = Field(
        default=Path(__file__).parent.parent,
        description="Root directory of Knowledge OS project",
    )

    def __init__(self, **kwargs: object) -> None:
        """Initialize config, loading from .env if present."""
        super().__init__(**kwargs)
        # Load .env file from project root if it exists
        env_path = self.knowledge_os_root / ".env"
        if env_path.exists():
            from dotenv import load_dotenv
            load_dotenv(env_path, override=True)
            # Reload after dotenv
            super().__init__(**kwargs)

    @property
    def is_api_key_configured(self) -> bool:
        """Check if API key is set and not a placeholder."""
        return bool(self.api_key and self.api_key != "your_key_here")


# Global singleton instance
_config: Optional[SearchConfig] = None


def get_config() -> SearchConfig:
    """
    Get the global configuration instance.

    Returns:
        The singleton SearchConfig instance.
    """
    global _config
    if _config is None:
        _config = SearchConfig()
    return _config


# Convenience exports for direct module usage
API_KEY = get_config().api_key
MODEL_NAME = get_config().model_name
MAX_TOKENS = get_config().max_tokens
TEMPERATURE = get_config().temperature
N_RESULTS = get_config().n_results
CHROMA_DB_PATH = get_config().chroma_db_path
MODEL_NAME_EMBED = get_config().model_name_embed
KNOWLEDGE_OS_ROOT = get_config().knowledge_os_root