# Feedback log

Every piece of review feedback lands here, so the gates learn it once and
never miss it again.

- [log.md](log.md): one entry per comment: when, who, where, what they said,
  which gate should have caught it, the root cause, and the rule it became.
- [house-rules.md](house-rules.md): the rules learned from the log. Every rule
  says how to check it and which gate runs it. Agents read this file at G2, G3
  and G4.

## Sources

| Source | Who | Counts as an escape? |
| --- | --- | --- |
| **Bhavin** | Bhavin, in a ticket, Loom, doc or message | Yes, if it arrives after G6 |
| **Stakeholder** | Anyone reviewing on Bhavin's behalf, or another approver | Yes, if it arrives after G6 |
| **Design review** | The design lead or a teammate before G6 | No. It's the gates working; still log it so it becomes a rule. |

## Adding an entry

Use the `feedback-intake` skill, or by hand:

1. Add an entry to `log.md` with the next ID (`F-` for Bhavin and stakeholders, `D-` for design review). Quote the words exactly.
2. Name the gate that should have caught it and why it didn't (no checklist item, an item too vague, an item skipped, or a taste call nobody asked about).
3. Add or sharpen a rule in `house-rules.md`, and a checklist item in `checklist/items.md` if a principle wasn't covered at all.
4. Add a test case where the project can (a widget test, a fixture, a screenshot check).
5. Fix the work and re-run the gates.

Never delete an entry. If a rule turns out wrong, mark it retired with the date and why.
