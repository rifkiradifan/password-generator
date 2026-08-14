# Password/Secrets Generator CLI

A CLI to generate cryptographically secure random passwords, with configurable length and charset.


> Status: work in progress (Phase 1) — sections below will be filled in as the project progresses.

---

## What it does

Generates random passwords using Python's `secrets` module (CSPRNG), instead of `random`, which is not safe for cryptographic purposes. Password length and character categories (uppercase, lowercase, digits, symbols) are configurable via CLI flags.

---

## Why I'm building it

With a background in SRE/Cloud Engineering, I'm familiar with secrets management and credential rotation concepts in production, but had never written a generator myself. I'm building this to learn Python fundamentals (`secrets`, `argparse`) while connecting them to real-world security practices.

---

## Stack

| Component | Technology | Notes |
|---|---|---|
| Language | Python 3.13 | |
| Package manager | uv | |
| CLI parsing | `argparse` (stdlib) | |
| Random generator | `secrets` (stdlib) | CSPRNG, not `random` |
| Linting & formatting | ruff |  |
| Type checking | mypy | |
| Testing | pytest | |
| Dependency security scan | pip-audit | |
| Pre-commit hooks | pre-commit | |
| Task runner | Just (`Justfile`) | |

---

## Folder Structure

```
password-generator/
├── main.py
├── pyproject.toml
├── uv.lock
├── .python-version
├── .gitignore
└── README.md
```

---

## Installation

Requires Python 3.13+ and [`uv`](https://docs.astral.sh/uv/). No manual venv setup needed — `uv run` creates and syncs `.venv` automatically on first use.

---

## How to Run

```bash
uv run python main.py
```

> Currently prints a single cryptographically secure random lowercase letter (`secrets.choice`). CLI flags (`--length`, charset toggles, `--count`) are still in progress — see [ROADMAP.md](ROADMAP.md).

---

## Roadmap

Detailed execution roadmap is in [ROADMAP.md](ROADMAP.md).

---

## What I learned

not yet available

---

## License

MIT — see [LICENSE](LICENSE).