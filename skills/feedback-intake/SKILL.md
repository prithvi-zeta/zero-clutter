---
name: feedback-intake
description: >-
  Zero Clutter feedback loop. Turn review feedback (from Bhavin, a
  stakeholder or a design review) into a log entry, a root cause, a house
  rule and a test, so the gates catch it next time. Use whenever someone
  shares feedback on built or designed work, says "Bhavin said…", pastes a
  review comment, or when a reviewer flags something the gates passed.
metadata:
  version: "0.1.0"
---

# feedback-intake

Paths below are relative to the zero-clutter repo. In an installed copy
they are under `shared/` next to this file.

Every negative comment after G6 is an escape. The fix isn't done until the
gates would have caught it.

## Steps

1. **Quote it exactly.** Who, when, where (ticket, Loom timestamp, message),
   the words, and the screen or feature.
2. **Classify the source:** Bhavin, Stakeholder (counts as an escape after
   G6), or Design review (before G6; the gates working).
3. **Find the gate that should have caught it** and why it didn't:
   - not in the spec rows (G1: a sentence wasn't numbered),
   - a taste call nobody asked about (G1),
   - no checklist item or house rule covers it (new rule needed),
   - a rule exists but is too vague to check (sharpen it),
   - a rule exists but was skipped (process fix: which gate, who).
4. **Write or sharpen a house rule** in `feedback-log/house-rules.md`: the
   rule, how to check it, the gate, the checklist items it sharpens, and the
   log IDs it came from. If no principle covers it at all, add a checklist
   item in `checklist/items.md` with the next free ID.
5. **Add a test** where the project can: a widget or UI test, a screenshot
   check, a fixture for the reviewer.
6. **Log it** in `feedback-log/log.md` with the next ID (`F-` Bhavin and
   stakeholders, `D-` design review).
7. **Fix the work** and re-run the gates it touches.
8. **Record the escape** for the release (for the scoreboard).

## Output

```text
Entry: F-0xx / D-0xx
Said: "<quote>" — <who>, <date>, <where>
Should have caught it: G<n>, because <root cause>
Rule: HR-xx (new / sharpened): <rule> — check: <how>
Test: <what was added>
Fix: <what changed in the work>
```

## Rules

- Never argue with the feedback in the log; record it.
- Never delete an entry or a rule; retire a rule with a date and a reason.
- Don't name people in any customer-facing artifact (demo videos, release
  notes). The log is internal.
