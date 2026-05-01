import os
import glob
import chromadb
from sentence_transformers import SentenceTransformer

KNOWLEDGE_OS_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHROMA_DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "knowledge_db")

CATEGORIES = [
    "Starter_Story",
    "Inner_Work",
    "AI_Leaders",
    "Founders",
    "My_First_Million",
    "AI_Engineering"
]

DATA_SUBDIRS = ["Raw_Data", "Process_data", "Process_Data"]

MODEL_NAME = "all-MiniLM-L6-v2"


def find_markdown_files():
    md_files = []
    for category in CATEGORIES:
        category_path = os.path.join(KNOWLEDGE_OS_ROOT, category)
        if not os.path.exists(category_path):
            continue
        for subdir in DATA_SUBDIRS:
            subdir_path = os.path.join(category_path, subdir)
            if os.path.exists(subdir_path):
                pattern = os.path.join(subdir_path, "*.md")
                files = glob.glob(pattern)
                md_files.extend(files)
    return md_files


def read_file_content(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            if content.startswith("---"):
                parts = content.split("---", 2)
                if len(parts) >= 3:
                    content = parts[2]
            return content.strip()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return ""


def get_category_from_path(file_path):
    for category in CATEGORIES:
        if category in file_path:
            return category
    return "Unknown"


def get_file_type_from_path(file_path):
    if "Raw_Data" in file_path:
        return "transcript"
    elif "Process_data" in file_path or "Process_Data" in file_path:
        return "profile"
    return "unknown"


def main():
    print("=" * 60)
    print("Knowledge OS - Semantic Search Indexer")
    print("=" * 60)

    print(f"\n[1/4] Loading embedding model: {MODEL_NAME}...")
    model = SentenceTransformer(MODEL_NAME)
    print("      Model loaded successfully!")

    print("\n[2/4] Scanning for markdown files...")
    md_files = find_markdown_files()
    print(f"      Found {len(md_files)} files")

    if not md_files:
        print("\nNo markdown files found. Nothing to index.")
        return

    print("\n[3/4] Reading file contents...")
    documents = []
    metadatas = []
    ids = []

    for i, file_path in enumerate(md_files):
        content = read_file_content(file_path)
        if not content:
            continue

        rel_path = os.path.relpath(file_path, KNOWLEDGE_OS_ROOT)
        file_id = f"doc_{i}"

        documents.append(content)
        metadatas.append({
            "source": rel_path,
            "category": get_category_from_path(file_path),
            "file_type": get_file_type_from_path(file_path)
        })
        ids.append(file_id)

        print(f"      {i+1}. {rel_path}")

    if not documents:
        print("\nNo valid documents to index.")
        return

    print(f"\n      Total: {len(documents)} documents ready for indexing")

    print("\n[4/4] Creating embeddings and storing in Chroma...")
    embeddings = model.encode(documents, show_progress_bar=True)

    chroma_client = chromadb.PersistentClient(path=CHROMA_DB_PATH)
    collection = chroma_client.get_or_create_collection(name="knowledge")

    collection.add(
        embeddings=embeddings.tolist(),
        documents=documents,
        metadatas=metadatas,
        ids=ids
    )

    print(f"\n{'=' * 60}")
    print(f"Indexing complete!")
    print(f"  - Indexed {len(documents)} documents")
    print(f"  - Database stored at: {CHROMA_DB_PATH}")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()