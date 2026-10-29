# The gates

Six gates from spec to release. Each has an owner, what it needs going in,
what it must produce, and what passes it. A gate that fails sends the work
back one step; it never waves it through with a note.

Why gates this early: problems found at the spec or the design cost minutes;
the same problem found by Bhavin after release costs a round trip and his
trust in the process.

## G1 Spec

**When:** a ticket, Loom, doc or message arrives, before any design.
**Owner:** the PM or whoever picks up the work. **Tool:** `spec-check`.

**In:** the source (ticket, transcript, doc, screenshots).

**Out:**
- Every sentence of the source as a numbered requirement (R1, R2, …), with
  copy in quotes word for word.
- What exists today for each, and what changes.
- **Spec conflicts:** every requirement that breaks a principle or a house
  rule, with the item ID and a proposal. Example: a three-column comparison
  breaks HIER-04 ("Do not use multiple columns that require scanning top to
  bottom and left to right"); propose a single-column alternative.
- **Questions for Bhavin:** every ambiguity, contradiction between sources,
  and taste call. Blockers marked.

**Passes when:** Bhavin has answered every blocker question and every spec
conflict, and the answers are written into the plan. His answers are
decisions, not feedback: they can't come back as negatives later.

## G2 Design

**When:** before building, on every new or changed screen.
**Owner:** the designer. **Tool:** `delight-police`, plus the
[house rules](../feedback-log/house-rules.md).

**In:** Figma frames or mocks for every state (empty, loading, error,
success, small screen, long text), and the G1 plan.

**Out:** a Delight Police review per screen (first-use read, findings,
designer changes, product calls), and 3 to 5 cited references (Mobbin or real
apps) for any new pattern.

**Passes when:** no open Zero Cognitive Load findings, every product call
answered, every R-row from G1 visible in the designs.

## G3 Build

**When:** on every change, while building.
**Owner:** the developer or agent. **Tool:** `build-gate` (quick mode), which
agents run automatically through the repo's `AGENTS.md`.

**Out:** the 15 checks answered for what changed, with screenshots on a
small and a large screen.

**Passes when:** all 15 checks pass or are N-A with a reason. Nothing is
shown to anyone before this.

## G4 PR

**When:** before merge.
**Owner:** the author, plus one reviewer. **Tool:** `build-gate` (full mode),
[PR template](../templates/pull_request_template.md), CI.

**Out:** the [review report](../templates/review-report.md) attached to the PR:
every in-scope item from [items.md](../checklist/items.md) with its result and
evidence, the R-rows from G1 with a screenshot each, and the house rules that
applied.

**Passes when:** 0 blocker FAILs, 0 major FAILs without an owner and date,
every R-row proven, CI green, one person approved.

## G5 First use

**When:** before sign-off on any new flow or first-run screen.
**Owner:** someone who hasn't seen the work. **Tool:** `first-use`,
[first-use test](../templates/first-use-test.md).

**Out:** for each step: what they thought they should do, what they expected
to happen, where they hesitated, and anything they asked.

**Passes when:** they finish the flow with no help, and every hesitation is
either fixed or written up as a question for Bhavin.

## G6 Release

**When:** before shipping, and before showing the work to Bhavin.
**Owner:** the release owner.

**Out:** a live demo (simulator, device or a short video) and a one-page
summary: what changed, the gate results, and any open taste calls written as
questions.

**Passes when:** G1 to G5 passed for everything in the release. Bhavin sees a
demo with its report, never a draft.

## After Bhavin's review

Every negative comment from Bhavin after G6 is an **escape**. Within 48 hours,
run `feedback-intake`: log it, find which gate should have caught it, add or
sharpen a house rule (and a checklist item if a principle wasn't covered),
add a test case, fix the work, and re-run the gates. Escapes per release are
tracked; the target is zero.
