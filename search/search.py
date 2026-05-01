import os
import sys
import chromadb
from sentence_transformers import SentenceTransformer

CHROMA_DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "knowledge_db")
MODEL_NAME = "all-MiniLM-L6-v2"


def search_knowledge(query, n_results=5):
    chroma_client = chromadb.PersistentClient(path=CHROMA_DB_PATH)
    collection = chroma_client.get_or_create_collection(name="knowledge")

    if collection.count() == 0:
        return None, 0

    model = SentenceTransformer(MODEL_NAME)
    query_embedding = model.encode([query])

    results = collection.query(
        query_embeddings=query_embedding.tolist(),
        n_results=n_results
    )

    return results, collection.count()


def format_snippet(text, max_length=200):
    if len(text) <= max_length:
        return text
    return text[:max_length].rsplit(" ", 1)[0] + "..."


def print_results(results, total_docs):
    if not results or total_docs == 0:
        print("\nNo results found.")
        print("\nMake sure you've run the indexer first:")
        print("  python search/index.py")
        return

    documents = results.get("documents", [[]])[0]
    metadatas = results.get("metadatas", [[]])[0]
    distances = results.get("distances", [[]])[0]

    print(f"\nFound {len(documents)} results (from {total_docs} indexed documents):\n")
    print("-" * 70)

    for i, (doc, meta, dist) in enumerate(zip(documents, metadatas, distances), 1):
        score = 1 - dist
        source = meta.get("source", "Unknown")
        category = meta.get("category", "Unknown")
        file_type = meta.get("file_type", "unknown")

        file_type_label = "[transcript]" if file_type == "transcript" else "[profile]"

        print(f"{i}. {source} {file_type_label}")
        print(f"   Category: {category} | Relevance: {score:.2%}")
        print()

        snippet = format_snippet(doc)
        print(f"   {snippet}")
        print("-" * 70)


def main():
    print("=" * 70)
    print("Knowledge OS - Semantic Search")
    print("=" * 70)

    if len(sys.argv) < 2:
        print("\nUsage:")
        print("  python search/search.py \"your search query\"")
        print("\nExample:")
        print('  python search/search.py "how did marc lou validate his idea"')
        print("\nTo rebuild the index:")
        print("  python search/index.py")
        sys.exit(1)

    query = " ".join(sys.argv[1:])

    print(f'\nSearching for: "{query}"')
    print("-" * 70)

    try:
        results, total_docs = search_knowledge(query)
        print_results(results, total_docs)
    except Exception as e:
        print(f"\nError: {e}")
        print("\nMake sure you've run the indexer first:")
        print("  python search/index.py")


if __name__ == "__main__":
    main()