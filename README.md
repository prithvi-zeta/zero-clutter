# Zero Clutter

One command that checks anything you design or build against Bhavin's
**Design for Delight** principles and tells you, in a few lines, what passed,
what failed and how to fix it.

Works on anything with a UI: **native iOS and Android apps, Flutter apps, web
apps and websites**, from code, a running build, a URL, a screenshot or a
Figma frame. Works for designers, PMs and engineers, in Claude Code, Cursor,
Codex, GitHub Copilot, Gemini CLI, or plain chat, and in any repo: it reads
the project's own context and rules first.

| Gate | Subject | Verdict | Blocking | Major | Minor | Pending | Passed | N/A |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| design (G2) | Onboarding plans screen | FAIL | 1 | 2 | 0 | 1 | 38/42 | 6 |

| # | Kind | ID | Principle | Severity | What's wrong | Where | Fix |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Fix | HIER-04 | Hierarchy | blocking | 3 plans side by side to scan across | plans › table | One plan per card, with a Base, Plus or Premium switcher |
| 2 | Fix | CLUT-01 | Clutter | major | "Benefits apply until end of next month" repeated under each plan | | Say it once, under the list |
| 3 | Decide | WORD-05 | Words | major | "$250 in monthly card spends" and "$250 card spend / month" both used | | Keep one? (recommend: the first) |
| | Check | FB-01 | Feedback | pending | press states | | on a device |

| | |
| --- | --- |
| Keep | APY is the biggest thing on screen · one Continue · no tooltips |
| Next | Fix 1, then send 3 to the approver |

## What to expect

- **You type one thing.** `/zero-clutter`, or just "zero clutter this", "gate
  this", "is this ready?". It works out what you gave it (a spec, a design, a
  change, a PR, feedback) and runs the right gate.
- **You get tables.** A verdict table, then one row per finding (what to
  fix, what to decide, what still needs a check), then Keep and Next.
  Say "details" for the full report.
- **It judges, it doesn't redesign.** It won't silently change what the spec
  asks for; a principle the spec breaks comes back as a question for the
  approver.
- **The goal:** by the time Bhavin sees the work, it already passes his
  principles, his past feedback and a first-use test. Anything he still flags
  is logged as an *escape* and becomes a new rule, so it can't happen twice.

## Install

Pick your tool. You only do this once.

**Claude Code**
```text
/plugin marketplace add prithvi-zeta/zero-clutter
/plugin install zero-clutter@zero-clutter
```
(Claude Code 2.1.275 or later also takes `/plugin install zero-clutter --marketplace prithvi-zeta/zero-clutter`.)

**Cursor**: install **Zero Clutter** from the plugin marketplace once it's
listed. Until then, run the script below with `--tools cursor`.

**Codex, GitHub Copilot, or no marketplace**
```bash
git clone https://github.com/prithvi-zeta/zero-clutter
python3 zero-clutter/scripts/install.py            # every tool it finds
python3 zero-clutter/scripts/install.py --tools codex,copilot
```

**Gemini CLI**
```bash
gemini extensions install https://github.com/prithvi-zeta/zero-clutter
```

**Claude.ai, ChatGPT or any chat**: upload the `skills/zero-clutter` folder
(Claude: Settings → Capabilities → Skills), or attach its `SKILL.md` and the
`references/` folder, then say "run zero clutter on this".

Restart the tool after installing.

## Set up a repo (once per project)

In the repo, ask your agent:

```text
zero-clutter setup
```

It reads the project and creates:

| File | What it's for |
| --- | --- |
| `.zero-clutter/adapter.md` | How this project produces evidence: screenshot tool, smallest screen, tests, who approves |
| `.zero-clutter/house-rules.md` | Rules learned in this project (`P-01`, `P-02`, …) |
| `.zero-clutter/feedback-log.md` | Every review comment and what it taught us |
| `.github/pull_request_template.md` | The gates and the 15 checks on every PR (only if the repo has none) |
| A section in `AGENTS.md` | Tells every agent in the repo to run Zero Clutter at each gate |

Or run `python3 zero-clutter/scripts/install.py --project path/to/repo`. Commit these files so the whole team shares them.

## Use it

| When | Say | It runs |
| --- | --- | --- |
| A ticket, doc or Loom arrives | `zero-clutter` + the link or file | **spec** (G1): every requirement numbered, conflicts with the principles, questions for the approver |
| You have a design or screenshot | `zero-clutter` + the frame | **design** (G2): Delight Police plus the house rules |
| You changed something | `zero-clutter` | **build** (G3): the 15 checks on what changed |
| Before merging | `zero-clutter pr` | **pr** (G4): every checklist item with evidence, in its own reviewer agent |
| A new flow is ready | `zero-clutter first-use` | **first-use** (G5): a step-by-step test for someone who hasn't seen it |
| Feedback comes in | `zero-clutter` + the feedback | **feedback**: logs it, finds the gate that missed it, adds a rule |

