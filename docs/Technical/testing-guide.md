# Testing Guide

This document describes the testing infrastructure for Knowledge OS.

---

## Overview

Knowledge OS uses a comprehensive testing strategy with multiple test levels:

| Level | Purpose | Command |
|-------|---------|---------|
| Unit Tests | Test individual functions in isolation | `make test-unit` |
| Integration Tests | Test component interactions | `make test-integration` |
| End-to-End Tests | Test full workflows | `make test-e2e` |

---

## Quick Start

### Install Dependencies

```bash
# Install production dependencies
make install

# Install development dependencies (includes testing tools)
make install-dev
```

### Run Tests

```bash
# Run all tests
make test

# Run with coverage
make test-all
```

---

## Test Structure

```
tests/
├── __init__.py                 # Package initialization
├── conftest.py                 # Shared pytest fixtures
├── test_transcript.py          # Transcript extraction tests
├── test_indexer.py             # Search indexer tests
├── test_search.py              # Search functionality tests
├── test_skills.py              # Skill output validation
├── test_integration.py         # End-to-end workflow tests
└── fixtures/                  # Mock data for tests
    ├── __init__.py
    ├── mock_api_responses.py   # Mock YouTube API responses
    ├── sample_transcript.md    # Sample transcript file
    └── sample_profile.md       # Sample profile file
```

---

## Writing Tests

### Unit Test Example

```python
def test_sanitize_filename():
    """Test that special characters are removed."""
    result = sanitize_filename('Test: Video "With" <Chars>')
    assert ':' not in result
    assert '"' not in result
```

### Integration Test Example

```python
def test_full_workflow(self, project_root):
    """Test complete indexing workflow."""
    # Given: A test file
    # When: We process it
    # Then: We get expected output
    result = process_file(sample_file)
    assert result is not None
```

---

## CI/CD

Tests run automatically on GitHub Actions:

```yaml
# .github/workflows/test.yml
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
      - run: pip install -r requirements-dev.txt
      - run: pytest tests/ -v
```

---

## Code Quality Tools

| Tool | Purpose | Command |
|------|---------|---------|
| **black** | Code formatting | `make format` |
| **isort** | Import sorting | `make format` |
| **flake8** | Linting | `make lint` |
| **pre-commit** | Pre-commit hooks | `make pre-commit` |

---

## Coverage

Run tests with coverage reporting:

```bash
pytest tests/ --cov=. --cov-report=html
```

Open `htmlcov/index.html` to view the coverage report.

---

## Troubleshooting

### Tests fail with "Module not found"

```bash
pip install -r requirements-dev.txt
```

### Pre-commit hooks not running

```bash
pre-commit install
```

### Coverage not showing

```bash
pip install pytest-cov
```

---

## Best Practices

1. **Write tests first** - Use TDD for new features
2. **Keep tests focused** - One assertion per test when possible
3. **Use descriptive names** - `test_function_name_scenario`
4. **Mock external dependencies** - Don't rely on real APIs
5. **Test edge cases** - Empty inputs, large inputs, errors

---

## Continuous Improvement

To improve test coverage:

1. Run `make test-all` to see current coverage
2. Identify untested modules
3. Add tests for missing functionality
4. Update this guide with new patterns

---

*Last Updated: 2026-05-03*
*Knowledge OS Testing Guide*