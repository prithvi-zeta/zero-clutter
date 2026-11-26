# Design mode fixtures

Run a change to design mode against these fixtures before you release it.
Each fixture lists what a correct review must find. Wording can differ; the
principles and the changes must match.

---

## Fixture 1 · Transfer amount form (still)

**Input to the agent**

> Review this screen for delight. Audience: retail banking customer sending
> money to a saved payee. Job: enter an amount and confirm the transfer.
>
> Screen description (no image): Title "Initiate Funds Transfer Transaction".
> Subtitle "Please carefully review all details before submitting your request
> to transfer funds to the selected beneficiary." Three empty fields labeled
> "Enter transfer amount in your preferred currency", "Select debit account
> from the list of linked accounts", and "Optional notes / reference for your
> records". Primary button "Submit Transfer Request". Secondary link "Need
> help? Read our transfer FAQ". A right column lists "Related products",
> "Promotional offers", and three ad cards. Footer repeats "Please carefully
> review all details before submitting."

**Must find**

| Principle | What is wrong | Required change |
| --- | --- | --- |
| Zero Clutter | Related products, offers, and ad cards are not needed to send money | Remove the right column from this screen |
| Use fewer words | Long title, repeated review warning in subtitle and footer, verbose labels | Short title (e.g. Transfer), one short line of help if needed, short labels (Amount, From account, Note) |
| Smart Defaults and Auto completes | Debit account left empty when accounts are already linked | Pre-select the usual debit account |
| Progressive Disclosure / One page, One context | Transfer plus marketing in one view | One context: transfer only |
| Strong and Logical Visual Hierarchy | Two-column layout forces top-to-bottom and left-to-right scanning | Single column; amount and primary action dominate |
| Reduce Analytical Choices | User must pick an account and invent an amount with no guidance | Default account; optional amount chips or last-sent amount if known |

**Must also say**

- First-use read: a new user does not act instinctively; too much copy and a competing column.
- Cannot judge from a still: haptics, sound, under-100ms feedback.
- Not assessed (not marked high frequency) for Purpose-built Unique Design.
- Fix rows include shorter copy, single column, stronger primary action.
- Decide rows include default debit account, drop marketing from this step, stop repeating the review warning.

**Must not**

- Invent a biometric step or a success animation as if it were already on the screen.
- Recommend a novel gesture that needs instructions.

---

## Fixture 2 · Card freeze (high frequency, still)

**Input to the agent**

> Review this screen for delight. Audience: cardholder who lost their card.
> Job: freeze the card now. This is a high frequency feature for people who
> misplace a card.
>
> Screen description (no image): Full-screen photo of a generic credit card.
> Centered text "Swipe up if you want to temporarily disable card
> transactions; swipe down to keep spending active. Consult the security
> policy if unsure." No freeze button. Tiny question-mark icon in the corner.
> No confirmation that anything happened after a gesture.

**Must find**

| Principle | What is wrong | Required change |
| --- | --- | --- |
| Use fewer words | Long instruction explaining the gesture | If a gesture stays, it must need no instruction; otherwise use a clear Freeze control |
| Familiar Mental Models | Invented swipe-up / swipe-down with no known pattern for freeze | Prefer a single Freeze control, or a gesture that maps to a known pattern without copy |
| Instant Feedback | No confirmation after the gesture | Immediate state change (Frozen) with clear feedback |
| Reduce Analytical Choices | "Consult the security policy if unsure" forces analytic mode | Remove; freeze should be one decisive action |
| Purpose-built Unique Design | Custom gesture attempted, but it violates Zero Cognitive Load because it needs instructions and System 2 | Unique design is only valid if first use needs no instructions; redesign so freeze is instinctive |

**Must also say**

- First-use read: a new user cannot act without reading instructions; fails Zero Cognitive Load.
- Cannot judge from a still: haptics, sound, under-100ms feedback — and call out missing confirmation as Instant Feedback from what is stated.
- Purpose-built Unique Design is assessed (marked high frequency) and currently fails the IMPORTANT rule in [the principles](principles/design-for-delight-principles.md).
- Fix rows: visible Freeze control or an instinctive gesture; clear Frozen state; drop the policy aside.
- Decide rows: one action to freeze; no policy detour on the critical path.

**Must not**

- Praise the unique swipe as delight while it still needs instructions.
- Flag clutter that is not described on the screen.

---

## Fixture 3 · Receive money flow (three stills)

**Input to the agent**

> Review this flow. Audience: someone who was sent $50 and tapped the link in
> their text message. Job: claim the money. The spec says the button on
> screen 2 is "Verify account via Plaid".
>
> Screen 1: Title "Dustin, you've got $50" "Link a bank account belonging to
> Dustin Set to claim". Button "Proceed". Below it a Plaid logo and
> "Secured by Plaid".
>
> Screen 2: "$50 initiated". Two options: "Withdraw now" with "Download Ryze
> app", and "Send to Chase ••4567" with "Arrives in 3 business days".
>
> Screen 3 (after tapping Download Ryze app): a web form, "Sign up", with
> fields First name, Last name, Date of birth. Button "Continue".

**Must find**

| Rule | What is wrong | Required change |
| --- | --- | --- |
| HR-18 (blocking) | "Download Ryze app" leads to a web form, not to the download | The button opens the download; anything still needed happens in the app |
| HR-30 | "Proceed" doesn't say it links a bank through Plaid | A: "Link Dustin's bank account" with "Secured by Plaid" as a second line (new, needs approval) |
| HR-04 | The spec's "Verify account via Plaid" was replaced with "Proceed" | Use the spec's words, or send the change to the approver as a question (HR-30 and HR-04 can be one Decide row) |
| HR-26 | "…belonging to Dustin Set to claim" runs two statements together | Full stop between them |
| HR-31 | Screen 3 is a generic sign-up and no longer mentions the $50 | Keep the story: "Verify details to start using your $50" (new, needs approval) |

**Must also say**

- The copy read table marks the screen 1 helper `😕 Confusing`.
- First-use read: a recipient doesn't know why a form appears after tapping Download.

**Must not**

- Put any screen in Keep before the flow walk is done.
- Change the spec's button copy in the work itself.
