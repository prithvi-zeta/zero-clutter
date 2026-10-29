---
name: zero-clutter
description: >-
  Quality gate for anything with a UI (native iOS and Android, Flutter, web
  apps, websites): checks a spec, design, screen, change or PR against Bhavin's
  Design for Delight principles (Zero Cognitive Load, Engage the Senses,
  Purpose-built Unique Design, The Science behind Delight), the 134-item
  checklist and the house rules, and returns a short, neatly grouped list of
  what to fix, decide and keep. Use when someone says zero clutter, gate this,
  check this, review this screen or spec, is this ready, before saying done,
  before a PR merges, or when they share review feedback.
metadata:
  version: "0.4.1"
---

# Zero Clutter

One command for the whole gate. Find out what's in front of you, take the
project's context, run the right gate, and answer with a short verdict.

## 1. Take the project's context (every run)

Zero Clutter works on anything with a UI: native iOS and Android, Flutter, web
apps and websites, from code, a build, a URL, a screenshot or a Figma frame.
Find the platform and how to collect evidence in [platforms](references/platforms.md).

Read what exists, quickly; don't ask for what you can find:

- `AGENTS.md`, `CLAUDE.md`, `README.md`, `.cursor/rules/`: product, users, platform, tools.
- `.zero-clutter/adapter.md`: how this project verifies things (screenshot tool,
  test command, small-screen size, the approver). If missing, use sensible
  defaults for the stack and offer `zero-clutter setup` once at the end.
- `.zero-clutter/house-rules.md` and `.zero-clutter/feedback-log.md`: this
  project's own lessons. They count as much as the shared ones.
- The plan or ticket for this work, if there is one.

The **approver** is Bhavin unless the adapter names someone else.

## 2. Pick the mode

Pick from what the person gave you. Say which mode in the first line of the answer.

| They gave you | Mode | Gate | Read |
| --- | --- | --- | --- |
| Words saying what to build: a ticket, doc, PDF, Loom transcript, request | `spec` | G1 | [spec-check](references/spec-check.md) |
| A picture of what's designed or built: Figma frame, mock, screenshot | `design` | G2 | [delight-police](../delight-police/SKILL.md) + house rules |
| Code changes, a running build, "is this done" | `build` | G3 | [build-gate](references/build-gate.md), quick |
| A PR, "ready to merge", "full review" | `pr` | G4 | [build-gate](references/build-gate.md), full |
| A new flow to test on a person | `first-use` | G5 | [first-use](references/first-use.md) |
| Review feedback ("Bhavin said…") | `feedback` | loop | [feedback-intake](references/feedback-intake.md) |
| "Set up zero clutter here" | `setup` | — | step 5 below |

If it's unclear, pick the earliest gate that fits. Never ask more than one
question; ask only if the job of the screen or the user is unknown. Where
something can't be known from what you have (for example how it works today,
outside this repo), write "unknown" and carry on.

## 3. Judge

Always read these; the mode guide adds what else to read.

- The principles, word for word: [design-for-delight-principles](references/principles/design-for-delight-principles.md),
  [the-science-behind-delight](references/principles/the-science-behind-delight.md). Their order is the priority.
- The checks: [checklist](references/checklist.md) (15 questions) and
  [checklist-items](references/checklist-items.md) (134 items with IDs);
  terms in [glossary](references/glossary.md).
- The rules: [house-rules](references/house-rules.md), plus the project's.
- Judge only what is on screen, in the code or stated. Never invent UI.
- Measure what can be measured (padding, size, contrast, timing, asset
  resolution). From a still, say haptics, sound and speed can't be judged.
- Something the spec asks for that a principle forbids is a **spec conflict**:
  don't change it; it goes to the approver as a question with a proposal.
- Changes to existing UI that nobody asked for are suggestions, not fixes.
- A fix that needs new copy, numbers or UI is fine as a proposal: mark it
  `(new, needs approval)`. Never put invented copy into the work itself.

For a long `pr` review, hand the work to the `zero-clutter-reviewer` agent if
the tool has agents, so the main thread stays short.

## 4. Answer (short, every time)

