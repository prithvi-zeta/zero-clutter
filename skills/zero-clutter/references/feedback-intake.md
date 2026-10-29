# Feedback mode (the loop)

Every negative comment after G6 is an escape. The fix isn't done until the
gates would have caught it.

## Steps

1. **Quote it exactly.** Who, when, where (ticket, Loom timestamp, message),
   the words, and the screen or feature.
2. **Classify the source:** Approver, Stakeholder (counts as an escape after
   G6), or Design review (before G6; the gates working).
3. **Find the gate that should have caught it** and why it didn't:
   - not in the spec rows (G1: a sentence wasn't numbered),
   - a taste call nobody asked about (G1),
   - no checklist item or house rule covers it (new rule needed),
   - a rule exists but is too vague to check (sharpen it),
   - a rule exists but was skipped (process fix: which gate, who).
4. **Write or sharpen a rule** in the project's `.zero-clutter/house-rules.md`
   (next free `P-` ID): the rule, how to check it, the gate, the checklist
   items it sharpens, and the log IDs it came from. If it would help every
   project, also propose it for the shared `house-rules.md` with a PR to the
   zero-clutter repo. If no principle covers it at all, propose a new
   checklist item the same way.
5. **Add a test** where the project can: a UI or unit test, a screenshot
   check, a fixture for the reviewer.
6. **Log it** in `.zero-clutter/feedback-log.md` with the next ID (`F-`
   approver and stakeholders, `D-` design review). Create the file if it
   doesn't exist.
7. **Fix the work** and re-run the gates it touches.

## Output

One table, nothing else:

| Field | |
| --- | --- |
| Entry | F-0xx / D-0xx |
| Said | "<quote>" — <who>, <date>, <where> |
| Should have caught it | G<n>, because <root cause> |
| Rule | P-xx (new / sharpened): <rule> — check: <how> |
| Test | <what was added> |
| Fix | <what changed in the work> |

## Rules

- Never argue with the feedback in the log; record it.
- Never delete an entry or a rule; retire a rule with a date and a reason.
- Don't name people in any customer-facing artifact (demo videos, release
  notes). The log is internal.
