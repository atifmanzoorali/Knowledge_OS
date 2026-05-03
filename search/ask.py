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
import logging
import sys
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


def call_deepseek(api_key: str, prompt: str) -> str:
    """
    Call DeepSeek API to generate an answer.

    Args:
        api_key: DeepSeek API key.
        prompt: Formatted prompt with context and question.

    Returns:
        Generated answer text.

    Raises:
        LLMQueryError: If the API call fails.
    """
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
            max_tokens=config.max_tokens,
            temperature=config.temperature,
        )

        return response.choices[0].message.content

    except Exception as e:
        raise LLMQueryError(f"Failed to query DeepSeek: {e}") from e


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
        # Load API key
        api_key = load_api_key()

        # Search knowledge base
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

        # Generate answer
        logger.info("Generating answer with DeepSeek...")
        prompt = build_prompt(documents, metadatas, question)
        answer = call_deepseek(api_key, prompt)

        # Display response
        format_response(answer, documents, metadatas, distances, question)

        return 0

    except APIKeyNotConfiguredError as e:
        logger.error(str(e))
        return 1
    except SearchIndexEmptyError as e:
        logger.error(str(e))
        return 1
    except LLMQueryError as e:
        logger.error(f"LLM Error: {e}")
        return 1
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
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