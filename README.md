## Typed Python Starter

A small, modern Python project scaffold with type annotations, `mypy` type checking, and `pytest` tests.

### Requirements
- Python 3.10+

### Setup
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -U pip
pip install -e .
pip install mypy pytest
```

### Run
```bash
PYTHONPATH=src python -m typed_app.main
```

### Type check
```bash
mypy .
```

### Test
```bash
pytest
```

### Project layout
```
src/
  typed_app/
    __init__.py
    main.py
    models.py
    functions.py
tests/
  test_basic.py
```
# typed-python-starter
# typed-python-starter