## Reading the answer

| Kind | Means | Who acts |
| --- | --- | --- |
| Fix | Problems to fix; `blocking` means it can't ship | The team |
| Decide | A spec conflict, a taste call or a missing fact | The approver |
| Suggest | An improvement nobody asked for | Optional |
| Check | Needs a device, a person or a capture | Whoever it names |
| Keep | What works; don't lose it | Everyone |

Findings are numbered in the `#` column so you can say "fix 1, decide 3".
The verdict table shows the scope as `passed/checked`. The columns follow
[Conventional Comments](https://conventionalcomments.org/) (kind and
severity on every finding) and the same findings are written as
[SARIF](https://docs.oasis-open.org/sarif/sarif/v2.1.0/sarif-v2.1.0.html) for
CI. Full rules: [report format](skills/zero-clutter/references/report-format.md).
How evidence is collected on each platform: [platforms](skills/zero-clutter/references/platforms.md).

## CI gate

`pr` mode also writes the findings as SARIF to `.zero-clutter/reports/`. Copy
[examples/ci/zero-clutter-gate.yml](examples/ci/zero-clutter-gate.yml) into a
repo's `.github/workflows/` and every PR:

- fails if UI files changed without a Zero Clutter report,
- fails on any blocking finding, with annotations on the PR,
- can show the findings in GitHub's Security tab (optional step).

Locally: `python3 skills/zero-clutter/scripts/gate.py .zero-clutter/reports/`.

## The gates

| Gate | When | Passes when |
| --- | --- | --- |
| G1 Spec | Before design | Every requirement numbered; the approver answered every blocker question |
| G2 Design | Before build | No open Zero Cognitive Load findings |
| G3 Build | Every change | The 15 checks pass |
| G4 PR | Before merge | 0 blockers; every requirement proven with a screenshot |
| G5 First use | Before sign-off | Someone new finishes it unaided |
| G6 Release | Before shipping or showing the approver | All of the above; demo and report ready |

Details: [gates](skills/zero-clutter/references/gates.md).

## What it checks against

1. **[Bhavin's principles](skills/zero-clutter/references/principles/design-for-delight-principles.md)**, word for word, in their priority order: Zero Cognitive Load (zero clutter first), Engage the Senses, Purpose-built Unique Design, and [The Science behind Delight](skills/zero-clutter/references/principles/the-science-behind-delight.md).
2. **[The checklist](skills/zero-clutter/references/checklist.md)**: 15 questions, backed by [134 items](skills/zero-clutter/references/checklist-items.md) with stable IDs.
3. **[Shared house rules](skills/zero-clutter/references/house-rules.md)**: lessons from past reviews that apply everywhere.
4. **The project's own context and rules**: `AGENTS.md`, the adapter, and `.zero-clutter/house-rules.md`.

## What it can't do

- From a still image it can't judge haptics, sound or speed; it says so and asks for a recording or a device check.
- It can't stand in for a first-use test with a real person on first-run screens; it prepares the test and marks it pending.
- It doesn't decide taste for the approver. It asks, before the build.

## Inside the repo

| Path | What |
| --- | --- |
| `skills/zero-clutter/` | The skill: `SKILL.md`, `references/` (principles, checklist, gates, house rules, report format, mode guides, templates) and `scripts/gate.py` |
| `skills/delight-police/` | Screen and Figma review, used by design mode |
| `agents/zero-clutter-reviewer.md` | Reviewer that runs the full PR review in its own context |
| `cursor/` | Cursor command and rule |
| `.claude-plugin/`, `.cursor-plugin/`, `gemini-extension.json` | Plugin manifests |
| `examples/` | A real project's feedback log, a sample SARIF report, the CI workflow |
| `scripts/` | `install.py`, and `check.py`, which CI runs |

## Change Zero Clutter

1. Edit, then bump the version in `skills/zero-clutter/SKILL.md`, both plugin manifests and `gemini-extension.json` (they must match).
2. Add a line to [CHANGELOG.md](CHANGELOG.md).
3. Run `python3 scripts/check.py`: principles in sync, every ID, rule and link resolves, versions match.
4. Open a PR. Never edit the principles' wording; a new version of Bhavin's docs replaces the files.

A project rule that would help everyone: add it to the shared house rules in a PR, with the log entry it came from.
