# First-use mode (G5)

The only test of "doesn't need instructions" is someone who has never seen it.

## Who

A person who hasn't worked on it or seen it. An agent that hasn't seen the
build's reasoning can do a first pass from screenshots, but for first-run
screens and custom gestures a person must also do it: an agent pass alone is
`pending` (a person is still needed).

## Steps

1. Prepare the test with `templates/first-use-test.md`: the starting state, the
   task in the user's words ("open an account and add $100"), and the
   screenshot or live build for each step. No hints.
2. At each step, before they act, ask:
   - What would you do next?
   - What do you expect to happen?
   - Is anything unclear?
3. Let them act. Note every pause over a couple of seconds, wrong tap,
   question, or "oh".
4. Don't explain anything. If they're stuck, note it, then move them on.
5. Fill in the result: per step, what they said, what happened, and a verdict
   (clear / hesitated / stuck).

## Passes when

They finish the flow with no help. Every hesitation is fixed, or written up as
a question for the approver. A custom interaction that anyone got wrong on first try
ships as the familiar control instead (UNIQ-05).
