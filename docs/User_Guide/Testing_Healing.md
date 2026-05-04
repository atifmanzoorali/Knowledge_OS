# Testing & Healing

Learn how the system tests itself and automatically recovers from errors.

---

## Testing

Knowledge OS uses automated tests to ensure everything works correctly. Tests run every time you push code to GitHub.

### Test Levels

| Level | Purpose | When to Run |
|-------|---------|-------------|
| **Unit Tests** | Test individual functions in isolation | After making small changes |
| **Integration Tests** | Test that components work together | After adding new features |
| **End-to-End Tests** | Test complete workflows | Before submitting changes |

### Running Tests

```bash
# Run all tests
make test

# Run specific test level
make test-unit
make test-integration
make test-e2e

# Run with coverage report
make test-all
```

### What Gets Tested

- Transcript extraction from YouTube videos
- Search index building and querying
- Skill transformations (AI analysis)
- Full pipeline from URL to saved profile
- Error handling and edge cases

---

## Self-Healing

The system automatically recovers from common errors without requiring manual intervention.

### How It Works

When an error occurs, the system tries to fix it automatically before giving up.

| Error | Auto-Fix Strategy |
|-------|-------------------|
| **Rate Limit** (too many API calls) | Wait 5s → 10s → 20s, then retry (3 attempts) |
| **Timeout** (request too slow) | Reduce response size by 25%, retry |
| **API Error** | Exponential backoff and retry (3 attempts) |
| **Transcript in other language** | Try: en-US → en-GB → en → auto → es → pt |
| **Empty search index** | Automatically rebuild the index |

### Status Messages

You'll see these symbols when the system is healing itself:

| Symbol | Meaning |
|--------|---------|
| 📡 | Rate limited, waiting before retry |
| ⏱️ | Timeout occurred, reducing request size |
| 🌐 | Trying different language for transcript |
| 🔄 | Rebuilding search index |
| ⚠️ | Error occurred, attempting fix |
| ✅ | Problem fixed successfully |

### Healing Log

Every healing event is saved to `logs/healing_log.json`. This helps future sessions understand what was tried and what worked.

**Log format:**
```json
{
  "session_date": "2026-05-04",
  "healing_events": [
    {
      "timestamp": "2026-05-04T10:30:00",
      "error_type": "API_RATE_LIMIT",
      "error_message": "Rate limit exceeded",
      "fixes_tried": [
        {"attempt": 1, "action": "wait_5s_retry", "result": "failed"},
        {"attempt": 2, "action": "wait_10s_retry", "result": "success"}
      ],
      "outcome": "resolved",
      "next_agent_note": "Rate limit resolved after 2 attempts"
    }
  ]
}
```

### What Healing Can't Fix

The system only heals within tight bounds:
- Retries and waiting
- Language fallbacks
- Index rebuilds

It will **not** automatically:
- Change code or configuration
- Delete files
- Modify external API settings

These require human approval.

---

## Viewing Logs

All logs are stored in the `logs/` folder:

```bash
# View error logs
notepad logs\errors.log

# View healing events
notepad logs\healing_log.json
```

---

*Last Updated: 2026-05-04*