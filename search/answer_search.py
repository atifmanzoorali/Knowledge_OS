import os
import sys
import chromadb
from sentence_transformers import SentenceTransformer
from pathlib import Path

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

SEARCH_DIR = Path(__file__).parent
CHROMA_DB_PATH = SEARCH_DIR / "knowledge_db"
MODEL_NAME = "all-MiniLM-L6-v2"
KNOWLEDGE_OS_ROOT = SEARCH_DIR.parent


def search_knowledge(query, n_results=3):
    chroma_client = chromadb.PersistentClient(path=str(CHROMA_DB_PATH))
    collection = chroma_client.get_or_create_collection(name="knowledge")

    if collection.count() == 0:
        return None, 0, []

    model = SentenceTransformer(MODEL_NAME)
    query_embedding = model.encode([query])

    results = collection.query(
        query_embeddings=query_embedding.tolist(),
        n_results=n_results
    )

    return results, collection.count(), collection.get()


def read_file_content(file_path):
    try:
        full_path = KNOWLEDGE_OS_ROOT / file_path
        with open(full_path, "r", encoding="utf-8") as f:
            content = f.read()
            if content.startswith("---"):
                parts = content.split("---", 2)
                if len(parts) >= 3:
                    content = parts[2]
            return content.strip()
    except Exception as e:
        return f"Error reading file: {e}"


def main():
    print("=" * 60)
    print("Knowledge OS - Search")
    print("=" * 60)

    if len(sys.argv) >= 2 and sys.argv[1] == "--ask":
        import ask
        sys.argv = [sys.argv[0]] + sys.argv[2:]
        ask.main()
        return

    if len(sys.argv) < 2:
        print("\nUsage:")
        print("  python search/answer_search.py \"query\"           # Search profiles")
        print("  python search/answer_search.py --ask \"question\" # RAG answer")
        query = input("\nEnter your search: ").strip()
        if not query:
            print("No search query entered.")
            sys.exit(1)
    else:
        query = " ".join(sys.argv[1:])

    print(f'\nSearching for: "{query}"')
    print("-" * 60)

    try:
        results, total_docs, all_data = search_knowledge(query)
        
        if not results or total_docs == 0:
            print("\nNo results found.")
            print("\nMake sure you've run the indexer first:")
            print("  python search/index.py")
            return

        documents = results.get("documents", [[]])[0]
        metadatas = results.get("metadatas", [[]])[0]
        distances = results.get("distances", [[]])[0]

        print(f"\nFound {len(documents)} relevant section(s):\n")
        print("=" * 60)

        for i, (doc, meta, dist) in enumerate(zip(documents, metadatas, distances), 1):
            score = 1 - dist
            if score < 0:
                score = 0
            elif score > 1:
                score = 1
            source = meta.get("source", "Unknown")
            category = meta.get("category", "Unknown")
            file_type = meta.get("file_type", "unknown")

            file_type_label = "[transcript]" if file_type == "transcript" else "[profile]"

            print(f"\n--- RESULT {i} ---")
            print(f"Source: {source} {file_type_label}")
            print(f"Category: {category} | Relevance: {score:.2%}")
            print()
            
            print(doc)
            print("=" * 60)

        print(f"\nSource: {source}")
        print("=" * 60)

    except Exception as e:
        print(f"\nError: {e}")
        print("\nMake sure you've run the indexer first:")
        print("  python search/index.py")


if __name__ == "__main__":
    main()
