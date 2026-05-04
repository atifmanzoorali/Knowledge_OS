# Search Guide

Learn how to effectively search your knowledge base.

---

## Two Search Methods

Knowledge OS offers two ways to search:

| Method | Command | Best For |
|--------|---------|----------|
| **Ask** (RAG) | `python search/ask.py "question"` | Getting synthesized answers |
| **Semantic Search** | `python search/answer_search.py "query"` | Finding relevant profiles |

---

## Ask (RAG - Recommended)

This method uses AI to understand your question and synthesize an answer from your saved content.

### How It Works

1. You ask a question in natural language
2. System finds relevant content using semantic search
3. AI reads through the content
4. Synthesizes a clear answer with sources

### Examples

```bash
# Good questions
python search/ask.py "how do successful founders validate their ideas"
python search/ask.py "what are the key habits of productive people"
python search/ask.py "how does meditation improve focus"
python search/ask.py "what advice do AI leaders have for beginners"
```

### Why Use Ask

- **Understands context** - Finds answers even when keywords don't match exactly
- **Synthesizes** - Combines insights from multiple sources
- **Conversational** - Ask naturally, like talking to a research assistant

---

## Semantic Search

This method finds relevant content and returns ranked results.

### How It Works

1. Your query is converted to a vector (mathematical representation)
2. System compares against all stored content vectors
3. Returns results sorted by relevance score

### Examples

```bash
# Good queries
python search/answer_search.py "startup validation"
python search/answer_search.py "AI product strategy"
python search/answer_search.py "meditation techniques"
python search/answer_search.py "founder advice"
```

### Understanding Results

Each result shows:
- **Relevance score** - How closely it matches (0-100%)
- **Source** - Which profile/transcript
- **Category** - Which folder it came from

---

## Tips for Better Searches

### Be Specific

```bash
# Vague - may return mixed results
python search/ask.py "startups"

# Specific - returns focused answers
python search/ask.py "how do SaaS founders price their product"
```

### Use Complete Questions

```bash
# Fragment
python search/ask.py "founder mistakes"

# Question form
python search/ask.py "what mistakes do first-time founders make"
```

### Search by Concept, Not Just Keywords

```bash
# Keyword-based (works but limited)
python search/answer_search.py "revenue growth"

# Concept-based (finds more)
python search/answer_search.py "how startups scale revenue"
```

### Combine Topics

```bash
python search/ask.py "how do AI companies build products and what can startups learn from them"
```

---

## Search Limitations

- Only searches content you've added to the system
- Requires search index to be built (`python search/index.py`)
- Works best with clear, specific queries

---

## Rebuilding the Index

After adding new content, always rebuild the search index:

```bash
python search/index.py
```

This ensures new content is searchable.

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| No results found | Rebuild index: `python search/index.py` |
| Irrelevant results | Try more specific queries |
| Empty answer | Check if content exists in that topic |

---

*Last Updated: 2026-05-04*