# The feedback loop

Every piece of review feedback is logged, traced to the gate that missed it,
and turned into a rule, so the gates learn it once.

## Where things live

| What | Where |
| --- | --- |
| Shared house rules (every project) | `house-rules.md` in this skill |
| A project's own log | `.zero-clutter/feedback-log.md` in that repo |
| A project's own rules | `.zero-clutter/house-rules.md` in that repo (IDs `P-01`, `P-02`, …) |
| A worked example | `examples/ryzedesign/feedback-log.md` in the zero-clutter repo |

A project rule that would help every project is promoted to the shared rules
with a PR to the zero-clutter repo.

## Sources

| Source | Who | Counts as an escape? |
| --- | --- | --- |
| **Approver** | The approver (Bhavin, unless the project names someone else), in a ticket, Loom, doc or message | Yes, if it arrives after G6 |
| **Stakeholder** | Anyone reviewing on the approver's behalf | Yes, if it arrives after G6 |
| **Design review** | A design lead or teammate before G6 | No. It's the gates working; still log it so it becomes a rule. |

## Log entry format

```
| ID | Date | Source | Feature | What was said (quoted) | Should have caught it | Root cause | Rule |
| F-001 | 2026-10-28 | Approver | Onboarding pitch | "…" | G2 | … | P-03 |
```

`F-` for the approver and stakeholders, `D-` for design review. Never delete an
entry; retire a rule with a date and the reason.
