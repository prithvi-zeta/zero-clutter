# House rules (shared)

Lessons from review feedback that apply to every project. Each rule says how
to check it, which gate runs it, and which [checklist items](checklist-items.md)
it sharpens. `From:` names the log entries it came from; the first rules come
from the worked example in `examples/ryzedesign/feedback-log.md` in the
zero-clutter repo. A project's own rules live in its
`.zero-clutter/house-rules.md` and are checked too.

### HR-01 · Every source sentence is a numbered requirement with proof
**Rule:** Before design, turn every sentence of the ticket, Loom transcript,
doc or comment into a numbered row (R1, R2, …). Before done, attach a
screenshot per row and re-read the source line by line against them.
**Check:** the plan has an R-row for every source sentence; the PR has a
screenshot per R-row. **Gate:** G1, G4. **Items:** PROC-01. **From:** F-001, F-002.

### HR-02 · Start from a pattern that's already approved
**Rule:** A new surface starts from the nearest design the approver has already
signed off (in this product or a sibling product), then 3 to 5 cited
references. Never from a blank page. An illustration or animation goes to the
approver with 2 or more options, not one.
**Check:** the G2 review names the starting pattern and the references; a
single illustration or animation with no alternative is a `question` asking
for options. **Gate:** G2. **Items:** MENT-07, CONS-01. **From:** F-003, F-022.

### HR-03 · One dominant thing, big
**Rule:** Pitch, marketing and success screens have one dominant element (the
key number or statement) at headline size or larger, clearly heavier than
anything else on the screen. The number the approver calls out is the visual hero.
**Check:** in the screenshot, the hero is the largest and heaviest element
and is seen first in a 5-second look. **Gate:** G2. **Items:** HIER-01,
HIER-02, CLUT-01. **From:** F-004, F-005, F-021.

### HR-04 · Spec copy is word for word
**Rule:** Copy from a ticket, doc, Loom or Figma is used exactly, including
capitals and spelling, unless the source owner changes it. Typos go to them as
a question, not a silent fix.
**Check:** diff every visible string against the source quote in the plan.
**Gate:** G3, G4. **Items:** PROC-07, PROC-08. **From:** D-001.

### HR-05 · Nothing invented
**Rule:** No invented footnotes, asterisks, disclaimers, labels, placeholder
copy or features. If something seems missing, ask.
**Check:** every visible string traces to a source or to an existing screen.
**Gate:** G3, G4. **Items:** PROC-08, CLUT-01. **From:** D-002.

### HR-06 · One thing per screen
**Rule:** A story, pitch or onboarding screen says one thing: one statement
under one visual. Supporting lines move to their own screen or go.
**Check:** count statements per screen in the screenshot; more than one is
an `issue` unless the spec asks for it (then a `question` for the approver).
**Gate:** G2. **Items:** CLUT-01, PROG-01, WORD-01. **From:** D-003.

### HR-07 · Spacing and patterns come from existing screens
**Rule:** Padding, gaps, header spacing, list rows and transitions reuse the
values and components of the nearest existing screen of the same kind. Equal
sides are equal. A new value needs a reason. The same gap (for example
between a primary and a secondary button) is the same on every screen of the
flow. Icons and chevrons sit on the middle of their line of text.
**Check:** measure edges in the screenshot (left = right, top and bottom as
the reference screen); measure each repeated gap on the screens before and
after this one; check each chevron and icon is centred on its text line;
compare transitions side by side with the reference.
**Gate:** G2, G3. **Items:** CONS-01, CONS-02, HIER-08. **From:** D-004, D-005, D-006, F-019, F-020.

### HR-08 · Sharp at every size
**Rule:** Icons and illustrations are vectors, or raster art at least the
pixel size it's shown at on the densest supported screen. Never enlarge a
smaller export.
**Check:** for each asset, source pixels ≥ shown size × device scale; zoom the
screenshot on edges. **Gate:** G3. **Items:** CONS-02. **From:** D-007.

### HR-09 · Motion you can read
**Rule:** Every state stays on screen long enough to read (about 250ms per
word, never under 500ms) before the next move, and every move is slow enough
to follow (a merge or morph you can see happen, about 1s or more).
**Check:** a frame sheet at 100ms steps shows each state held and each move
visible over several frames. **Gate:** G3. **Items:** SENSE-*, FB-*. **From:** D-008.

