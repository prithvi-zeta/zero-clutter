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
references. Never from a blank page.
**Check:** the G2 review names the starting pattern and the references.
**Gate:** G2. **Items:** MENT-07, CONS-01. **From:** F-003.

### HR-03 · One dominant thing, big
**Rule:** Pitch, marketing and success screens have one dominant element (the
key number or statement) at headline size or larger, clearly heavier than
anything else on the screen. The number the approver calls out is the visual hero.
**Check:** in the screenshot, the hero is the largest and heaviest element
and is seen first in a 5-second look. **Gate:** G2. **Items:** HIER-01,
HIER-02, CLUT-01. **From:** F-004, F-005.

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
sides are equal. A new value needs a reason.
**Check:** measure edges in the screenshot (left = right, top and bottom as
the reference screen); compare transitions side by side with the reference.
**Gate:** G3. **Items:** CONS-01, CONS-02, HIER-05. **From:** D-004, D-005, D-006.

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
