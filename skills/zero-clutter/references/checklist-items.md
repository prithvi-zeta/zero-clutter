# Checklist items

Every item, with a stable ID, a severity, the question to answer, and the
sentence from the principles it enforces. IDs never change or get reused, so
reports, house rules and project adapters can point at them.

This file is project-agnostic. Terms such as SHOT, COMPACT, FRESH-5S, the
removal test and completion tiers are defined in [glossary.md](glossary.md).
Each project's `.zero-clutter/adapter.md` says *how* to produce the evidence on
its stack.

Severity: **blocker** (cannot ship), **major** (fix before review), **minor**
(fix or note).

## Zero Cognitive Load: what it feels like (a to f), what it means, why

- **ZCL-01** · blocker · Can a first-time user finish the screen's primary task with no instruction text, tooltip, coachmark, tutorial or 'Tap/Swipe to...' hint on the primary path?
  - Enforces: Zero Cognitive Load > What it feels like > a. doesn't need instructions. Source: "Zero Cognitive means a user interface that does not require System 2 even when being used for the first time" + "a. doesn't need instructions,"
- **ZCL-02** · blocker · In a 5-second look, does a new user name the intended first action, and is it the single most prominent control, big enough to hit, on screen without scrolling, and not a hidden gesture?
  - Enforces: Zero Cognitive Load > What it feels like > b. performs the right first action instinctively. Source: "b. performs the right first action instinctively,"
- **ZCL-03** · major · Does the screen's first action produce the screen's own outcome (the keypad's outcome is the amount shown; a contact row's outcome is the next step opening) within 100ms, with no sheet, dialog, upsell or extra route in between?
  - Enforces: Zero Cognitive Load > What it feels like > c. gets an immediate, rewarding response. Source: "c. gets an immediate, rewarding response,"
- **ZCL-04** · major · For every tappable, does what happens match what a first-time user predicts from its label and look?
  - Enforces: Zero Cognitive Load > What it feels like > d. feels "this makes sense". Source: "d. feels \"this makes sense,\" and"
- **ZCL-05** · blocker · Is the screen free of all nine System 2 triggers: (1) mental arithmetic, (2) recalling a value from an earlier screen, (3) comparing more than 2 attributes across options, (4) decoding a term on the WORD-05 list or one a FRESH-5S Q3 answer asked about, (5) more than 1 sentence or more than 2 rendered lines of body text above the decision control, (6) a negation or double negative in a label, toggle or option, (7) not being able to tell whether the last action worked or what state something is in, (8) hunting for a target in an unordered or dense area, (9) fetching information from outside the app that the app could supply?
  - Enforces: Zero Cognitive Load > What it feels like > e. never switches into analytic mode (System 2 triggers). Source: "e. never switches into analytic mode." + "Zero Cognitive means a user interface that does not require System 2"
- **ZCL-06** · major · Does the flow run from first tap to success with no stretch over 1s without visible progress, no system-triggered overlay, and no lost input on back?
  - Enforces: Zero Cognitive Load > What it feels like > f. experiences flow and not cognition. Source: "f. experiences flow and not cognition"
- **ZCL-07** · major · Is every unit of the flow's interaction cost (screens, taps, typed characters, analytical choices, waits) at its floor per the ZCL-10 ledger, with high-frequency money flows reaching success in 3 screens or fewer?
  - Enforces: Zero Cognitive Load > Why 1. Feels "Effortless" (interaction cost). Source: "Why 1. Feels \"Effortless\""
- **ZCL-08** · major · Is every high-frequency task reachable from a stable spot on Home, with the repeat path (same person, same source) no longer than the first-time path?
  - Enforces: Zero Cognitive Load > Why 2. Habit forming. Source: "2. Habit forming"
- **ZCL-09** · major · Does every funnel step, web funnel page and flow log a reachable view and outcome event carrying the final state, so drop-off and the effect of each change can be measured?
  - Enforces: Zero Cognitive Load > Why 3. Higher Funnel conversion (measurement). Source: "3. Higher Funnel conversion"
- **ZCL-10** · blocker · Is every remaining unit of cognitive cost on the screen zero, or named as irreducible, rather than merely lower than before?
  - Enforces: Zero Cognitive Load > What it means 1 (zero, not minimized). Source: "Design interfaces that dont just minimize cognitive load but rather represent Zero Cognitive load"
- **ZCL-11** · major · Does a returning user get straight back to their task: one-time content never shows twice, interrupted flows resume with their input, and the app opens to the balance with no teaching or marketing pause?
  - Enforces: Zero Cognitive Load > What it feels like to a returning user. Source: "3. What it feels like to a new or returning user"
- **ZCL-12** · major · Does every tappable have a hit area of at least 49x49 canvas pt with at least 8pt to its neighbours, and can every high-frequency task be done one-handed with the thumb?
  - Enforces: Zero Cognitive Load > Why 1. Feels "Effortless" (physical effort) + Purpose-built How a.i ('with just one finger'). Source: "Why 1. Feels \"Effortless\"" + "allowing users to navigate long playlists efficiently with just one finger"
- **ZCL-13** · major · Must every funnel step (in-app onboarding and the web funnels) happen before the user's first value moment, with everything that can wait moved after account open or first deposit?
  - Enforces: Zero Cognitive Load > Why 3. Higher Funnel conversion (nothing before first value that could come after). Source: "3. Higher Funnel conversion"

## ZCL principle 1: Zero Clutter

- **CLUT-01** · major · Does every element on the screen, including below the fold, inside scrolled or collapsed regions and in every PROC-04 state (text run, icon, image, badge, divider, control, footnote), pass the removal test?
  - Enforces: Zero Cognitive Load > 1. Zero Clutter (necessary: no more). Source: "a. Each screen contains exactly and only the elements (words, images, assets) that are both necessary and sufficient to achieve the outcome. No more, no less"
