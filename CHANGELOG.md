# Changelog

Versions of the Zero Clutter system. Each skill also keeps its own changelog.

## 0.4.4 — 2026-10-29

- **No small type except the terms.** Text under the floor (14pt on iOS,
  14sp on Android, 14px on web and Flutter), and any caption, footnote or
  extra-small style, is flagged. The only exception is the terms and
  conditions. See HIER-11 and HR-15.

## 0.4.3 — 2026-10-29

- **Answers are tables.** The chat verdict, every finding, Keep and Next, and
  the feedback-mode entry are Markdown tables. The CI gate prints the same
  tables. See `references/report-format.md`.

## 0.4.2 — 2026-10-29

- **Every symbol renders as colour emoji.** The fix line now uses 🎯 (was a
  pencil) and the question line ❓ (was a speech bubble). Both old symbols showed
  as small black glyphs in GitHub's code blocks. `scripts/check.py` now fails on
  any emoji that needs a variation selector to show in colour.

## 0.4.1 — 2026-10-29

- **One framed block.** The answer is a `text` code block with a left border
  (`╭─ ├─ │ ╰─`) and a labelled divider per section, so it looks the same in
  every terminal, IDE, chat and on GitHub, and keeps its alignment.
- **Easy to scan.** An emoji per section (🔧 Fix, 🤔 Decide, 💡 Suggest, ⏳ Check,
  ✅ Keep, 👉 Next), a severity dot on every finding and on the totals
  (🔴 blocking, 🟠 major, 🟡 minor), and a verdict badge (✅ PASS, ❌ FAIL,
  🟢 READY, 🟡 OPEN).
- **Findings numbered per section** (F1, D1, S1): 📍 what's wrong, the where
  under it, 🎯 the fix (❓ the question in Decide). Lines wrap at about 90
  characters.
- `gate.py` prints the same frame.

## 0.4.0 — 2026-10-29

- **Runs on anything with a UI.** New `references/platforms.md`: how to find
  the platform (native iOS, native Android, Flutter, web app, website) and
  collect evidence on each (screenshots, smallest size, large text, motion,
  contrast, speed), plus the checks that change by platform (safe areas and
  haptics on phones, keyboard and focus on the web, Web Vitals on websites).
- **Clean, grouped answer.** A verdict line, then **Fix**, **Decide**,
  **Suggest**, **Check**, **Keep** and **Next**. Findings are numbered and
  take three short lines each: ID, principle and severity; what and where;
  the fix. Markdown, so it renders well in Claude Code, Cursor and chat.
  Follows Conventional Comments; see `references/report-format.md`.
- **SARIF reports.** pr mode writes `.zero-clutter/reports/<date>-<name>.sarif`
  next to the Markdown report; other modes on request.
- **CI gate.** `skills/zero-clutter/scripts/gate.py` reads the reports,
  prints the same grouped summary, annotates the PR and fails on blocking
  findings. Example workflow: `examples/ci/zero-clutter-gate.yml`. Sample
  report: `examples/reports/onboarding-option-3.sarif`.
- Result words unified across the mode guides (`pass`, `issue`, `question`,
  `pending`, `n/a`).

## 0.3.0 — 2026-10-29

- **One command, any tool.** Zero Clutter is now a single `zero-clutter` skill
  that picks the gate from what you give it (spec, design, change, PR,
  first-use, feedback) and answers in a few lines: `✗` findings with the fix,
  `?` questions for the approver, passes as a count.
- **Plugins:** Claude Code plugin and marketplace (`.claude-plugin/`), Cursor
  plugin (`.cursor-plugin/`, with a command and a rule), Gemini CLI extension.
  The installer covers Codex, Copilot and manual installs.
- **Generic, project-aware.** Reads the project's `AGENTS.md`, README and
  `.zero-clutter/adapter.md` first. Each repo keeps its own house rules and
  feedback log in `.zero-clutter/`; `zero-clutter setup` creates them. The
  approver is Bhavin unless the project names someone else.
- **Reviewer agent** (`agents/zero-clutter-reviewer.md`) runs the full PR
  review in its own context.
- The gate skills from 0.2.0 became the skill's mode guides in
  `skills/zero-clutter/references/`. Delight Police moved to
  `skills/delight-police/`, unchanged. RyzeDesign's log is now a worked
  example in `examples/ryzedesign/`.
- `scripts/check.py` also checks every relative link and that all manifests
  share one name and version.

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
