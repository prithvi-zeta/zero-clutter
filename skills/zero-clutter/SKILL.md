---
name: zero-clutter
description: >-
  Quality gate for anything with a UI (native iOS and Android, Flutter, web
  apps, websites): checks a spec, design, screen, change or PR against Bhavin's
  Design for Delight principles (Zero Cognitive Load, Engage the Senses,
  Purpose-built Unique Design, The Science behind Delight), the 133-item
  checklist and the house rules, and returns short tables of what to fix,
  decide and keep. Whenever copy is on screen, it also says what a user will
  understand from reading it and gives options where the copy confuses. Use
  when someone says zero clutter, gate this, check this, review this screen
  or spec, is this ready, what will the user understand, read this copy,
  before saying done, before a PR merges, or when they share review feedback.
  Chat tables always use the scan emoji from report-format.
metadata:
  version: "0.4.9"
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

Pick from what the person gave you. Name the mode in the first table of the answer.

| They gave you | Mode | Gate | Read |
| --- | --- | --- | --- |
| Words saying what to build: a ticket, doc, PDF, Loom transcript, request | `spec` | G1 | [spec-check](references/spec-check.md) |
| A picture of what's designed or built: Figma frame, mock, screenshot | `design` | G2 | [delight-police](../delight-police/SKILL.md) + house rules |
| Code changes, a running build, "is this done" | `build` | G3 | [build-gate](references/build-gate.md), quick |
| A PR, "ready to merge", "full review" | `pr` | G4 | [build-gate](references/build-gate.md), full |
| A new flow to test on a person | `first-use` | G5 | [first-use](references/first-use.md) |
| Only copy, or "what will the user understand from this" | `copy` | G2 | HR-16 in [house-rules](references/house-rules.md) |
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
  [checklist-items](references/checklist-items.md) (133 items with IDs);
  terms in [glossary](references/glossary.md).
- The rules: [house-rules](references/house-rules.md), plus the project's.
- Judge only what is on screen, in the code or stated. Never invent UI.
- Measure what can be measured (padding, size, timing, asset resolution).
  Do not measure or flag contrast. From a still, say haptics, sound and
  speed can't be judged.
- Flag small type on a screenshot, mock or Figma frame, not only in code
  (HIER-11, HR-15). A still is enough: compare each text run to the body
  text on that screen and flag every smaller step. Do not mark it pending
  for lack of a font token. The only text allowed to be small is the terms
  and conditions.
- **Read the copy as the user (HR-16), every time copy is on screen**, in
  any mode, even when nobody asked. For each headline, helper line, CTA and
  field label that carries the screen's meaning, say how a first-time user
  will read it, not how the team means it. Read it with only what is on
  that screen: no knowledge of other flows, internal names or the plan.
  List what it says clearly and what it leaves open: is money a fee or a
  deposit, where it goes, is it one-time, why this amount or step, what
  happens next, can it be undone. Flag words that fight each other (for
  example "free" next to a charge).
- **Tag every line with a verdict**: `😕 Confusing` when it leaves open
  anything that matters to the user (a fee or a deposit, where money goes,
  a word that fights another), else `🙂 Clear`. Judge the line on what the
  user reads, not on whether the copy matches the spec. Read each line
  with the rest of the screen: a line whose subject the screen already
  gives (the $100 in the title) is not missing it, and a line that answers
  another line's question ("Spend or withdraw anytime" under a $100 ask)
  is Clear. Whether a promise is true is a `⏳ Check` row, not a
  confusion, and neither is where the line sits. Every Confusing
  line gets a `🤔 Decide` row; a Clear line's `❓ Left open` is `—`.
- **Every confusion gets options**, as a `🤔 Decide` row: two options at
  most, each a full line of copy marked `(new, needs approval)`, plus your
  pick and why. Prefer options that keep the spec's words (title, CTA) and
  add or move one line. Never change the copy in the work itself.
- **A promise in an option is a fact to confirm.** If an option claims
  something the screen can't prove ("withdraw it anytime", "no fee"), add a
  `⏳ Check` row naming who confirms it (product, the approver) before it ships.
- Something the spec asks for that a principle forbids is a **spec conflict**:
  don't change it; it goes to the approver as a question with a proposal.
- Changes to existing UI that nobody asked for are suggestions, not fixes.
- A fix that needs new copy, numbers or UI is fine as a proposal: mark it
  `(new, needs approval)`. Never put invented copy into the work itself.

