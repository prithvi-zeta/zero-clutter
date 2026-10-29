# Glossary

Terms the checklist items use. The project's `.zero-clutter/adapter.md` says
which tool produces each kind of evidence on its stack.

## Evidence

- **SHOT**: a screenshot of one screen in one state, at the project's usual
  phone size.
- **COMPACT**: the same screen at the smallest supported size (phones
  375×667pt, Android 360×640dp, web 320px wide and 200% zoom; see
  [platforms](platforms.md)) with the longest real values. Nothing may overflow, clip or push
  the primary action off screen.
- **FRAMES**: a recording of a motion, cut into frames (about every 33 to
  100ms) and laid out as a sheet, so timing and flashes can be seen.
- **EDGES**: measured distances from content to the screen and card edges,
  in points, from a SHOT.
- **CONTRAST**: the WCAG contrast ratio of each text run against what's
  behind it (on gradients or glass, against the lightest part behind it).
- **PRESS-TEST**: a check that a tappable shows a pressed state within one
  frame and fires its haptic.
- **LATENCY-TEST**: a check that the result of a tap is on screen within
  100ms.
- **FRESH-5S**: a first-use test with reviewers who have never seen the
  product: each sees a SHOT for 5 seconds and answers, in a few words,
  (1) what is this screen, (2) what would you do next, (3) is anything
  unclear. Write the answer key first; three reviewers; a person, not only
  an agent, for first-run screens. (Same idea as G5.)
- **States** (PROC-04): every state the screen can show: empty, typing,
  results, no results, loading, error, disabled, success, longest values,
  COMPACT, reduced motion, first run, returning, each theme, large text.

## Rules the items refer to

- **Removal test** (CLUT-01): for each element, name the question it answers
  or the action it enables. If removing it breaks nothing the user needs at
  that moment, remove it. "Context", "reassurance", "branding" and "looks
  empty" don't count.
- **Allowed reasons** (CLUT-06): a navigation aid (section headers, an A–Z
  rail, tabs, filters) needs one of: the list is long (more than about 20
  rows) and search can't replace it; the user asked for it; the platform
  requires it; or a dated list uses date headers instead of a date on every
  row. An asset needs to be the hero, a data image (logo, avatar) or a tile
  with meaning.
- **Disabled rule** (CHOICE-02): an option this user can never use is hidden;
  one they'd expect to see but can't use now is shown disabled with a 1–2 word
  reason.
- **Cost ledger** (ZCL-07, ZCL-10): per screen, count instruction strings,
  System 2 triggers, analytical choices, typed inputs, words over budget,
  taps without instant feedback, and extra steps. Every count is 0 or has an
  "irreducible because" (security, law, a spec conflict, or a fact only the
  user knows). "Fewer than before" doesn't pass on its own.
- **Completion tiers** (SENSE-02):
  - **A**, a first or a milestone (account open, first deposit, card
    activated): success haptic, sound where allowed, animated payoff.
  - **B**, a routine repeat (another transfer): success haptic and an
    animated check.
  - **C**, a toggle or an intermediate step (freeze, OTP, PIN): a light
    haptic and an in-place change, no new screen.
- **High frequency**: features people use many times a week. The project
  lists them in its adapter; for a money app the usual ones are home, send,
  request, add money, withdraw, pay and transactions. Only these get
  Purpose-built Unique Design, and money flows among them should reach
  success in 3 screens or fewer.
- **Frozen**: screens or copy signed off or handed to engineering. The
  project lists them in its adapter. They don't change unless the owner asks.
- **T0**: the moment an action really happens (after authentication returns,
  or on release of the tap or slide). No success cue before T0.
