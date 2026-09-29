# Password/Secrets Generator CLI

A CLI to generate cryptographically secure random passwords, with configurable length and charset.


> Status: Phase 1 ongoing.

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

Not available yet.

---

## Installation

Not available yet.

---

## How to Run

Not available yet.

---

## Roadmap

Detailed execution roadmap is in [ROADMAP.md](ROADMAP.md).

---

## License

MIT — see [LICENSE](LICENSE).