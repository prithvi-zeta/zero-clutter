---
name: spec-check
description: >-
  Zero Clutter gate G1. Turn a ticket, Loom transcript, doc, PDF or message
  into numbered requirements, find every place the spec breaks Bhavin's
  Design for Delight principles or a house rule, and write the questions
  Bhavin must answer before design starts. Use when new work arrives, when
  someone says "check this spec", "plan this ticket", "understand this
  Loom", or before any design or build from a stakeholder request.
metadata:
  version: "0.1.0"
---

# spec-check (G1)

Paths below are relative to the zero-clutter repo. In an installed copy
they are under `shared/` next to this file.

Get Bhavin's decisions before anyone designs, so they can't come back as
negative feedback later.

## Read first

1. `principles/design-for-delight-principles.md` and
   `principles/the-science-behind-delight.md` (word for word, in priority order).
2. `checklist/items.md`, for IDs.
3. `feedback-log/house-rules.md`, for what past reviews taught us.

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
   - more than one statement per screen (CLUT-01, house rule HR-06)
   - asking for something the product could fill in (DEF-*)
   - a choice the user has to calculate or compare (CHOICE-*)
   - a cost or delay first shown after commit (SCI-02)
6. **List taste calls.** Anything where Bhavin's preference decides it
   (layout options, which variant is the default). Never guess his taste; ask.
7. **Write questions for Bhavin.** Short, one decision each, with the
   options and your recommendation. Mark blockers (work can't start without
   the answer). Give a working assumption for each non-blocker.
8. **Save the plan.** In the project's plans folder (or the ticket), using
   `templates/ticket-checklist.md`.

## Output

```text
Source: <ticket / doc / Loom, links>
Requirements: R1–Rn (table: #, requirement with quoted copy, source, today, change)
Conflicts between sources: <list>
Spec conflicts (principles): <R#, item ID, principle quote, proposal>
Taste calls: <list>
Questions for Bhavin (blockers first): <numbered, options + recommendation>
Working assumptions: <for each non-blocker>
G1 status: OPEN until every blocker question and spec conflict is answered
```

## Rules

- Quote, don't paraphrase, when it's copy.
- Every source sentence gets a row, even ones that seem obvious.
- Never resolve a spec conflict silently in either direction.
- When Bhavin answers, write the answer into the plan next to the question.
  Those answers are decisions; G2 onward builds to them.
