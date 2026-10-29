# Build and PR modes (G3, G4)

## Read first

1. `principles/` (both documents).
2. `checklist.md` (the 15 questions) and `checklist-items.md` (IDs).
3. `house-rules.md`.
4. The project's `.zero-clutter/adapter.md`: how each item is verified on
   this stack, and its own house rules.
5. The G1 plan for this work (the R-rows and the approver's answers).

## Quick mode (G3, every change)

1. List what changed: screens, states, copy, motion, assets.
2. Capture evidence for each changed screen: a screenshot on the smallest and
   a large supported screen, large text, and a frame sheet for any motion.
3. Answer the 15 questions for what changed, each `pass`, `issue` or `n/a` with a
   reason, pointing at the evidence.
4. Check every house rule that applies.
5. Fix every `issue` before showing anyone. Changes to existing UI that weren't
   asked for are proposals, not fixes.

## Full mode (G4, before merge)

1. Everything in quick mode.
2. Every in-scope item in `checklist-items.md` gets a result, using the
   labels in [report-format](report-format.md):
   - `pass` with evidence (measured, not "looks fine")
   - `issue (blocking|major|minor)` with file:line or screen › element, and the fix
   - `question` for a spec conflict or a taste call, with a proposal (don't change it)
   - `pending` with what's needed (a capture, a device, a person)
   - `n/a` with a reason
3. Every R-row from the G1 plan has a screenshot proving it. Re-read the
   source line by line against them.
4. Write the report with `templates/review-report.md` and the SARIF file
   (`report-format.md`) to `.zero-clutter/reports/`, and attach the summary to the PR.

## Full report

In chat, answer in the short format from the skill (`SKILL.md`, step 4). This is
the full version: attach it to the PR, or show it when someone says "details".

```text
Change: <what>
First-use read: <would a new user act without instructions? one or two lines>
Requirements: R1–Rn, each with its proof
Results by principle (priority order): <item, result, evidence>
House rules: <HR-xx, result>
Spec conflicts: <for the approver>
Designer changes: <layout, words, hierarchy, motion>
Product calls: <what to stop asking, default, or split>
Pending: <captures, device checks, people>
Verdict: PASS / FAIL (0 blocking issues, nothing pending on a blocker, every R-row proven)
```

## Rules

- **Evidence or it didn't pass.** "Looks good" is not a `pass`.
- **Measure.** Padding, sizes, contrast, timing and asset resolution are
  numbers; use the project's tools.
- **Stills can't prove motion, haptics or sound.** Use a recording, a frame
  sheet or a device check, or mark it `pending`. A still does prove type
  size: judge HIER-11 from the screenshot.
- **Spec and frozen screens win.** A principle violation in the spec is a
  `question` for the approver, not a silent change.
- **No skipped items.** Every in-scope item gets a result.