For a long `pr` review, hand the work to the `zero-clutter-reviewer` agent if
the tool has agents, so the main thread stays short.

## 4. Answer (tables, every time)

Always Markdown tables. No framed block, no prose verdict, no bullets for
findings. Full rules: [report-format](references/report-format.md).

```markdown
| Gate | Subject | Verdict | Blocking | Major | Minor | Pending | Passed | N/A |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| <mode> (G<n>) | <what was checked> | <emoji VERDICT> | 🔴 <n> | 🟠 <n> | 🟡 <n> | ⏳ <n> | ✅ <passed>/<checked> | ➖ <n> |

| 📖 Copy | 🎯 Verdict | 👀 User reads it as | ✅ Clear | ❓ Left open |
| --- | --- | --- | --- | --- |
| "<the line, quoted>" | <😕 Confusing or 🙂 Clear> | <how a first-time user reads it> | <what it says clearly> | <questions it leaves, separated by ·, or —> |

| # | Kind | ID | Principle | Severity | What's wrong | Where | Fix |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 🔧 Fix | <ID> | <Principle> | 🔴 blocking | <what's wrong> | <where> | <the fix> |
| 2 | 🤔 Decide | <ID> | <Principle> | <emoji severity> | <the decision> | <where> | <proposal> (recommend: <x>) |
| | ⏳ Check | <ID> | <Principle> | ⏳ pending | <what can't be judged yet> | <where> | <who or what resolves it> |

| | |
| --- | --- |
| ✅ Keep | <what works, 1 to 3 things, separated by ·> |
| 👉 Next | <the one thing to do now> |
```

- **Tables, in this order.** The verdict table is always first. The copy
  read table next, whenever copy is on screen: one row per line that
  carries meaning (headline, helper, CTA, key label), quoted exactly, with
  its `😕 Confusing` or `🙂 Clear` verdict. The
  findings table only when there is a Fix, Decide, Suggest or Check row;
  each `😕 Confusing` line's open question becomes a `🤔 Decide` row with its options
  in Fix, as `A: "<copy>" · B: "<copy>" (new, needs approval) (recommend: A,
  <why in a few words>)`. The Keep / Next table is always last. Nothing
  before or after them except, at most, one line offering setup.
- **`copy` mode** keeps the same tables; the verdict is `🟢 READY` (nothing
  left open that matters) or `🟡 OPEN`, and Passed and N/A are `➖ —`.
- **Emoji on every label.** Chat and `gate.py` always prefix Kind, Severity,
  Verdict, Keep and Next, and the count cells, with the scan emoji in
  [report-format](references/report-format.md). SARIF stays plain (no emoji).
- **Kind** is `🔧 Fix` (the team fixes it), `🤔 Decide` (only the approver: a
  spec conflict, a taste call, a missing fact), `💡 Suggest` (optional;
  nobody asked), or `⏳ Check` (pending: a device, a person, a capture).
- **Number** Fix, Decide and Suggest down the `#` column (1, 2, 3…) so people
  can say "fix 1, decide 2". Leave `#` empty on Check rows.
- **Where** is `file:line`, `screen › element` or `R#`. First two places, then
  `+n`. One row per finding. Keep each cell to one line. Escape a literal `|`
  in a cell as `\|`.
- **Order:** Fix, then Decide, then Suggest, then Check. Within Fix, Decide
  and Suggest: blocking, then major, then minor, and within each, principle
  order. At most 10 finding rows, then one line under the table:
  `+<n> more — say "details"`.
- **Verdict:** `✅ PASS` or `❌ FAIL` for design, build, pr and first-use
  (`PASS` only with 0 blocking and nothing pending on a blocker). For spec:
  `🟢 READY` or `🟡 OPEN`, and Passed and N/A are `➖ —`. Feedback mode
  answers with the table in [feedback-intake](references/feedback-intake.md).
- **Nothing else:** no preamble, no praise beyond the Keep row, no recap of
  the principles. A clean pass is the verdict table, the copy read table
  if there is copy, and the Keep / Next table.
- **Plain-text tools:** still emit these Markdown tables.
- **Files:** pr mode always writes the full report (Markdown) and a SARIF file
  to `.zero-clutter/reports/<date>-<name>.md` and `.sarif`; other modes when
  asked ("details", "sarif"). The spec plan goes where the adapter says, else
  `.zero-clutter/plans/`. If you can't write files, add a Check row:
  `full report` → `say "details"`.

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
