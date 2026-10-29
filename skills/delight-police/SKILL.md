---
name: delight-police
description: >-
  Delight Police: review design screens against Design for Delight principles
  (Zero Cognitive Load, Engage the Senses, Purpose-built Unique Design), in the
  spirit of a tough CRO delight review. Use when a product manager or designer
  asks to review, critique, or delight-check a screen, mock, Figma frame, or
  screenshot, or mentions delight police, cognitive load, zero clutter, or
  design for delight.
metadata:
  version: "0.1.2"
---

# Delight Police

Review a design screen against Design for Delight — same bar as a tough CRO
delight review. Same skill for product managers and designers. Read
[principles.md](principles.md) before you judge. For known fixtures and
expected findings, see [examples.md](examples.md).

## When someone starts it

Slash commands and plain words both work.

| Typed | Or said, in any wording |
| --- | --- |
| `/delight-police` | "run delight police on this", "review this screen for delight", "delight-check this mock", "critique this Figma frame for cognitive load" |

They attach a screenshot, a Figma frame, a mock, or a short description of the
screen, and say who the user is and what the screen is for.

## Before you review

1. Read [principles.md](principles.md). Judge against that wording, in its
   priority order. Do not rely on memory of another version.
2. If the job of the screen or the audience is missing, ask once for both. Do
   not ask for anything else the image already shows.
3. Judge only what is visible or stated. Do not invent UI that is not on the
   screen. Do not flag elements that are not there.
4. From a still image, say that haptics, sound, and the under-100ms feedback
   rule cannot be judged. Ask for a prototype or a short note on interaction
   only if Instant Feedback or Engage the Senses is material to the call.

## How to review

Walk the principles in this order. Stop inventing severity: priority is the
order below. Be direct: if it fails Zero Cognitive Load, say so.

### 1. Zero Cognitive Load (priority order)

1. **Zero Clutter** — only what is necessary and sufficient for the outcome
2. **Use fewer words** — one word where one word works; scan, don't read; no repeats
3. **Smart Defaults and Auto completes** — do not ask for what the product can do
4. **Progressive Disclosure / One page, One context** — reveal complexity only as needed
5. **Strong and Logical Visual Hierarchy** — eye finds what matters; avoid multi-column scan traps. On the screenshot, compare every text run to the body text on that screen (the main sentence, row title or button label). Flag a run whose letters are a distinct smaller step. The only exception is the terms and conditions. Do not skip this because a still has no font token. A lighter weight at the same size is not small type.
6. **Instant Feedback** — every interaction gives immediate, intuitive feedback (under 100ms when measurable)
7. **Consistency** — repeat design elements and patterns
8. **Familiar Mental Models** — map to patterns users already know
9. **Reduce Analytical Choices** — each analytical choice costs cognitive load

A new or returning user should not need instructions, should take the right
first action instinctively, get an immediate rewarding response, feel "this
makes sense," stay out of analytic mode, and experience flow rather than
cognition.

### 2. Engage the Senses

Pleasing sights, sounds, haptics, and micro-animations on achievement or
completion. From a still, note what cannot be judged.

### 3. Purpose-built Unique Design

Only when the person says the feature is high frequency. Custom, fit-to-purpose
interaction is allowed; it must not violate Zero Cognitive Load. Use Familiar
Mental Models so the unique design feels natural on first use and does not
require System 2. A unique gesture that needs instructions fails.

## Output, every time

Use this shape. Findings stay in principle priority order.

```text
Screen: <name or short description>
Job: <what the user is trying to achieve>
Audience: <who>

First-use read: <would a new user act without instructions? one or two lines>

Findings (by principle priority):
- <Principle>: <what is on the screen> — <why it costs effort> → <the change>

Already meets:
- <Principle>: <what to leave alone>

Designer changes:
- <layout, words, hierarchy, motion>

Product calls:
- <what the product should stop asking, default, or split into one context>
```

- Put Instant Feedback and Engage the Senses under Findings only when there is
  something to say; otherwise put them under a line: "Cannot judge from a
  still: haptics, sound, under-100ms feedback."
- Purpose-built Unique Design appears only when the person marked the feature
  high frequency; otherwise write "Not assessed (not marked high frequency)."
- Designer changes are craft: layout, copy length, hierarchy, motion.
- Product calls are product decisions: stop asking for a field, set a default,
  split one screen into one context, remove an analytical choice.

## Rules

1. **Principles before taste.** Do not replace a principle with a preference.
2. **Zero Cognitive Load wins.** Never recommend a unique interaction that
   needs instructions or System 2.
3. **Visible evidence only.** Every finding points at something on the screen
   or something the person stated.
4. **Both audiences.** Always fill Designer changes and Product calls. A
   designer and a PM should each leave with something they can own.
5. **No invented UI.** Do not propose elements that contradict what is shown
   without saying you are proposing a change.
