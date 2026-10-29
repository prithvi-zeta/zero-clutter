# Zero Clutter

One command that checks anything you design or build against Bhavin's
**Design for Delight** principles and tells you, in a few lines, what passed,
what failed and how to fix it.

Works for designers, PMs and engineers, in Claude Code, Cursor, Codex,
GitHub Copilot, Gemini CLI, or plain chat. Works in any repo: it reads the
project's own context and rules first.

```text
Zero Clutter · design (G2) · Onboarding plans screen
FAIL · 1 blocker · 2 majors · 0 minors

✗ HIER-04 Plans shown as 3 columns to scan across → one plan per card, Base | Plus | Premium switcher
✗ CLUT-01 "Benefits apply until end of next month" repeated under each plan → once, under the list
✗ WORD-05 "$250 in monthly card spends" and "$250 card spend / month" both used → one term
? HR-03 Which number leads: 4% APY or the plan name? → propose 4% at headline size

✓ 38 checks passed
Next: send the HR-03 question to the approver, then fix the 3 ✗
```

## What to expect

- **You type one thing.** `/zero-clutter`, or just "zero clutter this", "gate
  this", "is this ready?". It works out what you gave it (a spec, a design, a
  change, a PR, feedback) and runs the right gate.
- **You get a short answer.** One line per problem: the rule it breaks, what's
  wrong and where, and the fix. Questions only the approver can answer are
  marked `?`. Passes are a count. Say "details" for the full report.
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
| `skills/zero-clutter/` | The skill: `SKILL.md` plus `references/` (principles, checklist, gates, house rules, mode guides, templates) |
| `skills/delight-police/` | Screen and Figma review, used by design mode |
| `agents/zero-clutter-reviewer.md` | Reviewer that runs the full PR review in its own context |
| `cursor/` | Cursor command and rule |
| `.claude-plugin/`, `.cursor-plugin/`, `gemini-extension.json` | Plugin manifests |
| `examples/ryzedesign/` | A worked example: a real project's feedback log |
| `scripts/` | `install.py`, and `check.py`, which CI runs |

## Change Zero Clutter

1. Edit, then bump the version in `skills/zero-clutter/SKILL.md`, both plugin manifests and `gemini-extension.json` (they must match).
2. Add a line to [CHANGELOG.md](CHANGELOG.md).
3. Run `python3 scripts/check.py`: principles in sync, every ID, rule and link resolves, versions match.
4. Open a PR. Never edit the principles' wording; a new version of Bhavin's docs replaces the files.

A project rule that would help everyone: add it to the shared house rules in a PR, with the log entry it came from.
