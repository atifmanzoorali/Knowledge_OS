"""
RAG-powered Answer Generator for Knowledge OS.

Provides semantic search over the knowledge base with LLM-powered
answer synthesis using DeepSeek API.

Usage:
    python -m search.ask "your question here"
    python search/ask.py "your question here"
    python search/ask.py  # Interactive mode
"""

import argparse
import json
import logging
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Any, Optional

import chromadb
from openai import OpenAI
from sentence_transformers import SentenceTransformer

from search.config import get_config

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)


class KnowledgeOSError(Exception):
    """Base exception for Knowledge OS errors."""

    pass


class APIKeyNotConfiguredError(KnowledgeOSError):
    """Raised when DeepSeek API key is not configured."""

    pass


class SearchIndexEmptyError(KnowledgeOSError):
    """Raised when the search index contains no documents."""

    pass


class LLMQueryError(KnowledgeOSError):
    """Raised when LLM query fails."""

    pass


def _get_healing_log_path() -> Path:
    """Get path to healing log file."""
    config = get_config()
    return config.log_dir / "healing_log.json"


def _load_healing_log() -> dict:
    """Load existing healing log or create new one."""
    log_path = _get_healing_log_path()
    if log_path.exists():
        try:
            with open(log_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            pass
    return {"session_date": datetime.now().strftime("%Y-%m-%d"), "healing_events": []}


def _save_healing_log(log_data: dict) -> None:
    """Save healing log to file."""
    config = get_config()
    config.log_dir.mkdir(parents=True, exist_ok=True)
    log_path = _get_healing_log_path()
    with open(log_path, "w", encoding="utf-8") as f:
        json.dump(log_data, f, indent=2)


def _log_healing_event(
    error_type: str,
    error_message: str,
    fixes_tried: list[dict],
    outcome: str,
    next_agent_note: str = "",
) -> None:
    """Log a self-healing event for future agent sessions."""
    log_data = _load_healing_log()
    event = {
        "timestamp": datetime.now().isoformat(),
        "error_type": error_type,
        "error_message": error_message,
        "fixes_tried": fixes_tried,
        "outcome": outcome,
        "next_agent_note": next_agent_note,
    }
    log_data["healing_events"].append(event)
    _save_healing_log(log_data)


def _user_alert(message: str, prefix: str = "ℹ️") -> None:
    """Print user-facing alert message."""
    print(f"\n{prefix} {message}\n")
    logger.info(message)


def _auto_rebuild_index() -> bool:
    """Auto-rebuild search index when empty. Returns True if successful."""
    _user_alert("Search index is empty. Auto-rebuilding...", "🔄")
    try:
        result = subprocess.run(
            [sys.executable, "-m", "search.index"],
            cwd=get_config().knowledge_os_root,
            capture_output=True,
            text=True,
            timeout=120,
        )
        if result.returncode == 0:
            _user_alert("Index rebuilt successfully!", "✅")
            return True
        else:
            _user_alert(f"Index rebuild failed: {result.stderr}", "❌")
            return False
    except Exception as e:
        _user_alert(f"Could not auto-rebuild index: {e}", "❌")
        return False


def load_api_key() -> str:
    """
    Load and validate DeepSeek API key from configuration.

    Returns:
        Valid API key string.

    Raises:
        APIKeyNotConfiguredError: If API key is not configured.
    """
    config = get_config()

    if not config.is_api_key_configured:
        raise APIKeyNotConfiguredError(
            "DeepSeek API key not configured. "
            "Get your free API key at https://platform.deepseek.com/ "
            f"and set it in the .env file at {config.knowledge_os_root / '.env'}"
        )

    return config.api_key


def search_knowledge(
    query: str,
    n_results: int | None = None,
) -> tuple[dict[str, Any], int, list[str]]:
    """
    Search the knowledge base for relevant documents.

    Args:
        query: Search query string.
        n_results: Number of results to retrieve. Defaults to config value.

    Returns:
        Tuple of (search results dict, total document count, collection IDs).

    Raises:
        SearchIndexEmptyError: If no documents in the index.
    """
    config = get_config()

    if n_results is None:
        n_results = config.n_results

    chroma_client = chromadb.PersistentClient(path=str(config.chroma_db_path))
    collection = chroma_client.get_or_create_collection(name="knowledge")

    if collection.count() == 0:
        if _auto_rebuild_index():
            collection = chroma_client.get_or_create_collection(name="knowledge")
            if collection.count() == 0:
                raise SearchIndexEmptyError(
                    "No documents in the search index after auto-rebuild. "
                    "Run 'python search/index.py' to build the index."
                )
        else:
            raise SearchIndexEmptyError(
                "No documents in the search index. "
                "Run 'python search/index.py' to build the index."
            )

    model = SentenceTransformer(config.model_name_embed)
    query_embedding = model.encode([query])

    results = collection.query(
        query_embeddings=query_embedding.tolist(),
        n_results=n_results,
    )

    return results, collection.count(), collection.get()["ids"]


def read_file_content(rel_path: str) -> str:
    """
    Read content from a file relative to project root.

    Args:
        rel_path: Relative path to the file.

    Returns:
        File content with YAML frontmatter stripped. Error message on failure.
    """
    config = get_config()
    full_path = config.knowledge_os_root / rel_path

    try:
        with open(full_path, "r", encoding="utf-8") as f:
            content = f.read()
            if content.startswith("---"):
                parts = content.split("---", 2)
                if len(parts) >= 3:
                    content = parts[2]
            return content.strip()
    except OSError as e:
        return f"Error reading file: {e}"
    except Exception as e:
        return f"Unexpected error: {e}"


def build_prompt(
    context_docs: list[str],
    metadatas: list[dict[str, Any]],
    question: str,
) -> str:
    """
    Build the prompt for the LLM with context and question.

    Args:
        context_docs: List of document texts from search results.
        metadatas: List of metadata dicts from search results.
        question: The user's question.

    Returns:
        Formatted prompt string.
    """
    context_parts = []

    for i, (doc, meta) in enumerate(zip(context_docs, metadatas), 1):
        source = meta.get("source", "Unknown")
        # Truncate long documents
        truncated_doc = doc[:1500] if len(doc) > 1500 else doc
        context_parts.append(f"--- Source {i}: {source} ---\n{truncated_doc}\n")

    context = "\n".join(context_parts)

    prompt = f"""You are a helpful assistant that answers questions based on the user's knowledge base.
Use the provided context from their knowledge files to answer accurately.
Always cite sources when making claims. Be concise but thorough. If the context doesn't contain enough information to answer the question, say so.

Context from knowledge base:
{context}

Question: {question}

Instructions: Answer based on the context above. Cite the specific source files when making claims."""

    return prompt


def call_deepseek(
    api_key: str,
    prompt: str,
    max_tokens: int | None = None,
    attempt: int = 1,
    fixes_tried: list | None = None,
) -> str:
    """
    Call DeepSeek API with self-healing logic.

    Args:
        api_key: DeepSeek API key.
        prompt: Formatted prompt with context and question.
        max_tokens: Override max tokens for retry with smaller request.
        attempt: Current attempt number (for logging).
        fixes_tried: List of fixes already attempted (for logging).

    Returns:
        Generated answer text.

    Raises:
        LLMQueryError: If the API call fails and cannot be auto-healed.
    """
    if fixes_tried is None:
        fixes_tried = []

    config = get_config()

    try:
        client = OpenAI(
            api_key=api_key,
            base_url="https://api.deepseek.com",
        )

        response = client.chat.completions.create(
            model=config.model_name,
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant that answers questions based on the user's knowledge base.",
                },
                {"role": "user", "content": prompt},
            ],
            max_tokens=max_tokens or config.max_tokens,
            temperature=config.temperature,
        )

        return response.choices[0].message.content

    except Exception as e:
        error_msg = str(e)
        error_type = type(e).__name__

        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "module": "search.ask",
            "function": "call_deepseek",
            "error_type": error_type,
            "error_message": error_msg,
        }
        config.log_dir.mkdir(parents=True, exist_ok=True)
        error_log_path = config.log_dir / "errors.log"
        with open(error_log_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(log_entry) + "\n")

        if "429" in error_msg or "rate_limit" in error_msg.lower() or "rate limit" in error_msg.lower():
            if attempt < 3:
                wait_times = [5, 10, 20]
                wait = wait_times[attempt - 1]
                _user_alert(f"Rate limited. Waiting {wait}s before retry (attempt {attempt + 1}/3)...", "📡")
                time.sleep(wait)
                fixes_tried.append({"attempt": attempt, "action": f"wait_{wait}s_retry", "result": "failed"})
                return call_deepseek(api_key, prompt, max_tokens, attempt + 1, fixes_tried)
            else:
                _log_healing_event("API_RATE_LIMIT", error_msg, fixes_tried, "failed", "All 3 retry attempts exhausted. Consider checking API quota.")
                raise LLMQueryError(f"Rate limit persisted after 3 attempts: {e}") from e

        if "timeout" in error_msg.lower() or "timed out" in error_msg.lower():
            if max_tokens is None and attempt <= 2:
                new_max_tokens = int(config.max_tokens * 0.75)
                _user_alert(f"Request timed out. Trying with smaller response ({new_max_tokens} tokens)...", "⏱️")
                time.sleep(2)
                fixes_tried.append({"attempt": attempt, "action": f"reduce_max_tokens_to_{new_max_tokens}", "result": "failed"})
                return call_deepseek(api_key, prompt, new_max_tokens, attempt + 1, fixes_tried)
            else:
                _log_healing_event("API_TIMEOUT", error_msg, fixes_tried, "failed", "Timeout persisted after reducing tokens.")
                raise LLMQueryError(f"Request timeout: {e}") from e

        if attempt < 3:
            _user_alert(f"API error (attempt {attempt}/3): {error_type}. Retrying...", "⚠️")
            time.sleep(2 ** attempt)
            fixes_tried.append({"attempt": attempt, "action": "basic_retry", "result": "failed"})
            return call_deepseek(api_key, prompt, max_tokens, attempt + 1, fixes_tried)

        _log_healing_event(error_type, error_msg, fixes_tried, "failed", f"Exhausted all fixes. Error type: {error_type}")
        raise LLMQueryError(f"Failed to query DeepSeek after 3 attempts: {e}") from e


