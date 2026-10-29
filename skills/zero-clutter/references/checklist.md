# The checklist

Fifteen questions for every screen, flow and change. Answer each with what is
on the screen or in the build, not opinion. The IDs in brackets point at the
full items in [items.md](checklist-items.md); agents check those.

## Zero Cognitive Load (in Bhavin's priority order)

1. **Zero clutter.** Is every word, image and element needed to finish the task? Anything that isn't, goes. [CLUT-01–06]
2. **Fewer words.** Could any label be one word? Is anything said twice? Can it be scanned without reading? [WORD-01–06]
3. **Smart defaults.** Are we asking for anything the product already knows or could fill in? [DEF-01–09]
4. **One page, one context.** Is the screen about one thing, with extra detail revealed only when needed? [PROG-01–07]
5. **Hierarchy.** Does the eye land on the most important thing first? Is it one column, with nothing to scan across columns? [HIER-01–10]
6. **Instant feedback.** Does every tap answer at once (under 100ms) with a press state and a haptic, and never get silently ignored? [FB-01–08]
7. **Consistency.** Does it reuse the same parts and patterns as the rest of the product? Is every rate, fee, limit and time the same value everywhere? [CONS-01–08]
8. **Familiar.** Does it work the way people already expect from their phone and other apps? [MENT-01–07]
9. **Fewer choices.** Is there any moment where the user has to compare, calculate or think hard? Remove it. [CHOICE-*]
10. **First use.** Would someone new act correctly with no instructions? [ZCL-01–13]

## Engage the Senses

11. Does each completion get a haptic and a small celebration that fits its size, and is nothing celebrated before it has really happened? [SENSE-*]

## Purpose-built Unique Design (high-frequency features only)

12. Does every fresh user get the custom interaction right the first time? If not, ship the familiar control. [UNIQ-*]

## The Science behind Delight

13. Is the reward better than expected, with no cost, net amount or delay first revealed after commit, and no stress (a money failure always says where the money is and how to fix it)? [SCI-*]

## House rules

14. Is spec copy word for word, with nothing invented (no footnotes or placeholders) and nothing removed that wasn't asked for? Are the [house rules](house-rules.md) for this kind of work met? [PROC-07, PROC-08]
15. Was it checked on a small screen and at large text, and does it build with tests passing? [PROC-01, PROC-03, PROC-09]

## Results

Each item ends with one of:

- **PASS**, with evidence (screenshot, measurement, test)
- **FAIL**, with where and why
- **N-A**, with a one-line reason
- **SPEC-CONFLICT**: the spec asks for something a principle forbids. Don't change it; send it to the approver as a question with a proposal (see G1).
- **PENDING**: needs a capture, a device or a person still to come

"Looks good" is a FAIL. Done means 0 blocker FAILs, nothing PENDING on a blocker,
and every SPEC-CONFLICT answered.
