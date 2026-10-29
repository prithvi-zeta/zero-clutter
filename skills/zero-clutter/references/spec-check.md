# Spec mode (G1)

Get the approver's decisions before anyone designs, so they can't come back as
negative feedback later.

## Read first

1. `principles/design-for-delight-principles.md` and
   `principles/the-science-behind-delight.md` (word for word, in priority order).
2. `checklist-items.md`, for IDs.
3. `house-rules.md`, for what past reviews taught us.

## Steps

1. **Collect every source.** Ticket text, every linked doc, transcript or
   subtitle file, screenshots. If a PDF is image-only, render the pages and
   read them. If a link can't be opened, say so and ask for it.
2. **Number every sentence.** One row per requirement: `R1`, `R2`, … Quote
   copy word for word, including typos (flag typos as questions, don't fix
   them). Group by flow and screen. Keep where each came from (doc page,
   transcript timestamp).
3. **Map to today.** For each row: what exists now, what changes, and what's
   new. Note anything already built.
4. **Find conflicts between sources.** Doc vs transcript, old ticket vs new,
   spec vs a frozen screen. Each conflict is a question.
5. **Run the principles over the spec.** For each requirement, check the
   checklist items it touches. Anything the spec asks for that a principle
   forbids is a **SPEC-CONFLICT**: name the item, quote the principle, and
   propose an option that meets both. Common ones:
   - multi-column layouts (HIER-04)
   - more than one statement per screen (CLUT-01)
   - asking for something the product could fill in (DEF-*)
   - a choice the user has to calculate or compare (CHOICE-*)
   - a cost or delay first shown after commit (SCI-02)
6. **List taste calls.** Anything where the approver's preference decides it
   (layout options, which variant is the default). Never guess his taste; ask.
7. **Write questions for the approver.** Short, one decision each, with the
   options and your recommendation. Mark blockers (work can't start without
   the answer). Give a working assumption for each non-blocker.
8. **Save the plan** using `templates/ticket-checklist.md` (where: see below).

## The plan

Save this where the adapter says plans go, else `.zero-clutter/plans/<name>.md`.
In chat, answer in the skill's short format: spec conflicts, taste calls and
open questions as `?` lines, verdict `READY` or `OPEN`, and the plan's path
(or `… full plan: say "details"` if you can't write files).

```text
Source: <ticket / doc / Loom, links>
Requirements: R1–Rn (table: #, requirement with quoted copy, source, today, change)
Conflicts between sources: <list>
Spec conflicts (principles): <R#, item ID, principle quote, proposal>
Taste calls: <list>
Questions for the approver (blockers first): <numbered, options + recommendation>
Working assumptions: <for each non-blocker>
G1 status: OPEN until every blocker question and spec conflict is answered
```

## Rules

- Quote, don't paraphrase, when it's copy.
- Every source sentence gets a row, even ones that seem obvious.
- Never resolve a spec conflict silently in either direction.
- When the approver answers, write the answer into the plan next to the question.
  Those answers are decisions; G2 onward builds to them.