### HR-10 · No flashes, no hard cuts
**Rule:** Transitions are continuous: no frame where something pops, flashes,
changes colour suddenly or disappears and reappears.
**Check:** record the transition, view it in slow motion and as a frame
sheet. **Gate:** G3. **Items:** FB-*, CONS-*. **From:** D-009.

### HR-11 · Small screen and large text
**Rule:** Every screen is checked on the smallest supported phone and at a
large text size; nothing overflows, clips or overlaps.
**Check:** screenshots or tests at the small size and large text; no overflow
errors. **Gate:** G3. **Items:** PROC-03, HIER-*. **From:** D-010.

### HR-12 · Containers match their content
**Rule:** Sheets, cards and backgrounds match the screen inside them; no
stray strips of another colour at edges, behind the home indicator or around
the grab handle.
**Check:** screenshot the full sheet edge to edge. **Gate:** G3.
**Items:** CONS-02, CLUT-01. **From:** D-011.

### HR-13 · Demos only after sign-off, and checked before sending
**Rule:** Walkthrough videos and demos are made only after the work is signed
off. Voiceovers never name people. Voice matches what's on screen, with no
silent stretches, waits or flashes.
**Check:** script has no names; review the video once end to end before
sending. **Gate:** G6. **Items:** PROC-*. **From:** D-012, D-014.

### HR-14 · Handed-off screens are frozen
**Rule:** A screen handed to engineering or signed off doesn't change unless
the source owner asks. Improvements become proposals.
**Check:** the PR touches no frozen screen, or links the request.
**Gate:** G3, G4. **Items:** PROC-07. **From:** D-013.

### HR-15 · No small type except the terms
**Rule:** Text is never small. The only exception is the terms and
conditions. Labels, helper text, errors, timestamps, badges, captions,
footnotes, disclaimers, rates and fees sit at or above the small-type floor.
**Check:** on a screenshot, mock or Figma frame, with no code required.
List every text run you can see. The body is the main sentence, row title
or button label. Flag each run whose letters are a distinct smaller step
(helper, caption, timestamp, footnote, badge, disclaimer). A lighter weight
at the same size is not small. When the shot's pixel width is a known
device width, also measure pixels ÷ scale against the floor (glossary:
small type). Unknown scale does not make this pending. In code, the same
rule is the font size, text style or token. A run passes only when it is
the terms and conditions. The fix is to raise it to the floor or larger;
if it no longer fits, cut words rather than shrink the type.
**Gate:** G2, G3, G4. **Items:** HIER-11, CLUT-04. **From:** D-015.

### HR-16 · Read the copy as the user, and give options
**Rule:** Whenever copy is on screen (a screenshot, Figma frame, build or
string in a diff), say what a first-time user will understand from it, using
only what is on that screen. Name what it says clearly and what it leaves
open: fee or deposit, where money goes, one-time or recurring, why this
amount or step, what happens next. Flag words that fight each other ("free"
next to a charge). Tag each line `😕 Confusing` (it leaves open something
that matters) or `🙂 Clear`, reading each line with the rest of the screen: a
line that answers another line's question is Clear, and whether a promise
is true is a Check, not a confusion. Every open question that matters gets at most two options
of full copy, marked `(new, needs approval)`, with a pick and why; prefer
options that keep the spec's title and CTA. A promise an option makes
("withdraw anytime") is a fact for product to confirm, and a rate or APY on
screen is a fact for legal to confirm. A section or list's name fits
everything it will hold ("To do", not "Set up your account" for a list that
will grow past setup). The work's copy is not changed until the approver picks.
**Check:** the answer has a copy read table quoting every line that carries
meaning with a Confusing or Clear verdict, and a Decide row with options for
each Confusing line.
**Gate:** G1, G2, G3, G4. **Items:** WORD-02, WORD-03, ZCL-05. **From:** D-016, F-023, F-024.

