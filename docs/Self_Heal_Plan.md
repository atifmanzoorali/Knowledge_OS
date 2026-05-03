# Self-Healing Implementation Plan

## Goal
Add retry logic and error logging so the system can detect and recover from its own failures.

---

## Selected Approach: Quick (30 min) — High Impact, Low Risk

---

## Technical Decisions Made

| Decision | Choice |
|----------|--------|
| **Approach** | Quick (retry + logging only) |
| **Log Directory** | `logs/` in project root |
| **Log Format** | JSON |
| **Safety** | No breaking changes, all errors to log file |

---

## Files to Modify

| File | Changes |
|------|---------|
| `search/ask.py` | Add tenacity retry to `call_deepseek()`, add error logging |
| `scripts/Transcript_Extraction.py` | Add retry to `get_transcript()`, add error logging |
| `search/config.py` | Add log directory path |
| New: `logs/` | Create directory |
| New: `logs/errors.log` | Empty file (logs will be appended) |

---

## Implementation Steps

### Step 1: Configure log directory in `search/config.py`
- Add `LOG_DIR` path pointing to `logs/` directory in project root

### Step 2: Update `search/ask.py`
- Import tenacity and logging
- Add `@retry` decorator to `call_deepseek()` with 3 attempts, exponential backoff
- Add JSON error logging for any exceptions that occur

### Step 3: Update `scripts/Transcript_Extraction.py`
- Import tenacity and logging
- Add `@retry` decorator to `get_transcript()` with 3 attempts
- Add JSON error logging for transcript and metadata failures

### Step 4: Verify
- Run tests to ensure nothing broke
- Verify log files are created

---

## Success Criteria

- [ ] API calls retry automatically (3 attempts with backoff)
- [ ] All errors logged to `logs/errors.log` as JSON
- [ ] User sees clean output (no error messages on screen)
- [ ] Existing functionality works unchanged

---

## For Next Session

When implementing:
1. Read this plan file first
2. Execute the 4 steps above
3. Verify everything works
4. Update the Rating Assessment

---

*Created: 2026-05-03*