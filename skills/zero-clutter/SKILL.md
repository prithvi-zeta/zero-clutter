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
  version: "0.4.0"
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

Clean and scannable: a header, then findings grouped under four plain
headings, each finding as three short lines. Markdown, so it renders well in
Claude Code, Cursor and chat. Full rules: [report-format](references/report-format.md).

```markdown
**Zero Clutter** · <mode> (G<n>) · <what was checked>
**<VERDICT>** · <n> blocking · <n> major · <n> minor · <n> pending · <passed>/<checked> passed · <n> n/a

**Fix**
1. **<ID> <Principle>** · <blocking|major|minor>
   <what's wrong> · `<where>`
   → <the fix>

**Decide** (the approver)
2. **<ID> <Principle>** · <severity>
   <the decision to make>
   → <proposal> (recommend: <x>)

**Check**
- **<ID> <Principle>** · <what can't be judged yet> → <who or what resolves it>

**Keep** <what works, 1 to 3 things, separated by ·>

**Next** <the one thing to do now>
```

- **Headings, in this order, only when they have something:** **Fix** (the
  team fixes it: issues), **Decide** (only the approver can: spec conflicts,
  taste calls, missing facts), **Suggest** (optional improvements nobody asked
  for), **Check** (pending: a device, a person, a capture), **Keep**, **Next**.
- **Numbered findings** in Fix, Decide and Suggest, numbered across the
  headings (1, 2, 3…), so people can say "fix 1, decide 2".
- **Three lines each:** the ID, principle name and severity in bold on the
  first; what's wrong and where on the second (`file:line`, `screen › element`
  or `R#`; first two places, then `+n`); the fix after `→` on the third.
  Keep each line short; no sentence longer than it needs to be.
- **Check** items are one line each, as bullets.
- **Order:** blocking, then major, then minor; within each, principle order.
  At most 10 findings, then `+<n> more — say "details"`.
- **Verdict:** `PASS` or `FAIL` for design, build, pr and first-use (`PASS`
  only with 0 blocking and nothing pending on a blocker). For spec: `READY` or
  `OPEN`, and no passed count. Feedback mode answers with its five-line entry.
- **Nothing else:** no preamble, no praise beyond Keep, no recap of the
  principles, no tables unless asked. A clean pass is just the two header
  lines, Keep and Next.
- **Plain-text tools:** where Markdown doesn't render, use the same layout
  without the `**`.
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
