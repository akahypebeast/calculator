# Calculator

A simple browser-based calculator with a Python (Flask) backend.

## Quick Start

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd calculator
```

### 2. Create virtual environment and install dependencies

```bash
bash scripts/create_venv.sh
source .venv/bin/activate
```

### 3. Run the web calculator

```bash
python main.py web
```

Open [http://localhost:5000](http://localhost:5000) in your browser.

### 4. Run via CLI

```bash
python main.py 10 add 5
python main.py 20 divide 4
python main.py 3 multiply 7
```

---

## Development

### Format code

```bash
bash scripts/format.sh
```

### Check formatting (no changes)

```bash
bash scripts/format_check.sh
```

### Run linter

```bash
bash scripts/lint.sh
```

### Run tests

```bash
bash scripts/test.sh
```

### Clean repository

```bash
bash scripts/clean.sh
```

---

## CI Pipeline

GitHub Actions runs automatically on every push to `main`, `master`, `develop` and on Pull Requests to `main`/`master`.

The pipeline performs these steps in order:

1. **Set up Python 3.12**
2. **Create virtualenv & install dependencies** — `scripts/create_venv.sh`
3. **Format check** — verifies all files comply with `black` formatting
4. **Lint** — runs `pylint` on source and test files
5. **Tests** — runs `pytest` on the `tests/` directory

All steps must pass (green) before a PR can be considered complete.

---

## Project Structure

```
calculator/
├── calculator/
│   ├── __init__.py
│   └── logic.py          # Core arithmetic functions
├── tests/
│   ├── __init__.py
│   └── test_logic.py     # Unit tests
├── static/
│   └── index.html        # Browser UI
├── scripts/
│   ├── create_venv.sh
│   ├── format.sh
│   ├── format_check.sh
│   ├── lint.sh
│   ├── test.sh
│   └── clean.sh
├── .github/
│   └── workflows/
│       └── python-app.yml
├── main.py               # CLI entry point + Flask server
├── pyproject.toml        # Tool configuration
├── requirements.txt
└── README.md
```
