# House rules (shared)

Lessons from review feedback that apply to every project. Each rule says how
to check it, which gate runs it, and which [checklist items](checklist-items.md)
it sharpens. `From:` names the log entries it came from; the first rules come
from the worked example in `examples/ryzedesign/feedback-log.md` in the
zero-clutter repo. A project's own rules live in its
`.zero-clutter/house-rules.md` and are checked too.

### HR-01 · Every source sentence is a numbered requirement with proof
**Rule:** Before design, turn every sentence of the ticket, Loom transcript,
doc or comment into a numbered row (R1, R2, …). Docs, videos and comments
linked from the mock file or ticket are sources too. Before done, attach a
screenshot per row and re-read the source line by line against them.
**Check:** the plan has an R-row for every source sentence, linked ones
included; the PR has a screenshot per R-row. A design review of a flow that
has a spec but no R-rows is a `⏳ Check` asking for them.
**Gate:** G1, G2, G4. **Items:** PROC-01. **From:** F-001, F-002, F-037.

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
a question, not a silent fix. A better wording is welcome, but it goes to the
approver as a question with the reason, and the spec's words stay until they
agree.
**Check:** diff every visible string against the source quote in the plan,
buttons included; a changed string with no approved question is an `issue`.
**Gate:** G1, G3, G4. **Items:** PROC-07, PROC-08. **From:** D-001, F-036.

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
compare transitions side by side with the reference. Then look at the gaps
by eye: where a heavy icon next to a light one, or a number next to an icon,
makes equal gaps look unequal (a tab bar), it's a minor `issue`; fix it
optically, not by the numbers.
**Gate:** G2, G3. **Items:** CONS-01, CONS-02, HIER-08. **From:** D-004, D-005, D-006, F-019, F-020, F-032.

### HR-08 · Sharp at every size
**Rule:** Icons and illustrations are vectors, or raster art at least the
pixel size it's shown at on the densest supported screen. Never enlarge a
smaller export.
**Check:** for each asset, source pixels ≥ shown size × device scale; zoom the
screenshot on edges. **Gate:** G3. **Items:** CONS-02. **From:** D-007.

### HR-09 · Motion you can read
**Rule:** Every state stays on screen long enough to read (about 250ms per
word, never under 500ms) before the next move, and every move is slow enough
to follow (a merge or morph you can see happen, about 1s or more). Text the
user has to read is on screen from the first frame and never animates in;
one thing moves (the hero art), not everything.
**Check:** a frame sheet at 100ms steps shows each state held and each move
visible over several frames. Text that types, fades or slides in, or more
than one element animating at once on a pitch screen, is an `issue`. From a
mock, say which elements are meant to move and flag the same.
**Gate:** G2, G3. **Items:** SENSE-*, FB-*. **From:** D-008, F-030.

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
An element goes in the Keep row only after it passes the removal test, and
after asking what about it is unintuitive and how the user will read it.
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
**Gate:** G2, G3, G4. **Items:** CLUT-01, CLUT-05, WORD-04. **From:** D-017, F-018, F-038.

### HR-18 · Icons and arrows mean what they say
**Rule:** An icon means what its label says: a shield is security, so it
never sits next to earning interest. A row, arrow, chevron or status opens
the thing it names (tapping "Card frozen" goes to freeze card; an arrow on
the balance goes to something about the balance).
**Check:** for each icon, write its usual meaning next to its label; for each
tappable, write where it goes. A mismatch is an `issue`. Across a flow, the
next screen is what the button promised: a button that says "Download Ryze"
leads to the download, not to a form. Walk every CTA to the screen after it.
**Check:** for each CTA in a flow, write what its label promises next to the
screen that follows. A screen that does something else is a blocking `issue`.
**Gate:** G2, G3. **Items:** ZCL-04, MENT-04. **From:** F-006, F-007, F-034.

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

### HR-26 · Copy is punctuated
**Rule:** Two statements are never run together. Each sentence ends with a
full stop, and two short statements in one line take a comma or a full
stop between them ("Account created, card ready").
**Check:** read every line on screen; two statements with no full stop or
comma between them is a minor `issue`, flagged in the copy read too.
**Gate:** G2, G3. **Items:** WORD-02. **From:** F-025, F-026.

### HR-27 · One theme and one art style
**Rule:** Every screen in a flow, and across the app, uses the same theme
(background and brand colour) and the same art style (for example rich 3D,
never cartoon next to it). Something that looks good on its own still fails
if it doesn't match the screens around it.
**Check:** list each screen's background colour and art style in the flow.
A screen that differs from its neighbours with no reason in the spec is a
major `issue`; a theme change waiting on a brand decision is a `⏳ Check`
naming who decides. **Gate:** G2. **Items:** CONS-01, CONS-02, SENSE-13.
**From:** F-027, F-028.

### HR-28 · A pick looks like a field
**Rule:** Something the user has to pick (amount chips, a source account)
sits in a card-like section of its own with a short label ("Amount",
"From"), set apart from the copy above, so it reads as a form and not as
more text. This is for a pick under pitch or explainer copy; a screen that
is only the pick (Withdraw, F-002) keeps no labels.
**Check:** a group of chips or options under pitch copy with no label, or
outside a card-like section, is a major `issue`.
**Gate:** G2. **Items:** HIER-06, MENT-04. **From:** F-029.

### HR-29 · Every wait is designed
**Rule:** A screen that waits on the server (account set-up, a check, a
match, a payment) has a wait state: a looping animation that holds for the
longest wait (up to about 10s), with the CTA shown the moment the check is
done. The wait is never a frozen screen or a disabled button with no
reason.
**Check:** for each step that calls the server, find its wait state. A
still mock with no wait state is a `⏳ Check`; a build that freezes or shows
the CTA before it's ready is a major `issue`.
**Gate:** G1, G2, G3. **Items:** FB-03, SCI-03. **From:** F-031.

### HR-30 · The button says what happens next
**Rule:** A CTA names what happens when it's tapped, with the place and the
person when they are known: "Link Dustin's bank account", not "Proceed".
Use the first name only. A trust line ("Secured by Plaid") doesn't replace
this; it can be the button's second line or sit just above it.
**Check:** a CTA reading "Proceed", "Continue", "Next" or "Submit" when the
next step is known is a major `issue`; a full name where the first name
fits is minor. **Gate:** G2, G3. **Items:** ZCL-04, WORD-02.
**From:** F-033.

### HR-31 · A flow keeps its story
**Rule:** A flow that starts from a promise ("$50 is waiting for you") names
it on every screen until it's kept ("Verify details to start using your
$50"). It never breaks into a generic screen (a sign-up form) that the user
can't link to why they came.
**Check:** walk the flow and write, for each screen, why the user is there
in their words. A screen that drops the promise is a `💡 Suggest`; a
generic form or step that doesn't follow from the last screen is a major
`issue`. **Gate:** G1, G2. **Items:** SCI-06, PROG-01. **From:** F-035.