- **CLUT-02** · blocker · Is every fact the user needs for this screen's decision on this screen, so they never guess, go back or remember?
  - Enforces: Zero Cognitive Load > 1. Zero Clutter (sufficient: no less). Source: "...that are both necessary and sufficient to achieve the outcome. No more, no less"
- **CLUT-03** · major · Does every row, pill and chip fit the budget: a title plus at most one secondary line, at most 2 facts on that line, the right token count per pill class, and every option's facts in fixed slots?
  - Enforces: Zero Cognitive Load > 1. Zero Clutter + 2b. Design for Scanning (row and pill budget). Source: "exactly and only the elements ... necessary and sufficient" + "b. Design for Scanning, Not Reading."
- **CLUT-04** · major · After 'cramped', 'busy' or 'cluttered' feedback, does the next version remove or move content rather than shrink type, padding or line height?
  - Enforces: Zero Cognitive Load > 1. Zero Clutter (fix discipline). Source: "No more, no less"
- **CLUT-05** · major · Does each outcome on the screen have exactly one visible control?
  - Enforces: Zero Cognitive Load > 1. Zero Clutter + 2c. Don't repeat (controls). Source: "exactly and only the elements" + "c. Don't repeat"
- **CLUT-06** · minor · Does every navigation aid and every asset have one of the allowed reasons?
  - Enforces: Zero Cognitive Load > 1. Zero Clutter (chrome, navigation aids, assets). Source: "...exactly and only the elements (words, images, assets)..."

## ZCL principle 2: Use fewer words

- **WORD-01** · major · Is every new or changed string the shortest version that passes the WORD-02 read-alone test, within the word budget for its role, with no filler words?
  - Enforces: Zero Cognitive Load > 2. Use fewer words > a. one word over two (word budget). Source: "a. If you can communicate something in one word, don't use two. Every extra word competes for attention."
- **WORD-02** · major · Read on its own, does every money, status and commit label say what it refers to, with money labels carrying their noun and commit labels naming the action?
  - Enforces: Zero Cognitive Load > 2. Use fewer words > a., bounded by clarity (read-alone test). Source: "a. If you can communicate something in one word, don't use two."
- **WORD-03** · major · Reading only the scan layer (large or bold text, numbers, icons, the CTA), can a reviewer say what the screen is for, the key value and what to do, and does every line lead with its key word?
  - Enforces: Zero Cognitive Load > 2. Use fewer words > b. Design for Scanning, Not Reading. Source: "b. Design for Scanning, Not Reading."
- **WORD-04** · major · Within each screen state, is every non-interactive phrase said once, with no content word echoed between a title and its subtitle, a row title and its secondary line, or a claim and its demo?
  - Enforces: Zero Cognitive Load > 2. Use fewer words > c. Don't repeat (within a screen). Source: "c. Don't repeat"