One framed block inside a ```` ```text ```` code block: a left border, a labelled
divider per section, an emoji per section and per severity. Code blocks look
the same in every terminal, IDE and chat, and keep the alignment. Full rules
and an example: [report-format](references/report-format.md).

```text
╭─ 🧹 Zero Clutter ─────────────────────────────────────────────
│  <what was checked> · <mode> (G<n>) · <platform>
│
│  <❌ FAIL|✅ PASS|🟡 OPEN|🟢 READY>   🔴 <n> blocking   🟠 <n> major   🟡 <n> minor   ⏳ <n> to check   ✅ <p>/<c> passed
│
├─ 🔧 Fix ──────────────────────────────────────────────────────
│
│  🔴 F1  <ID> <Principle>
│         📍 <what's wrong>
│            <where: file:line or screen › element, first two, then +n>
│         ✏️  <the fix>
│
├─ 🤔 Decide · <approver> ──────────────────────────────────────
│
│  🔴 D1  <ID> <Principle>
│         📍 <the decision and why it's needed>
│         💬 <the question> · recommend: <x>
│
├─ ⏳ Check ────────────────────────────────────────────────────
│
│  •  <ID> <Principle> · <what can't be judged yet> → <who or what resolves it>
│
├─ ✅ Keep ─────────────────────────────────────────────────────
│
│  <what works, 1 to 3 things, separated by ·>
│
├─ 👉 Next ─────────────────────────────────────────────────────
│
│  <the one thing to do now, naming findings: "Fix F1, send D1">
╰───────────────────────────────────────────────────────────────
```

- **One code block, fenced as `text`,** for the whole answer. Nothing before
  or after it except, at most, one line offering setup.
- **Frame:** `╭─` opens it with the title, `├─` starts each section with its
  emoji and name, `│` runs down the left, `╰─` closes it. Dividers are about
  64 characters long. No right border (emoji and long paths would break it).
- **Sections, in this order, only when they have something:** 🔧 Fix (the
  team fixes it), 🤔 Decide (only the approver can: spec conflicts, taste
  calls, missing facts), 💡 Suggest (optional, nobody asked), ⏳ Check (a
  device, a person, a capture), ✅ Keep, 👉 Next.
- **Severity dot** on every finding and on the totals: 🔴 blocking, 🟠 major,
  🟡 minor. Numbering per section: F1, F2 · D1 · S1.
- **Each finding:** dot, number and `ID Principle` on the first line; then,
  indented, 📍 what's wrong (and the where on its own line under it, also
  indented), and ✏️ the fix (💬 the question in Decide, 💡 the idea in Suggest).
- **Line length:** wrap at about 90 characters; continue under the text it
  belongs to, never past the left border. A blank `│` line between findings
  and after each divider.
- **Order:** blocking, then major, then minor; within each, principle order.
  At most 10 findings, then `│  +<n> more · say "details"`.
- **Verdict:** ✅ PASS or ❌ FAIL for design, build, pr and first-use (PASS only
  with 0 blocking and nothing pending on a blocker). Spec: 🟢 READY or 🟡 OPEN,
  without the passed count. A clean pass is the title, verdict, Keep and Next.
  Feedback mode puts its five-line entry in the same frame.
- **Nothing else:** no preamble, no praise beyond Keep, no recap of the
  principles.
- **Files:** pr mode always writes the full report (Markdown) and a SARIF file
  to `.zero-clutter/reports/<date>-<name>.md` and `.sarif`; other modes when
  asked ("details", "sarif"). The spec plan goes where the adapter says, else
  `.zero-clutter/plans/`. If you can't write files, add under Check:
  `full report → say "details"`.

## 5. Setup (`zero-clutter setup`)

In the current repo, create if missing, never overwrite:

- `.zero-clutter/adapter.md` from [the template](references/templates/project-adapter.md),
  filled in from what you learned in step 1 (stack, screenshot and test commands,
  smallest screen, approver).
- `.zero-clutter/house-rules.md` and `.zero-clutter/feedback-log.md`, empty with headers.
- `.github/pull_request_template.md` from [the template](references/templates/pull_request_template.md),
  only if the repo has none.
- A short "Zero Clutter" section in `AGENTS.md` (create it if missing) that says
  to run `zero-clutter` at each gate.

Then list what you created in one line each.
