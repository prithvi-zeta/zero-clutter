# Changelog

Versions of the Zero Clutter system. Each skill also keeps its own changelog.

## 0.2.0 — 2026-10-29

- Zero Clutter becomes the quality system for every project, not just a
  collection of skills.
- `principles/`: Bhavin's *Design for Delight Principles* and *The Science
  behind Delight*, word for word, as the one source of truth.
- `checklist/`: the 15-question checklist for people, and 134 portable items
  with stable IDs (from RyzeDesign's checklist, with stack-specific verify
  steps moved to project adapters).
- `gates/`: six gates, G1 spec to G6 release, with owners and exit criteria.
- `feedback-log/`: log of review feedback (19 entries seeded from RyzeDesign)
  and 14 house rules learned from it; zero-escape policy.
- `skills/`: spec-check (G1), build-gate (G3, G4), first-use (G5),
  feedback-intake (the loop). Delight Police (G1, G2) unchanged.
- `templates/`: PR template, review report, ticket checklist, first-use test,
  project adapter.
- `scripts/install.py`: installs every skill for Claude Code, Cursor, Codex and
  Copilot, and adopts a repo with `--project`. `scripts/check.py` and a CI
  workflow keep principles, IDs, rules and log entries consistent.

## 0.1.1 — 2026-10-28

- Delight Police skill (see `delight-police/CHANGELOG.md`).
