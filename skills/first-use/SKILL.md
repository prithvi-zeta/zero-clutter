---
name: first-use
description: >-
  Zero Clutter gate G5. Run a first-use test of a new flow or first-run
  screen with someone who hasn't seen it, or prepare the step-by-step script
  for one, and record where they hesitate. Use before sign-off on onboarding,
  empty states, new features and any custom interaction, or when someone asks
  for a "first-use test", "fresh eyes" or "would a new user get this".
metadata:
  version: "0.1.0"
---

# first-use (G5)

Paths below are relative to the zero-clutter repo. In an installed copy
they are under `shared/` next to this file.

The only test of "doesn't need instructions" is someone who has never seen it.

## Who

A person who hasn't worked on it or seen it. An agent that hasn't seen the
build's reasoning can do a first pass from screenshots, but for first-run
screens and custom gestures a person must also do it: an agent pass alone is
PENDING-HUMAN.

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
a question for Bhavin. A custom interaction that anyone got wrong on first try
ships as the familiar control instead (UNIQ-05).
