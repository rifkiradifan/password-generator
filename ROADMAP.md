# Roadmap — Password/Secrets Generator CLI

My execution plan for this project, broken into phases. I'll check items off as I go.

## Phase 1 — Small Project

- [x] Set up project (`uv init`) → verify: `main.py` & `pyproject.toml` created
- [x] Understand why `secrets` is used instead of `random` → verify: able to explain the difference
- [x] Generate 1 secure character from a single charset → verify: code runs, prints 1 character
- [x] Loop into a string of length N → verify: password of length N printed
- [x] Add `argparse` for `--length` → verify: length configurable via CLI
- [ ] Add charset toggles (`--no-uppercase`, etc.) → verify: charset changes according to flags
- [ ] Add `--count` to generate multiple passwords at once → verify: multiple passwords printed
- [ ] `README.md`, `.gitignore`, first commit → verify: ready to push to GitHub

## Phase 2 — Medium Project

- [ ] Move structure to `src/` + `tests/` (per my Python folder structure standard)
- [ ] Set up `ruff` + `mypy` in `pyproject.toml`
- [ ] Write tests with `pytest` (`@pytest.mark.parametrize` for charset combinations & length edge cases)
- [ ] Set up `pip-audit` for dependency scanning
- [ ] Set up pre-commit hooks (`ruff` + `mypy`)
- [ ] Create `Justfile` (`lint`, `test`, `security`, `check`, `format`)
- [ ] Verify: `just check` all green, push per feature

## Phase 3 — Large Project (optional)

This CLI is realistically "done" after Phase 2. I'd only come back to this phase if I decide to turn it into something bigger than a local CLI:

- [ ] Add `structlog` for audit logging (log the generate *event*, never the password value itself — that's the whole hygiene lesson)
- [ ] Load default policy (length, charset) from environment variables via `pydantic-settings`, instead of hardcoding
- [ ] Wrap it as a small FastAPI endpoint with `lifespan` + graceful SIGTERM shutdown, if I ever want to run it as a service instead of a local CLI

## Backlog — ideas for later

Things I might explore after Phase 1 is solid. Not committing to these yet.

- Passphrase mode (diceware-style, word-based)
- Exclude ambiguous characters
- Guarantee at least 1 character per active category
- Entropy/strength indicator in the output
