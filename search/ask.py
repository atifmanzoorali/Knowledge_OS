import sys
import os
from pathlib import Path

SEARCH_DIR = Path(__file__).parent
sys.path.insert(0, str(SEARCH_DIR))

import chromadb
import config
from sentence_transformers import SentenceTransformer

if sys.platform == "win32":
    import io
    try:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace', line_buffering=False)
    except Exception:
        pass


def load_api_key():
    if not config.API_KEY or config.API_KEY == "your_key_here":
        print("ERROR: DeepSeek API key not configured.")
        print("\nTo fix:")
        print("1. Get your free API key at: https://platform.deepseek.com/")
        print(f"2. Edit the .env file at: {config.ROOT_DIR / '.env'}")
        print("3. Replace 'your_key_here' with your actual API key")
        print("4. Run this command again")
        sys.exit(1)
    return config.API_KEY


def search_knowledge(query, n_results=None):
    if n_results is None:
        n_results = config.N_RESULTS

    chroma_client = chromadb.PersistentClient(path=str(config.CHROMA_DB_PATH))
    collection = chroma_client.get_or_create_collection(name="knowledge")

    if collection.count() == 0:
        return None, 0, []

    model = SentenceTransformer(config.MODEL_NAME_EMBED)
    query_embedding = model.encode([query])

    results = collection.query(
        query_embeddings=query_embedding.tolist(),
        n_results=n_results
    )

    return results, collection.count(), collection.get()


def read_file_content(rel_path):
    try:
        full_path = config.KNOWLEDGE_OS_ROOT / rel_path
        with open(full_path, "r", encoding="utf-8") as f:
            content = f.read()
            if content.startswith("---"):
                parts = content.split("---", 2)
                if len(parts) >= 3:
                    content = parts[2]
            return content.strip()
    except Exception as e:
        return f"Error reading file: {e}"


def build_prompt(context_docs, metadatas, question):
    context_parts = []
    for i, (doc, meta) in enumerate(zip(context_docs, metadatas)):
        source = meta.get("source", "Unknown")
        truncated_doc = doc[:1500] if len(doc) > 1500 else doc
        context_parts.append(f"--- Source {i+1}: {source} ---\n{truncated_doc}\n")

    context = "\n".join(context_parts)

    prompt = f"""You are a helpful assistant that answers questions based on the user's knowledge base.
Use the provided context from their knowledge files to answer accurately.
Always cite sources when making claims. Be concise but thorough. If the context doesn't contain enough information to answer the question, say so.

Context from knowledge base:
{context}

Question: {question}

Instructions: Answer based on the context above. Cite the specific source files when making claims."""

    return prompt


def call_deepseek(api_key, prompt):
    from openai import OpenAI

    client = OpenAI(
        api_key=api_key,
        base_url="https://api.deepseek.com"
    )

    response = client.chat.completions.create(
        model=config.MODEL_NAME,
        messages=[
            {"role": "system", "content": "You are a helpful assistant that answers questions based on the user's knowledge base."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=config.MAX_TOKENS,
        temperature=config.TEMPERATURE
    )

    return response.choices[0].message.content


def format_response(answer, documents, metadatas, distances, query):
    print("\n" + "=" * 60)
    print(f"Question: {query}")
    print("=" * 60)
    print("\n📝 Answer:\n")
    print(answer)
    print("\n" + "-" * 60)
    print("\n📚 Sources (ranked by relevance):\n")

    for i, (doc, meta, dist) in enumerate(zip(documents, metadatas, distances), 1):
        score = 1 - dist  # May be negative if distance > 1
        if score < 0:
            score = 0
        elif score > 1:
            score = 1
        source = meta.get("source", "Unknown")
        category = meta.get("category", "Unknown")
        file_type = meta.get("file_type", "unknown")
        file_type_label = "[profile]" if file_type == "profile" else "[transcript]"

        print(f"  {i}. {source} {file_type_label}")
        print(f"     Category: {category} | Relevance: {score:.1%}")
        print()


def main():
    print("=" * 60)
    print("Knowledge OS - RAG Answer Generator")
    print("=" * 60)

    if len(sys.argv) < 2:
        query = input("\nEnter your question: ").strip()
        if not query:
            print("No question entered.")
            sys.exit(1)
    else:
        query = " ".join(sys.argv[1:])

    api_key = load_api_key()

    print(f'\nSearching for relevant context...')
    print("-" * 40)

    try:
        results, total_docs, all_data = search_knowledge(query)

        if not results or total_docs == 0:
            print("\nNo relevant context found in your knowledge base.")
            print("Try adding more content or rebuilding the index:")
            print("  python search/index.py")
            return

        documents = results.get("documents", [[]])[0]
        metadatas = results.get("metadatas", [[]])[0]
        distances = results.get("distances", [[]])[0]

        print(f"Found {len(documents)} relevant sources")

        print("\nGenerating answer with DeepSeek...")
        print("-" * 40)

        prompt = build_prompt(documents, metadatas, query)
        answer = call_deepseek(api_key, prompt)

        format_response(answer, documents, metadatas, distances, query)

        print("=" * 60)

    except Exception as e:
        print(f"\nError: {e}")
        print("\nMake sure you've:")
        print("1. Set your DeepSeek API key in .env")
        print("2. Run 'python search/index.py' to build the index")
        sys.exit(1)


if __name__ == "__main__":
    main()