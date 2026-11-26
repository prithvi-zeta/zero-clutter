# Design mode (G2)

Review a screen, mock, Figma frame or screenshot against Design for Delight,
to the bar of a tough delight review, before anyone builds it. The same
review works for product managers and designers. Known fixtures and the
findings they must produce are in [design-examples](design-examples.md).

## Read first

1. `principles/design-for-delight-principles.md` and
   `principles/the-science-behind-delight.md` (word for word, in priority order).
2. `checklist.md` and `checklist-items.md`, for IDs.
3. `house-rules.md`, plus the project's own.

## Before you review

1. If the screen's job or its audience is missing, ask once for both. Don't
   ask for anything the image already shows.
2. Judge only what is visible or stated. Don't invent UI that isn't on the
   screen, and don't flag elements that aren't there.
3. From a still, say that haptics, sound and the under-100ms feedback rule
   can't be judged. Ask for a prototype or a note on interaction only if
   Instant Feedback or Engage the Senses matters to the call.

## How to review

Walk the principles in this order; the order is the priority. Be direct: if
it fails Zero Cognitive Load, say so. Run the sweeps in SKILL.md step 3 as
you go (repeats, element by element, small type, the copy read).

### 1. Zero Cognitive Load (priority order)

1. **Zero Clutter**: only what is necessary and sufficient for the outcome.
2. **Use fewer words**: one word where one word works; scan, don't read; no
   repeats (HR-17).
3. **Smart Defaults and Auto completes**: don't ask for what the product can do.
4. **Progressive Disclosure / One page, One context**: reveal complexity only as needed.
5. **Strong and Logical Visual Hierarchy**: the eye finds what matters; no
   multi-column scan traps; no small type except the terms (HR-15).
6. **Instant Feedback**: every interaction answers at once (under 100ms when measurable).
7. **Consistency**: repeat design elements and patterns.
8. **Familiar Mental Models**: map to patterns users already know.
9. **Reduce Analytical Choices**: each analytical choice costs cognitive load.

A new or returning user should need no instructions, take the right first
action by instinct, get an immediate rewarding response, feel "this makes
sense", stay out of analytic mode, and feel flow rather than effort.

### 2. Engage the Senses

Pleasing sights, sounds, haptics and micro-animations on achievement or
completion. From a still, note what can't be judged.

### 3. Purpose-built Unique Design

Only when the person says the feature is high frequency; otherwise write
"Not assessed (not marked high frequency)" and count it in N/A. A custom interaction is allowed, but it must not break Zero
Cognitive Load: it borrows a familiar mental model so it feels natural on
first use. A unique gesture that needs instructions fails.

## Answer

Zero Clutter's tables (SKILL.md step 4). In the verdict table's Subject, add
a one-line **first-use read**: would a new user act without instructions?
Craft changes (layout, words, hierarchy, motion) are `🔧 Fix` rows. Product
decisions (stop asking for a field, set a default, split one screen into one
context, remove an analytical choice) are `🤔 Decide` rows for the approver.

## Rules

1. **Principles before taste.** Never replace a principle with a preference.
2. **Zero Cognitive Load wins.** Never recommend a unique interaction that
   needs instructions or System 2.
3. **Visible evidence only.** Every finding points at something on the
   screen or something the person stated.
4. **Both audiences.** A designer and a PM should each leave with something
   they own: Fix rows for one, Decide rows for the other.
5. **No invented UI.** Don't propose elements that contradict what is shown
   without saying it's a proposal, marked `(new, needs approval)`.