### HR-17 · Any repeat is a finding, tappable or not, approved or not
**Rule:** A phrase or value shown twice on one screen state is a repeat,
wherever it sits: text, display, chip, pill, button or field. Whether the
element can be tapped doesn't matter, and neither does whether the screen
or pattern was approved before. Every repeat is looked at again; the one
allowed is the commit button restating the amount it commits (SCI-02).
An element goes in the Keep row only after it passes the removal test.
Art of an object (a card, a bank) only shows that the object exists: a card
number, an eye, a copy button or any other control on it fails the removal
test.
**Check:** list every value and phrase on the screen with each place it
appears (a big amount and a selected amount chip are two places). Any value
in two places is an `issue` under CLUT-01 / WORD-04, or CLUT-05 when both
places are controls for one outcome. Each control or data run on
illustrative art is an `issue` under CLUT-01. Fix by keeping the one that does the
job and removing the other; if the repeat is in the spec or a signed-off
screen, it's a `question` for the approver with that proposal.
**Gate:** G2, G3, G4. **Items:** CLUT-01, CLUT-05, WORD-04. **From:** D-017, F-018.

### HR-18 · Icons and arrows mean what they say
**Rule:** An icon means what its label says: a shield is security, so it
never sits next to earning interest. A row, arrow, chevron or status opens
the thing it names (tapping "Card frozen" goes to freeze card; an arrow on
the balance goes to something about the balance).
**Check:** for each icon, write its usual meaning next to its label; for each
tappable, write where it goes. A mismatch is an `issue`.
**Gate:** G2, G3. **Items:** ZCL-04, MENT-04. **From:** F-006, F-007.

### HR-19 · The main action is the bright one
**Rule:** A screen with only one action shows it as a bright primary button,
never in a secondary style. Next to Cancel, Later or Skip, the primary looks
clearly different. When the user came to do one action (they tapped Send),
that action is the highlighted one.
**Check:** in the screenshot, a lone action in a secondary style, a primary
styled like its Cancel, or an entry action that isn't the most prominent is
an `issue`. **Gate:** G2, G3. **Items:** HIER-01, ZCL-02. **From:** F-008.

### HR-20 · Data reads at a glance
**Rule:** Phone numbers follow their country's format, with the country code
apart. Account and routing numbers are grouped into short blocks. Every
place that shows an account number has the same reveal and copy controls.
A long detail page is split into titled sections, most important first (for
account details: terms with rate and fees, then account number, then
account info).
**Check:** a raw run of digits, or the same number with different controls
on two screens, is an `issue`; a detail list of more than about six rows
with no sections is a suggestion.
**Gate:** G2, G3. **Items:** MENT-03, CONS-01, PROG-01. **From:** F-009, F-010.

### HR-21 · Every combination of a feature is designed
**Rule:** When a feature depends on what the user has, every combination has
a screen. For add money or withdraw with a debit card or a bank account:
neither, debit only, bank only, both, and more than one card or account.
**Check:** list the combinations from the feature's inputs and match each to
a mock or state. Each one with no screen is `pending`, named in the Where
cell. **Gate:** G1, G2. **Items:** PROC-04. **From:** F-011.

### HR-22 · Errors wait until the user is done
**Rule:** A field shows an error only when the user leaves it or submits,
never while they are still typing.
**Check:** an error or "invalid" state shown on a field mid-typing is an
`issue`. **Gate:** G2, G3. **Items:** FB-04. **From:** F-012.

### HR-23 · Fields fill what they can
**Rule:** An email field offers to finish common domains once "@" is typed
(gmail.com first, then a .com option). Choosing "Custom" clears the preset
amount instead of keeping it. One input is finished before the next opens.
**Check:** a custom field that still holds a preset, or two inputs open at
once, is an `issue`; an email field with no domain help is a suggestion.
**Gate:** G2, G3. **Items:** DEF-02, DEF-09. **From:** F-013, F-014.

### HR-24 · Gestures don't fight scrolling
**Rule:** Checked only on a screen that supports a gesture. A swipe to
dismiss never sits on a screen that scrolls the same way; the back button
does that job.
**Check:** if the screen has a gesture in the direction it scrolls, it's an
`issue`. No gesture on the screen: `n/a`.
**Gate:** G2, G3. **Items:** MENT-02, MENT-06. **From:** F-015.

### HR-25 · Lists and endings work as people expect
**Rule:** Lists are in the order people expect: contacts A to Z, with no
group moved to the bottom. A one-off action ends where the user sees its
result (home, with the new entry), not on "do another".
**Check:** a list in any other order, or a one-off flow that ends on a
repeat prompt, is an `issue`. **Gate:** G2, G3. **Items:** DEF-03, ZCL-11. **From:** F-016, F-017.