def format_response(
    answer: str,
    documents: list[str],
    metadatas: list[dict[str, Any]],
    distances: list[float],
    query: str,
) -> None:
    """
    Format and print the response to stdout.

    Args:
        answer: Generated answer text.
        documents: List of source documents.
        metadatas: List of document metadata.
        distances: List of similarity distances.
        query: Original user query.
    """
    print("\n" + "=" * 60)
    print(f"Question: {query}")
    print("=" * 60)
    print("\nAnswer:\n")
    print(answer)
    print("\n" + "-" * 60)
    print("\nSources (ranked by relevance):\n")

    for i, (doc, meta, dist) in enumerate(zip(documents, metadatas, distances), 1):
        # Convert distance to relevance score (0-1)
        score = 1 - dist
        score = max(0.0, min(1.0, score))

        source = meta.get("source", "Unknown")
        category = meta.get("category", "Unknown")
        file_type = meta.get("file_type", "unknown")
        file_type_label = "[profile]" if file_type == "profile" else "[transcript]"

        print(f"  {i}. {source} {file_type_label}")
        print(f"     Category: {category} | Relevance: {score:.1%}")
        print()

    print("=" * 60)


def query_knowledge_base(question: str) -> int:
    """
    Execute a query against the knowledge base.

    Args:
        question: The user's question.

    Returns:
        Exit code (0 for success, non-zero for error).
    """
    try:
        api_key = load_api_key()

        logger.info("Searching for relevant context...")
        results, total_docs, _ = search_knowledge(question)

        if not results or total_docs == 0:
            logger.error("No relevant context found in your knowledge base.")
            logger.info("Try adding more content or rebuilding the index:")
            logger.info("  python search/index.py")
            return 1

        documents = results.get("documents", [[]])[0]
        metadatas = results.get("metadatas", [[]])[0]
        distances = results.get("distances", [[]])[0]

        logger.info(f"Found {len(documents)} relevant sources")

        logger.info("Generating answer with DeepSeek...")
        prompt = build_prompt(documents, metadatas, question)
        answer = call_deepseek(api_key, prompt)

        format_response(answer, documents, metadatas, distances, question)

        log_data = _load_healing_log()
        if any(e["outcome"] == "failed" for e in log_data.get("healing_events", [])):
            _log_healing_event("SESSION_SUCCESS", "Query completed after healing attempts", [], "resolved", "Previous healing attempts succeeded. System is healthy.")
            _user_alert("Query completed successfully (with auto-healing)!", "✅")

        return 0

    except APIKeyNotConfiguredError as e:
        logger.error(str(e))
        return 1
    except SearchIndexEmptyError as e:
        logger.error(str(e))
        return 1
    except LLMQueryError as e:
        logger.error(f"LLM Error: {e}")
        _user_alert(f"Could not auto-fix. Error saved for next session.", "⚠️")
        return 1
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        _user_alert(f"Unexpected error: {e}", "❌")
        return 1


def parse_arguments() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Query the Knowledge OS with AI-powered answers.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s "What is Marc Lou's revenue?"
  %(prog)s "Tell me about startup frameworks"
  %(prog)s  # Interactive mode - will prompt for question
        """,
    )
    parser.add_argument(
        "query",
        nargs="?",
        type=str,
        help="Question to ask the knowledge base",
    )
    return parser.parse_args()


def main() -> int:
    """
    Main entry point for the RAG query system.

    Returns:
        Exit code (0 for success, 1 for error).
    """
    logger.info("=" * 60)
    logger.info("Knowledge OS - RAG Answer Generator")
    logger.info("=" * 60)

    args = parse_arguments()

    # Get query from arguments or interactive input
    query = args.query
    if not query:
        query = input("\nEnter your question: ").strip()
        if not query:
            logger.error("No question entered.")
            return 1

    return query_knowledge_base(query)


if __name__ == "__main__":
    sys.exit(main())