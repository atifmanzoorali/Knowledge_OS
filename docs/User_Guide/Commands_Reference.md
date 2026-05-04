# Commands Reference

Quick reference for all commands in Knowledge OS.

---

## Search Commands

### Ask the Knowledge Base (RAG)

```bash
python search/ask.py "your question here"
```

Uses AI to understand your question and synthesize an answer from your saved content.

**Examples:**
```bash
python search/ask.py "how do founders validate product ideas"
python search/ask.py "what are the key traits of successful AI leaders"
python search/ask.py "how does meditation help with focus"
```

### Semantic Search

```bash
python search/answer_search.py "search query"
```

Returns relevant profiles ranked by relevance score.

**Examples:**
```bash
python search/answer_search.py "startup validation"
python search/answer_search.py "AI product strategy"
```

### Rebuild Search Index

```bash
python search/index.py
```

Rebuilds the vector search index. Run this after adding new content.

---

## Processing Commands

### Process a YouTube Video

Use the **Process_Link** skill via opencode:
1. Provide a YouTube URL
2. System extracts transcript
3. AI analyzes and creates profile
4. Updates search index

---

## Testing Commands

```bash
# Run all tests
make test

# Run with coverage
make test-all

# Run specific test types
make test-unit
make test-integration
make test-e2e
```

---

## Code Quality Commands

```bash
# Format code
make format

# Run linter
make lint

# Install pre-commit hooks
make pre-commit
```

---

## Make Commands Summary

| Command | Description |
|---------|-------------|
| `make install` | Install dependencies |
| `make install-dev` | Install dev dependencies |
| `make test` | Run tests |
| `make test-all` | Run tests with coverage |
| `make format` | Format code |
| `make lint` | Lint code |
| `make pre-commit` | Setup pre-commit hooks |
| `make clean` | Clean temporary files |

---

## Tips

- **Always rebuild index** after adding new content: `python search/index.py`
- **Use natural questions** with ask.py - it understands context
- **Check logs** if something fails: `logs/errors.log`

---

*Last Updated: 2026-05-04*