"""
Semantic Search Indexer for Knowledge OS.

Builds a vector search index from all markdown files in the knowledge base.
Uses ChromaDB for persistent vector storage and sentence-transformers
for embedding generation.

Usage:
    python -m search.index

Or:
    python search/index.py
"""

import glob
import logging
import os
from pathlib import Path
from typing import Any

import chromadb
from sentence_transformers import SentenceTransformer

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)

# Constants
CATEGORIES: list[str] = [
    "Starter_Story",
    "Inner_Work",
    "AI_Leaders",
    "Founders",
    "My_First_Million",
    "AI_Engineering",
]

DATA_SUBDIRS: list[str] = ["Raw_Data", "Process_data", "Process_Data"]

MODEL_NAME: str = "all-MiniLM-L6-v2"

# Determine project root
_knowledge_os_root = Path(__file__).parent.parent.resolve()
_chroma_db_path = Path(__file__).parent / "knowledge_db"


def get_project_root() -> Path:
    """Get the project root directory."""
    return _knowledge_os_root


def get_chroma_db_path() -> Path:
    """Get the ChromaDB storage path."""
    return _chroma_db_path


def find_markdown_files(
    root_path: Path | None = None,
    categories: list[str] | None = None,
) -> list[str]:
    """
    Find all markdown files in the knowledge base categories.

    Args:
        root_path: Root directory of Knowledge OS. Defaults to project root.
        categories: List of category folder names. Defaults to CATEGORIES.

    Returns:
        List of absolute file paths to markdown files.
    """
    if root_path is None:
        root_path = _knowledge_os_root
    if categories is None:
        categories = CATEGORIES

    md_files: list[str] = []

    for category in categories:
        category_path = root_path / category
        if not category_path.exists():
            logger.debug(f"Category folder not found: {category_path}")
            continue

        for subdir in DATA_SUBDIRS:
            subdir_path = category_path / subdir
            if not subdir_path.exists():
                continue

            pattern = str(subdir_path / "*.md")
            files = glob.glob(pattern)
            md_files.extend(files)
            logger.debug(f"Found {len(files)} files in {subdir_path}")

    return md_files


def read_file_content(file_path: str) -> str:
    """
    Read content from a markdown file, stripping YAML frontmatter.

    Args:
        file_path: Path to the markdown file.

    Returns:
        File content with YAML frontmatter removed. Empty string on error.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            # Strip YAML frontmatter
            if content.startswith("---"):
                parts = content.split("---", 2)
                if len(parts) >= 3:
                    content = parts[2]
            return content.strip()
    except OSError as e:
        logger.error(f"Error reading {file_path}: {e}")
        return ""
    except Exception as e:
        logger.error(f"Unexpected error reading {file_path}: {e}")
        return ""


def get_category_from_path(file_path: str, categories: list[str] | None = None) -> str:
    """
    Extract category name from file path.

    Args:
        file_path: Path to the markdown file.
        categories: List of valid category names. Defaults to CATEGORIES.

    Returns:
        Category name if found, otherwise "Unknown".
    """
    if categories is None:
        categories = CATEGORIES

    for category in categories:
        if category in file_path:
            return category
    return "Unknown"


def get_file_type_from_path(file_path: str) -> str:
    """
    Determine if file is a raw transcript or processed profile.

    Args:
        file_path: Path to the markdown file.

    Returns:
        "transcript" for Raw_Data, "profile" for Process_data, "unknown" otherwise.
    """
    if "Raw_Data" in file_path:
        return "transcript"
    if "Process_data" in file_path or "Process_Data" in file_path:
        return "profile"
    return "unknown"


def prepare_documents(
    md_files: list[str],
) -> tuple[list[str], list[dict[str, Any]], list[str]]:
    """
    Prepare documents for indexing by reading content and extracting metadata.

    Args:
        md_files: List of markdown file paths.

    Returns:
        Tuple of (documents list, metadata list, ids list).
    """
    documents: list[str] = []
    metadatas: list[dict[str, Any]] = []
    ids: list[str] = []

    for i, file_path in enumerate(md_files):
        content = read_file_content(file_path)
        if not content:
            logger.warning(f"Skipping empty file: {file_path}")
            continue

        rel_path = os.path.relpath(file_path, _knowledge_os_root)
        file_id = f"doc_{i}"

        documents.append(content)
        metadatas.append({
            "source": rel_path,
            "category": get_category_from_path(file_path),
            "file_type": get_file_type_from_path(file_path),
        })
        ids.append(file_id)

        logger.debug(f"Prepared: {rel_path}")

    return documents, metadatas, ids


def build_index(
    documents: list[str],
    metadatas: list[dict[str, Any]],
    ids: list[str],
    model: SentenceTransformer,
) -> chromadb.Collection:
    """
    Build ChromaDB index from documents and embeddings.

    Args:
        documents: List of document texts.
        metadatas: List of metadata dictionaries.
        ids: List of document IDs.
        model: Sentence transformer model for embeddings.

    Returns:
        The created ChromaDB collection.
    """
    logger.info("Generating embeddings...")
    embeddings = model.encode(documents, show_progress_bar=True)

    logger.info(f"Creating index with {len(documents)} documents...")
    chroma_client = chromadb.PersistentClient(path=str(_chroma_db_path))
    collection = chroma_client.get_or_create_collection(name="knowledge")

    collection.add(
        embeddings=embeddings.tolist(),
        documents=documents,
        metadatas=metadatas,
        ids=ids,
    )

    return collection


def main() -> int:
    """
    Main entry point for the indexer.

    Returns:
        Exit code (0 for success, 1 for error).
    """
    logger.info("=" * 60)
    logger.info("Knowledge OS - Semantic Search Indexer")
    logger.info("=" * 60)

    try:
        # Step 1: Load embedding model
        logger.info(f"Loading embedding model: {MODEL_NAME}...")
        model = SentenceTransformer(MODEL_NAME)
        logger.info("Model loaded successfully!")

        # Step 2: Scan for markdown files
        logger.info("Scanning for markdown files...")
        md_files = find_markdown_files()
        logger.info(f"Found {len(md_files)} files")

        if not md_files:
            logger.warning("No markdown files found. Nothing to index.")
            return 0

        # Step 3: Read file contents
        logger.info("Reading file contents...")
        documents, metadatas, ids = prepare_documents(md_files)

        if not documents:
            logger.warning("No valid documents to index.")
            return 0

        logger.info(f"Total: {len(documents)} documents ready for indexing")

        # Step 4: Create embeddings and store in Chroma
        build_index(documents, metadatas, ids, model)

        # Success message
        logger.info("=" * 60)
        logger.info("Indexing complete!")
        logger.info(f"  - Indexed {len(documents)} documents")
        logger.info(f"  - Database stored at: {_chroma_db_path}")
        logger.info("=" * 60)

        return 0

    except Exception as e:
        logger.error(f"Indexing failed: {e}")
        return 1


if __name__ == "__main__":
    import sys
    sys.exit(main())