- **WORD-05** · minor · Is every term the everyday word your users use, with no internal terms or abbreviations to decode, and one term per concept across every platform (app, native, web)?
  - Enforces: Zero Cognitive Load > 2. Use fewer words + 8. Familiar Mental Models (the user's vocabulary). Source: "Every extra word competes for attention." + "a. Map interactions to patterns users already know."
- **WORD-06** · major · Is each claim, explanation or confirmation said once per flow and once per event: no sentence or claim restated on a later step or story, no toast repeating a change already visible in place, and no push, inbox row and toast all announcing one event while the user is looking?
  - Enforces: Zero Cognitive Load > 2. Use fewer words > c. Don't repeat (across a flow and across channels). Source: "c. Don't repeat"

## ZCL principle 3: Smart Defaults and Auto completes

- **DEF-01** · major · For every input and manual step, has the system first used what it already knows (profile, bank link, contacts, device, last use, previous step, location lookup), so it never asks for something it could fill itself?
  - Enforces: Zero Cognitive Load > 3. Smart Defaults and Auto completes (input inventory). Source: "a. Do not ask users to input information or perform actions that you can perform automatically"
- **DEF-02** · major · Does every choice open with the most likely safe option selected, so the happy path finishes without opening a picker and never defaults the user into a fee?
  - Enforces: Zero Cognitive Load > 3. Smart Defaults (preselection). Source: "a. Do not ask users to input information or perform actions that you can perform automatically"
- **DEF-03** · minor · Is every pick-list ordered with the most likely choice first (recent or frequent, then A-Z), in one flat list with search?
  - Enforces: Zero Cognitive Load > 3. Smart Defaults (order by predicted intent). Source: "a. Do not ask users to input information or perform actions that you can perform automatically"
- **DEF-04** · major · Do fixed-length inputs (OTP, PIN, SSN last 4, CVC) submit themselves when complete, while open-ended inputs (amounts, names, notes) wait for an explicit action?
  - Enforces: Zero Cognitive Load > 3. Auto completes (fixed-length codes). Source: "a. Do not ask users to input information or perform actions that you can perform automatically"
- **DEF-05** · major · Does every text field, on every platform, declare the right keyboard and, where the OS has one, an autofill content type, with paste never blocked?
  - Enforces: Zero Cognitive Load > 3. Auto completes (OS autofill and keyboards). Source: "a. Do not ask users to input information or perform actions that you can perform automatically"
- **DEF-06** · blocker · Does every as-you-type formatter insert only separators, stay lossless when the inferred type switches, apply length caps only once the type is certain, and keep the caret, including a custom-drawn one, where the next typed character will appear?
  - Enforces: Zero Cognitive Load > 3. Auto completes must be safe (separators only, lossless, caret stays put). Source: "a. Do not ask users to input information or perform actions that you can perform automatically"
- **DEF-07** · major · Do retry, 'Send again', 'Request again' and recovery paths open with the person, amount and source already filled, from the user's own source, without ever committing on their own?
  - Enforces: Zero Cognitive Load > 3. Smart Defaults (repeat and retry carry context). Source: "a. Do not ask users to input information or perform actions that you can perform automatically"
- **DEF-08** · major · Does the app take every action it can on the user's behalf: focus the first empty field with the right keyboard, advance on a single-select pick, select a just-added account, fill derived fields, and retry a transient failure once?
  - Enforces: Zero Cognitive Load > 3. Smart Defaults ('...or perform actions that you can perform automatically'). Source: "a. Do not ask users to input information or perform actions that you can perform automatically"
- **DEF-09** · major · Does every free-text field with a known domain (contact, address, bank, employer, merchant, ZIP) suggest matches as the user types, and does picking one fill every field it determines?
  - Enforces: Zero Cognitive Load > 3. Auto completes (known domains). Source: "3. Smart Defaults and Auto completes" + "a. Do not ask users to input information or perform actions that you can perform automatically"

## ZCL principle 4: Progressive Disclosure / One page, One context

- **PROG-01** · major · Can the screen's purpose be written as 'This screen lets you ___' in 5 words or fewer, without 'and', with nothing on it serving another goal, in the correct product shell?
  - Enforces: Zero Cognitive Load > 4. Progressive Disclosure / One page, One context (one goal). Source: "4. Progressive Disclosure / One page, One context"
- **PROG-02** · major · Are secondary details at most one labelled tap away, while every decision fact stays visible without scrolling or tapping?
  - Enforces: Zero Cognitive Load > 4. Progressive Disclosure > a. Reveal complexity only as needed. Source: "a. Reveal complexity only as needed"
- **PROG-03** · major · Does every hidden layer (card details, more options, collapsed content, gesture reveal) have a visible cue or a visible control that reaches the same content?
  - Enforces: Zero Cognitive Load > 4. Progressive Disclosure needs a visible cue. Source: "a. Reveal complexity only as needed" + "a. doesn't need instructions,"
- **PROG-04** · major · Does every footnote, qualifier or annotation, and every paired element, become visible on the same beat as the thing it qualifies or pairs with, never before it?
  - Enforces: Zero Cognitive Load > 4. Progressive Disclosure in time (annotations arrive with their referent). Source: "a. Reveal complexity only as needed"
- **PROG-05** · minor · Is at most one sheet, dialog or toast layer open at a time, with no sheet opening another sheet, dialog or toast on top of itself?
  - Enforces: Zero Cognitive Load > 4. One page, One context (one modal layer). Source: "4. Progressive Disclosure / One page, One context"
- **PROG-06** · major · On a review or confirm screen, can every choice shown be changed right there, with the same picker and the same option list that set it?
  - Enforces: Zero Cognitive Load > 4. One page, One context (edit in place on review). Source: "4. Progressive Disclosure / One page, One context" + "a. Do not ask users to input information or perform actions that you can perform automatically"
- **PROG-07** · major · When a flow leaves the app or the main view (bank-link browser, OS Settings, Wallet sheet, native system sheet, email or SMS for a code, web-to-app handoff), does the user come back to the exact step with input kept and the result applied?
  - Enforces: Zero Cognitive Load > 4. One page, One context (leaving and returning). Source: "4. Progressive Disclosure / One page, One context" + "f. experiences flow and not cognition"

## ZCL principle 5: Strong and Logical Visual Hierarchy

- **HIER-01** · major · Does the screen name its single most important fact (a value or state, not a label), set it in a hero token, and do fresh reviewers rank it and the primary action as the two most salient areas?
  - Enforces: Zero Cognitive Load > 5. Strong and Logical Visual Hierarchy (declared hero fact). Source: "Let the eye naturally find what's important"
- **HIER-02** · major · Is emphasis only where the screen means it: no sibling tile, icon, banner or colour stands out unless it is the hero fact or a real state?
  - Enforces: Zero Cognitive Load > 5. Visual Hierarchy (no accidental emphasis). Source: "Let the eye naturally find what's important"
- **HIER-03** · minor · Does the screen's content text use at most 4 distinct (size, weight) pairs from tokens, with the hero fact the largest and the title the heaviest of the remaining text?
  - Enforces: Zero Cognitive Load > 5. Visual Hierarchy through font weight (type budget). Source: "a. Use font weight, contrast, indentation as required to creating a logical visual hierarchy."
- **HIER-04** · major · Does the content read as one vertical column, with no grid, no side-by-side blocks of independent content and no horizontal scroller that makes the eye zig-zag?
  - Enforces: Zero Cognitive Load > 5. Visual Hierarchy > b. no multi-column scanning. Source: "b. Do not use multiple columns that require scanning top to bottom and left to right."
- **HIER-06** · major · Does every fact sit in a named slot of its component's anatomy (title, secondary line, inside a pill, value column, caption under the amount), with no loose text beside a pill, badge or icon, groups set by spacing, one weight per chip or line and separators in the secondary colour?
  - Enforces: Zero Cognitive Load > 5. Visual Hierarchy + 2b. Scanning (grouping and slots). Source: "Let the eye naturally find what's important" + "b. Design for Scanning, Not Reading."
- **HIER-07** · minor · Does the top-to-bottom order follow the order the user decides (what, how much, from/to, when/cost, act), with the action after every fact it commits to?
  - Enforces: Zero Cognitive Load > 5. Visual Hierarchy (reading order follows decision order). Source: "Let the eye naturally find what's important"
- **HIER-08** · major · Do shared edges agree within 1pt and is padding inside every card even, in every state?
  - Enforces: Zero Cognitive Load > 5. Visual Hierarchy through indentation + 7. Consistency (alignment and padding). Source: "a. Use font weight, contrast, indentation as required to creating a logical visual hierarchy." + "a. Repeat design elements and patterns"
- **HIER-09** · major · Does indentation express hierarchy and only hierarchy: content text starts on the column's leading edge, subordinate content sits one fixed step in from its parent, and centred text appears only on the allowlist?
  - Enforces: Zero Cognitive Load > 5. Visual Hierarchy through indentation (levels and one reading edge). Source: "a. Use font weight, contrast, indentation as required to creating a logical visual hierarchy."
- **HIER-11** · major · On the SHOT as well as in code, is every text run at or above the small-type floor, with the terms and conditions as the only text allowed to be small?
  - Enforces: Zero Cognitive Load > 5. Visual Hierarchy (no fine print except the terms). Source: "a. Use font weight, contrast, indentation as required to creating a logical visual hierarchy." + "Let the eye naturally find what's important"

## ZCL principle 6: Instant Feedback

- **FB-01** · blocker · Does every tappable show a visual press state on touch-down and fire exactly one light or selection haptic, and does no control silently ignore a tap?
  - Enforces: Zero Cognitive Load > 6. Instant Feedback (touch-down press state on every tappable). Source: "a. Every user interaction must give an immediate and intuitive feedback within under 100ms"
- **FB-02** · major · Does the first visible change after every interaction happen within 100ms, with nothing awaited before it and no commit cue fired before auth?
  - Enforces: Zero Cognitive Load > 6. Instant Feedback within 100ms (nothing awaited first). Source: "a. Every user interaction must give an immediate and intuitive feedback within under 100ms"
- **FB-03** · major · Does every action that waits acknowledge within 100ms, block a second submit, show a loader only for waits that need one, label long waits, and never wait just to look busy?
  - Enforces: Zero Cognitive Load > 6. Instant Feedback for async work (honest waits). Source: "a. Every user interaction must give an immediate and intuitive feedback within under 100ms"
- **FB-04** · major · Is every invalid input rejected at the field at the right moment, with a caption, a shake and the error haptic, never silently?
  - Enforces: Zero Cognitive Load > 6. Instant, intuitive feedback on errors. Source: "a. Every user interaction must give an immediate and intuitive feedback within under 100ms"
- **FB-05** · major · Do drags track the finger on every frame, do holds react on touch-down, and does a blocked tap still answer?
  - Enforces: Zero Cognitive Load > 6. Instant Feedback for drags and holds. Source: "a. Every user interaction must give an immediate and intuitive feedback within under 100ms"
- **FB-06** · minor · Does the main feedback appear on or next to the touched element, do toggles show the new state on the next frame and roll back visibly on failure, and are toasts used only when nothing can change in place?
  - Enforces: Zero Cognitive Load > 6. Intuitive feedback where the user is looking. Source: "a. Every user interaction must give an immediate and intuitive feedback within under 100ms"
- **FB-07** · major · Are success, error, loading, auto-submit and story changes announced to screen readers, and does anything that advances on its own stop while a screen reader runs?
  - Enforces: Zero Cognitive Load > 6. Instant Feedback for every user (screen readers). Source: "a. Every user interaction must give an immediate and intuitive feedback within under 100ms"
- **FB-08** · major · Do native platform sheets and controls give a press highlight and the same haptic class as their cross-platform twins, with platform branching kept inside platform services and every platform gap listed?
  - Enforces: Zero Cognitive Load > 6. Instant Feedback + 7. Consistency (native twins). Source: "a. Every user interaction must give an immediate and intuitive feedback within under 100ms" + "a. Repeat design elements and patterns"

## ZCL principle 7: Consistency

- **CONS-01** · major · Does an element that already exists in the app, in the design system, or as a native or web twin reuse that component (or a documented mirror whose rendered size matches) instead of a new look-alike?
  - Enforces: Zero Cognitive Load > 7. Consistency (reuse and twins). Source: "a. Repeat design elements and patterns"
- **CONS-02** · major · Do sibling elements share one pattern: every row in a card uses one row component and one alignment rule, and sibling display titles break the same way, set on purpose?
  - Enforces: Zero Cognitive Load > 7. Consistency (siblings share one pattern). Source: "a. Repeat design elements and patterns"
- **CONS-03** · major · Does every element and fact shown on two consecutive screens keep its form, size and wording, either staying in place or flying as a Hero, with nothing the user didn't change moving on Next?
  - Enforces: Zero Cognitive Load > 7. Consistency across consecutive screens (object permanence). Source: "a. Repeat design elements and patterns" + "f. experiences flow and not cognition"
- **CONS-04** · major · Does each task class use one interaction pattern app-wide: one money commit control, one auth order, one primary CTA position, one back and dismiss behaviour?
  - Enforces: Zero Cognitive Load > 7. Consistency of interaction patterns. Source: "a. Repeat design elements and patterns"
- **CONS-05** · major · Does each event class always produce the same haptic, sound and animation, only through the product's shared haptics and sound services, with completions reusing one shared success implementation and significance changing only by SENSE-02 tier?
  - Enforces: Zero Cognitive Load > 7. Consistency of sensory vocabulary (central API, shared success moment). Source: "a. Repeat design elements and patterns" + "a. Build in haptics and pleasing sounds on relevant events / completion of relevant actions"
- **CONS-06** · major · Do the logo, back button, title edge and top inset match the product's main screen within 1pt, with the logo rendered from the brand's logo asset?
  - Enforces: Zero Cognitive Load > 7. Consistency of chrome and brand lockup. Source: "a. Repeat design elements and patterns"
- **CONS-07** · blocker · Does every fact (rate, fee, limit, arrival time, speed label) and every term have one value and one wording on every surface, taken from one constant?
  - Enforces: Zero Cognitive Load > 7. Consistency of facts and copy (trust). Source: "a. Repeat design elements and patterns"
- **CONS-08** · major · Do product meanings use product tiles, chrome uses one glyph library and stroke per surface, and does each glyph mean one thing that matches its label?
  - Enforces: Zero Cognitive Load > 7. Consistency of icon language. Source: "a. Repeat design elements and patterns"

## ZCL principle 8: Familiar Mental Models

- **MENT-01** · major · Does every non-standard interaction and gesture name a precedent users actually know, showing the same gesture with the same outcome?
  - Enforces: Zero Cognitive Load > 8. Familiar Mental Models (named precedent). Source: "a. Map interactions to patterns users already know."
- **MENT-02** · major · Does every gesture mean what it means on the platform (tap acts or advances, hold pauses or shows more, swipe goes next or dismisses, edge swipe goes back, pull refreshes or reveals, row swipe-left is destructive or archive), with a test per gesture class?
  - Enforces: Zero Cognitive Load > 8. Familiar Mental Models (gestures keep their platform meaning). Source: "a. Map interactions to patterns users already know."
- **MENT-03** · major · Is every formatted value in its native form for the user's locale, produced by one shared formatter per type?
  - Enforces: Zero Cognitive Load > 8. Familiar Mental Models (native formats). Source: "a. Map interactions to patterns users already know."
- **MENT-04** · major · Does everything interactive look interactive, and everything static look static?
  - Enforces: Zero Cognitive Load > 8. Familiar Mental Models (signifiers). Source: "a. Map interactions to patterns users already know."
- **MENT-05** · major · Does every selected item render as the canonical list row, does every picker show its options exactly as they look once picked, and does the selection mark sit in one fixed leading slot?
  - Enforces: Zero Cognitive Load > 8. Familiar Mental Models + 7. Consistency (picker anatomy). Source: "a. Map interactions to patterns users already know." + "a. Repeat design elements and patterns"
- **MENT-06** · blocker · Are existing visible affordances kept unless the user asked or approved their removal, with gestures added on top and never in their place, and do back, close and dismiss behave as on iOS?
  - Enforces: Zero Cognitive Load > 8. Familiar Mental Models (keep known affordances; standard back and dismiss). Source: "a. Map interactions to patterns users already know." + "b. performs the right first action instinctively,"
- **MENT-07** · major · Did the new surface start from the nearest existing product pattern or 3-5 cited references, with 1-2 options shown to the user before code, and for a high-frequency feature at least one purpose-built option beside the conventional one?
  - Enforces: Zero Cognitive Load > 8. Familiar Mental Models (start from the nearest known pattern). Source: "a. Map interactions to patterns users already know." + "a. Repeat design elements and patterns"

## ZCL principle 9: Reduce Analytical Choices

- **CHOICE-01** · major · Does each screen ask for at most one analytical choice, at the step where it is needed?
  - Enforces: Zero Cognitive Load > 9. Reduce Analytical Choices (count). Source: "a. Each time a user has to make an analytical choice it requires a cognitive load"
- **CHOICE-02** · major · When a choice is needed, is one option preselected, do options compare on at most 2 attributes in fixed slots, are computed values shown, and are unavailable options handled per the disabled rule?
  - Enforces: Zero Cognitive Load > 9. Reduce Analytical Choices (keep options comparable). Source: "a. Each time a user has to make an analytical choice it requires a cognitive load"
- **CHOICE-03** · minor · Does every decision show at most 4 options at once?
  - Enforces: Zero Cognitive Load > 9. Reduce Analytical Choices (option count). Source: "a. Each time a user has to make an analytical choice it requires a cognitive load"
- **CHOICE-04** · major · Do reversible actions run at once with undo or a reversible state, leaving confirm dialogs for irreversible actions only?
  - Enforces: Zero Cognitive Load > 9. Reduce Analytical Choices (undo instead of 'Are you sure?'). Source: "a. Each time a user has to make an analytical choice it requires a cognitive load"
- **CHOICE-05** · minor · Can every dialog be answered from its buttons alone, with verb labels that name the outcome, the safe option primary and the downside stated plainly?
  - Enforces: Zero Cognitive Load > 9. Reduce Analytical Choices (dialogs answer themselves). Source: "a. Each time a user has to make an analytical choice it requires a cognitive load"
- **CHOICE-06** · minor · Is every permission request, upsell and optional setup asked on the first screen where its feature is used, with a one-tap skip that triggers no second decision?
  - Enforces: Zero Cognitive Load > 9. Reduce Analytical Choices (when to ask). Source: "a. Each time a user has to make an analytical choice it requires a cognitive load"

## Engage the Senses

- **SENSE-01** · major · Is every event in the change classified and mapped to its haptic, sound, animation and reduced-motion fallback in a sensory coverage table?
  - Enforces: Engage the Senses > How a + b (sensory coverage table). Source: "a. Build in haptics and pleasing sounds on relevant events / completion of relevant actions" + "b. Add delightful micro animations when the user achieves, accomplishes, completes a task, milestone, activity"
- **SENSE-02** · blocker · Does every completion get the payoff its tier requires, after the action has truly succeeded?
  - Enforces: Engage the Senses > How a + b (tiered payoff on completions). Source: "a. Build in haptics and pleasing sounds on relevant events / completion of relevant actions" + "b. Add delightful micro animations when the user achieves, accomplishes, completes a task, milestone, activity"
- **SENSE-03** · major · Do tap, tick, success, warning and error each feel physically different, using the platform's own patterns, with no celebration cue on a failure?
  - Enforces: Engage the Senses (signals the user can tell apart). Source: "a. Build in haptics and pleasing sounds on relevant events / completion of relevant actions" + Science 8: "Stress and Negative Emotions: These can inhibit the reward system"
- **SENSE-04** · minor · Does every flow stay inside the haptic budget: one haptic per input, none on passive events, strong signals only at commit, completion, error or threshold, never stacked?
  - Enforces: Engage the Senses on relevant events only (haptic budget). Source: "a. Build in haptics and pleasing sounds on relevant events / completion of relevant actions"
- **SENSE-05** · major · Does each haptic and sound fire on the frame of the visual beat it marks, driven by the value that drives that visual, once, and only after the action has succeeded?
  - Enforces: Engage the Senses in sync with the event and after it succeeds. Source: "a. Build in haptics and pleasing sounds on relevant events / completion of relevant actions"
- **SENSE-06** · major · Do sounds play only on positive completions the user triggered, or on a positive relevant event they are watching in the foreground (SENSE-14), through the shared sound service on a path that mixes with other audio and honours silent mode?
  - Enforces: Engage the Senses > pleasing sounds (sound system). Source: "a. Build in haptics and pleasing sounds on relevant events / completion of relevant actions" + Science 5: "Delight can also be triggered by sensory inputs such as sights, sounds, or other sensory experiences that are processed as exceptionally pleasing."
- **SENSE-07** · major · Does each achievement show a micro animation on the achieved object itself (check, amount, card, row), starting quickly, lasting 300-1500ms and ending still and readable, on the screen the flow already lands on?
  - Enforces: Engage the Senses > micro animations on achievement. Source: "b. Add delightful micro animations when the user achieves, accomplishes, completes a task, milestone, activity"
- **SENSE-08** · major · Does every multi-element choreography have a beat sheet that matches the code, with dependents driven by the parent's controller and no dead stretch over 300ms inside a celebration?
  - Enforces: Engage the Senses > micro animations (choreography beat sheet). Source: "b. Add delightful micro animations when the user achieves, accomplishes, completes a task, milestone, activity"
- **SENSE-09** · major · With motion on, is every frame of every animation a valid composition: no pop, flash, hard cut, one-frame colour switch, double fade, clip reveal, layout jump or lingering part?
  - Enforces: Engage the Senses > exceptionally pleasing sights (no glitches). Source: "a. Exceptionally pleasing sensory inputs such as sights and sounds trigger dopamine release" + Science 8: "Stress and Negative Emotions: These can inhibit the reward system"
- **SENSE-10** · major · With reduced motion on, do celebrations, transitions, loops, parallax, gyro, particles, large travel and count-ups jump to their end state (or crossfade 200ms or less), does auto-advancing content stop, and do functional micro-feedback and the payoff cues remain?
  - Enforces: Engage the Senses with reduced motion (keep the payoff). Source: "b. Add delightful micro animations when the user achieves..." + "a. Every user interaction must give an immediate and intuitive feedback within under 100ms"
- **SENSE-11** · major · Does delight come from motion, haptics and sound rather than added elements or words, with every celebratory element settling or leaving?
  - Enforces: Engage the Senses, under Zero Clutter and Fewer words (guard). Source: "No more, no less" + "Every extra word competes for attention." + "b. Add delightful micro animations..."
- **SENSE-12** · major · Can the user read the result and continue or leave at any moment of a delight sequence, with no artificial wait before the result?
  - Enforces: Engage the Senses, under Instant Feedback and 'Feels Effortless' (guard). Source: "Feels \"Effortless\"" + "a. Every user interaction must give an immediate and intuitive feedback within under 100ms"
- **SENSE-13** · major · Is each new sight and sound exceptionally pleasing rather than merely present and glitch-free: designed curves, crisp assets, owned and level-matched sounds, and human taste sign-off on a device?
  - Enforces: Engage the Senses > Why a ('Exceptionally pleasing') + Science 5. Source: "Exceptionally pleasing sensory inputs such as sights and sounds trigger dopamine release" + "...processed as exceptionally pleasing."
- **SENSE-14** · major · When a relevant event arrives without a user action while the app is open, does it get the matching haptic and an in-place visual on the element it affects, without interrupting an open flow?
  - Enforces: Engage the Senses > How a ('on relevant events'). Source: "a. Build in haptics and pleasing sounds on relevant events / completion of relevant actions"

## Purpose-built Unique Design

- **UNIQ-01** · major · Is a novel control or gesture (one with no mainstream app or OS precedent) used only on a high-frequency feature, with low-frequency flows on standard or precedented controls?
  - Enforces: Purpose-built Unique Design > What a (scope: high frequency, where relevant). Source: "a. Where relevant for high frequency features build a custom purpose-built design that departs from the traditional forms and buttons to provide a much more fit-to-purpose interface"
- **UNIQ-02** · major · For a high-frequency feature, does the plan state the job, the primary decision criterion, the conventional baseline and a purpose-built option that is much more fit-to-purpose, shown to the user before code?
  - Enforces: Purpose-built Unique Design > How a (job analysis and a meaningful win). Source: "For a high frequency feature understand what the user is trying to achieve and instead of going with the convention, custom design the interaction to uniquely solve for the challenges of the user." + the iPod and Tinder examples
- **UNIQ-03** · minor · Does the purpose-built design depart from convention in its interaction model (input method, use of the screen, a removed step), not only in styling?
  - Enforces: Purpose-built Unique Design > Why a. Novelty (interaction-level, not cosmetic). Source: "a. Novelty triggers dopamine release" + "departs from the traditional forms and buttons"
- **UNIQ-04** · major · Does each purpose-built interaction's MENT-01 row name a mass-market model it borrows and what is new, the way Tinder borrowed a flick and the iPod a dial?
  - Enforces: Purpose-built Unique Design > How b. IMPORTANT: anchored in Familiar Mental Models. Source: "Use \"Familiar Mental Models\" to ensure the unique design feels intuitive and natural and does not require System 2"
- **UNIQ-05** · blocker · Does a first-time user do the custom interaction right on the first try, with no instruction beyond the control's own outcome label?
  - Enforces: Purpose-built Unique Design > How b. IMPORTANT: the Zero Cognitive Load veto (first try). Source: "b. IMPORTANT: This must not be done in violation of the Zero Cognitive Load principle."
- **UNIQ-06** · blocker · Does the screen carrying the unique design pass every Zero Cognitive Load item (ZCL, CLUT, WORD, DEF, PROG, HIER, FB, CONS, MENT, CHOICE)?
  - Enforces: Purpose-built Unique Design > How b. IMPORTANT: full Zero Cognitive Load compliance. Source: "b. IMPORTANT: This must not be done in violation of the Zero Cognitive Load principle."
- **UNIQ-07** · major · Does every custom gesture or drag control also work with a single pointer and no drag, carry a screen-reader label and action, and stay usable under reduced motion?
  - Enforces: Purpose-built Unique Design usable by everyone (non-drag path, semantics). Source: "...to ensure the unique design feels intuitive and natural and does not require System 2"
- **UNIQ-08** · major · Is every high-frequency feature the change touches either purpose-built or recorded as 'convention kept because' after a UNIQ-02 analysis, never a traditional form or list-with-buttons by default?
  - Enforces: Purpose-built Unique Design > What a (the mandate). Source: "a. Where relevant for high frequency features build a custom purpose-built design that departs from the traditional forms and buttons"
- **UNIQ-09** · major · Does every custom gesture behave physically: it follows the finger, can be reversed mid-gesture, springs back when released short, honours a fast flick, and marks the threshold with one selection haptic?
  - Enforces: Purpose-built Unique Design > How b ('feels intuitive and natural'). Source: "to ensure the unique design feels intuitive and natural and does not require System 2"

## The Science behind Delight (components 1 to 8)

- **SCI-01** · major · Does each completion make the concrete outcome its hero and surface at most one true fact that is better than the user was promised?
  - Enforces: Science 1. Dopamine Release + 2. Reward Prediction (better than expected). Source: "This release can be triggered by various stimuli that exceed expectations or provide a novel joy. Delight often occurs when there's an unexpected positive outcome, causing a surge in dopamine." + "If a reward is better than expected, dopamine release increases..."
- **SCI-02** · blocker · Is every cost, net amount and delay shown before the commit control, limits and lockouts shown when they will bite, and is the result never worse than the screen promised?
  - Enforces: Science 2. Reward Prediction and Error Signaling + 8. Stress (no negative prediction error). Source: "Dopaminergic neurons in the VTA are crucial for predicting rewards." + "Stress and Negative Emotions: These can inhibit the reward system"
- **SCI-03** · major · Does every pending, processing or scheduled state say when it completes and what happens next?
  - Enforces: Science 2. Reward Prediction (honest expectations for pending states). Source: "Dopaminergic neurons in the VTA are crucial for predicting rewards."
- **SCI-04** · major · Does the reward land within 500ms of T0, name the user's choice that earned it, and leave the user where the result is visible?
  - Enforces: Science 3. Activation of the Reward System (reinforce the behaviour). Source: "When these areas are activated, they not only make us feel good but also reinforce behaviors that are likely to reproduce the delightful experience."
- **SCI-05** · minor · Does every milestone the product knows about get an in-place moment on the element it changed, without blocking or delaying the user's first action?
  - Enforces: Science 1 + 3. Milestones become in-app moments. Source: "This release can be triggered by various stimuli that exceed expectations or provide a novel joy." + "reinforce behaviors that are likely to reproduce the delightful experience"
- **SCI-06** · minor · Does the screen use the user's own context (their name, the other person's name, their bank's full name, card last 4, their goal) wherever it is known?
  - Enforces: Science 4. Emotional Response (personal). Source: "Positive emotional responses contribute to feelings of delight, especially when an experience touches us personally or aligns closely with our preferences and values."
- **SCI-07** · major · Is the screen free of guilt, threats, vague loss framing and paid defaults, with every downside stated once as a plain, specific fact?
  - Enforces: Science 4. Emotional Response (values) + 8. Stress (no dark patterns). Source: "...aligns closely with our preferences and values." + "Stress and Negative Emotions: These can inhibit the reward system"
- **SCI-08** · major · Is every gain, saving or avoided cost stated as an explicit number or definite state where it happens, shown as evidence rather than a feature sentence, and the hero when it is the screen's key benefit?
  - Enforces: Science 6. Cognitive Appraisal (benefit judged at a glance). Source: "When an event or experience is perceived as particularly beneficial or satisfying, this area of the brain helps in assessing the situation and contributing to the emotional response."
- **SCI-09** · minor · Wherever another person is involved, are they shown as a person (avatar or initials plus first name) at pick and confirm, and when they act?
  - Enforces: Science 7. Social Interaction (people shown as people). Source: "Humans are inherently social creatures, and delight can often be amplified through social interactions."
- **SCI-10** · minor · Does each person-to-person flow close the loop for both people, and offer an optional way to involve a recipient who isn't a customer yet that is never a gate?
  - Enforces: Science 7. Social Interaction (closure for both sides). Source: "delight can often be amplified through social interactions" + "...areas of the brain responsible for social cognition and empathy..."
- **SCI-11** · blocker · At every commit control, can the user check the exact amount, counterparty, source, fee, net and arrival above it without scrolling, with a reassurance line where they may fear harm?
  - Enforces: Science 8. Stress and Negative Emotions (the point of no return). Source: "Stress and Negative Emotions: These can inhibit the reward system by affecting neurotransmitter levels, particularly dopamine and serotonin, altering how rewards are processed."
- **SCI-12** · blocker · Does every money failure, decline or return say where the money is now and offer a one-tap recovery?
  - Enforces: Science 8. Stress and Negative Emotions (money failures). Source: "Stress and Negative Emotions: These can inhibit the reward system..."
- **SCI-13** · major · Does every error say what happened and offer the one next step as a tappable action, inline where it happened, in calm words with no blame?
  - Enforces: Science 8. Stress and Negative Emotions (calm, recoverable errors). Source: "Stress and Negative Emotions: These can inhibit the reward system..."
- **SCI-14** · major · Are alarm signals used only for states that need action, and do lockouts count real failed submits, warn first and show the reset time?
  - Enforces: Science 8. Stress and Negative Emotions (alarm budget and fair lockouts). Source: "Stress and Negative Emotions: These can inhibit the reward system..."
- **SCI-15** · minor · Do first completions and true milestones get a distinct moment, shown once, beyond the routine success, so the reward is not fully predicted?
  - Enforces: Science 1. Dopamine Release (novel joy) + Purpose-built Why a. Source: "stimuli that exceed expectations or provide a novel joy" + "Novelty triggers dopamine release"
- **SCI-16** · minor · Where a choice earns a reward, is the reward shown as a concrete number at the moment of choosing?
  - Enforces: Science 3. Activation of the Reward System (anticipation). Source: "These areas process rewards and motivate us towards reward-seeking behavior."
- **SCI-17** · major · Does the app honour the user's stated preferences: in-app choices persist and are reused, and OS settings (text size, Bold Text, Reduce Motion, silent switch, System Haptics) are respected or the override is a recorded user decision?
  - Enforces: Science 4. Emotional Response (preferences). Source: "especially when an experience touches us personally or aligns closely with our preferences and values"
- **SCI-18** · blocker · For every validation rule, does the caption name the limit that actually bound, with the amount left, computed from the same value that triggered it, and is every limit enforced as stated?
  - Enforces: Science 2. Reward Prediction + 8. Stress (validation copy tells the truth). Source: "Dopaminergic neurons in the VTA are crucial for predicting rewards." + "Stress and Negative Emotions: These can inhibit the reward system..."
- **SURF-01** · major · Are home screen widgets, Control Center and Lock Screen controls, Live Activities, Siri and App Shortcuts snippets, and push notification copy and actions held to the same items as app screens?
  - Enforces: All three bible sections, on every surface outside app screens. Source: "a. Every user interaction must give an immediate and intuitive feedback within under 100ms" + "Each screen contains exactly and only the elements (words, images, assets) that are both necessary and sufficient to achieve the outcome."
- **WEB-01** · major · Does every change on the web get each applicable item with web evidence, never an N-A for an app-only check?
  - Enforces: All items, with web evidence. Source: "a. Every user interaction must give an immediate and intuitive feedback within under 100ms" + "a. Do not ask users to input information or perform actions that you can perform automatically"

## Process gates

- **PROC-01** · blocker · Does every sentence of the source (ticket, Loom, doc, Figma comment, stakeholder note) have a numbered row with current-build proof before the work is called done?
  - Enforces: Process gate: every requirement proved (Zero Clutter 'sufficient to achieve the outcome'). Source: "Each screen contains exactly and only the elements (words, images, assets) that are both necessary and sufficient to achieve the outcome."
- **PROC-02** · major · Before any code, does the plan state per screen the goal sentence, hero fact and first action, high-frequency yes/no with job statement, the familiar model, the decision count, the events with their sensory tier, the answer key for FRESH-5S, and the spec conflicts as open questions, approved by the user?
  - Enforces: Process gate: plan-time Design for Delight brief. Source: "For a high frequency feature understand what the user is trying to achieve" + "does not require System 2 even when being used for the first time"
- **PROC-03** · blocker · Was this checklist run in full before 'done', with every in-scope item given a result per its tier, each backed by evidence, with no cap on findings in the full report?
  - Enforces: Process gate: the full checklist, nothing skipped. Source: "Design interfaces that dont just minimize cognitive load but rather represent Zero Cognitive load" + "Principles in order of priority"
- **PROC-04** · major · Was each screen captured and checked in every state its code can produce, not just the default one?
  - Enforces: Process gate: every state, first-run and returning. Source: "3. What it feels like to a new or returning user" + "even when being used for the first time"
- **PROC-05** · major · Were the first-use items judged by independent reviewers against a pre-written answer key, graded by someone other than the builder, with a human check on first-run screens and custom interactions?
  - Enforces: Process gate: the curse of knowledge (fresh eyes). Source: "Zero Cognitive means a user interface that does not require System 2 even when being used for the first time" + "Further Reading: ChatGPT - System 1 vs System 2"
- **PROC-06** · major · Where items, rules or skills conflict, was the conflict settled in the stated order and written down?
  - Enforces: Process gate: priority order. Source: "Principles in order of priority" + "b. IMPORTANT: This must not be done in violation of the Zero Cognitive Load principle."
- **PROC-07** · blocker · Is every bible violation found in spec copy, a frozen screen, Figma-specified UI, a product rule, or a ticket, Loom, doc or stakeholder requirement reported as SPEC-CONFLICT with a proposal, and left as specified until the user decides?
  - Enforces: Process gate: flag spec, frozen and ticket conflicts, never fix them silently. Source: "Principles in order of priority" (applied to frozen spec too)
- **PROC-08** · blocker · Is every new string traced to a source or listed as 'new, needs approval', is source copy unchanged word for word except line breaks, are legal texts kept intact, and is every rejected string removed repo-wide with a guard?
  - Enforces: Process gate: copy integrity (Zero Clutter, Fewer words). Source: "Each screen contains exactly and only the elements (words, images, assets) that are both necessary and sufficient" + "Every extra word competes for attention."
- **PROC-09** · major · Do the objective gates pass, is every new behaviour locked by a test, are baseline counts no worse, and does every comment cited as evidence match the code?
  - Enforces: Process gate: objective gates, regression locks and honest evidence. Source: "a. Every user interaction must give an immediate and intuitive feedback within under 100ms" + "a. Repeat design elements and patterns"
- **PROC-10** · major · Is every haptic and sound row felt and heard on a physical device for each supported platform, including silent-switch and background-music cases, or marked PENDING-DEVICE per platform?
  - Enforces: Process gate: device sign-off for the senses. Source: "a. Build in haptics and pleasing sounds on relevant events / completion of relevant actions" + "Exceptionally pleasing sensory inputs such as sights and sounds trigger dopamine release"
- **PROC-11** · major · Does every stakeholder demo video have the voiceover in sync, no flashes, no people's names and no detours through internal menus or test screens?
  - Enforces: Process gate: stakeholder walkthrough videos (house rule from memory walkthrough-videos and walkthrough-no-names; sync and flash apply Senses Why a to demos). Source: "Exceptionally pleasing sensory inputs such as sights and sounds trigger dopamine release"
