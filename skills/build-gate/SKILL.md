---
name: build-gate
description: >-
  Zero Clutter gates G3 and G4. Check a built change (code, screenshots,
  recordings) against Bhavin's Design for Delight principles, the checklist
  and the house rules, with evidence for every result. Quick mode on every
  change before showing anyone; full mode before a PR merges. Use when
  something has been built or changed, before saying done, before opening or
  merging a PR, or when someone asks to "gate", "QA" or "delight-check" a
  build.
metadata:
  version: "0.1.0"
---

# build-gate (G3, G4)

Paths below are relative to the zero-clutter repo. In an installed copy
they are under `shared/` next to this file.

## Read first

1. `principles/` (both documents).
2. `checklist/README.md` (the 15 questions) and `checklist/items.md` (IDs).
3. `feedback-log/house-rules.md`.
4. The project's **adapter** (`zero-clutter.md` in the repo, or the file it
   points to): how each item is verified on this stack.
5. The G1 plan for this work (the R-rows and Bhavin's answers).

## Quick mode (G3, every change)

1. List what changed: screens, states, copy, motion, assets.
2. Capture evidence for each changed screen: a screenshot on the smallest and
   a large supported screen, large text, and a frame sheet for any motion.
3. Answer the 15 questions for what changed, each PASS, FAIL or N-A with a
   reason, pointing at the evidence.
4. Check every house rule that applies.
5. Fix every FAIL before showing anyone. Changes to existing UI that weren't
   asked for are proposals, not fixes.

## Full mode (G4, before merge)

1. Everything in quick mode.
2. Every in-scope item in `checklist/items.md` gets a result:
   - PASS with evidence (measured, not "looks fine")
   - FAIL with file and line, plus screenshot or frame
   - N-A with a reason
   - SPEC-CONFLICT with a proposal (don't change it)
   - PENDING-CAPTURE, PENDING-DEVICE or PENDING-HUMAN, with what's needed
3. Every R-row from the G1 plan has a screenshot proving it. Re-read the
   source line by line against them.
4. Write the report with `templates/review-report.md` and attach it to the PR.

## Report, every time

```text
Change: <what>
First-use read: <would a new user act without instructions? one or two lines>
Requirements: R1–Rn, each with its proof
Results by principle (priority order): <item, result, evidence>
House rules: <HR-xx, result>
Spec conflicts: <for Bhavin>
Designer changes: <layout, words, hierarchy, motion>
Product calls: <what to stop asking, default, or split>
Pending: <captures, device checks, people>
Gate: PASS / FAIL (0 blocker FAILs, nothing PENDING on a blocker, every R-row proven)
```

## Rules

- **Evidence or it didn't pass.** "Looks good" is a FAIL.
- **Measure.** Padding, sizes, contrast, timing and asset resolution are
  numbers; use the project's tools.
- **Stills can't prove motion, haptics or sound.** Use a recording, a frame
  sheet or a device check, or mark it PENDING.
- **Spec and frozen screens win.** A principle violation in the spec is a
  SPEC-CONFLICT for Bhavin, not a silent change.
- **No skipped items.** Every in-scope item gets a result.
