# Zero Clutter

Checks any UI against Bhavin's **Design for Delight** principles. Tells you what to fix, what to decide and what to keep.

- Works on iOS, Android, Flutter, web apps and websites
- Takes code, a build, a URL, a screenshot or a Figma frame
- Runs in Claude Code, Cursor, Codex, GitHub Copilot, Gemini CLI or any chat

## Install

**Claude Code**
```text
/plugin marketplace add prithvi-zeta/zero-clutter
/plugin install zero-clutter@zero-clutter
```

**Codex, Copilot, Cursor**
```bash
git clone https://github.com/prithvi-zeta/zero-clutter
python3 zero-clutter/scripts/install.py
```

**Gemini CLI**
```bash
gemini extensions install https://github.com/prithvi-zeta/zero-clutter
```

**Any chat**: upload the `skills/zero-clutter` folder, then say "run zero clutter on this".

Restart the tool after installing.

## Set up a repo

Say `zero-clutter setup` in the repo. It adds:

- `.zero-clutter/adapter.md`: how this project takes screenshots, runs tests, who approves
- `.zero-clutter/house-rules.md`: rules learned in this project
- `.zero-clutter/feedback-log.md`: review comments and what they taught
- A section in `AGENTS.md` and a PR template

Commit them so the team shares them.

## Use it

Say `zero-clutter` with what you have:

- **A ticket or doc**: lists every requirement and asks questions (G1)
- **A design or screenshot**: checks every element and walks the flow (G2)
- **A change**: runs the 15 checks (G3)
- **`zero-clutter pr`**: full review before merge (G4)
- **`zero-clutter first-use`**: a test for someone new (G5)
- **Copy**: says what a first-time user will understand, with options
- **Feedback**: logs it and adds a rule so it can't happen twice

## The answer

- 🔧 **Fix**: a problem. 🔴 blocking means it can't ship
- 🤔 **Decide**: a call for the approver
- 💡 **Suggest**: optional
- ⏳ **Check**: needs a device or a person
- ✅ **Keep**: what works

Findings are numbered, so you can say "fix 1, decide 3". Say "details" for the full report. More: [report format](skills/zero-clutter/references/report-format.md), [gates](skills/zero-clutter/references/gates.md).

## What it checks

- [Bhavin's principles](skills/zero-clutter/references/principles/design-for-delight-principles.md) and [The Science behind Delight](skills/zero-clutter/references/principles/the-science-behind-delight.md)
- [The checklist](skills/zero-clutter/references/checklist.md): 15 questions, [133 items](skills/zero-clutter/references/checklist-items.md)
- [Shared house rules](skills/zero-clutter/references/house-rules.md) from past reviews
- The project's own rules

## What it can't do

- Check contrast
- Judge haptics, sound or speed from a still image
- Replace a first-use test with a real person
- Decide taste for the approver

## CI

Copy [the workflow](examples/ci/zero-clutter-gate.yml) into `.github/workflows/`. PRs fail if UI changed without a report, or a finding is blocking.

## Change Zero Clutter

- Bump the version in `SKILL.md`, both plugin manifests and `gemini-extension.json`
- Add a line to [CHANGELOG.md](CHANGELOG.md) and a `release-notes/<version>.md`
- Run `python3 scripts/check.py`
- Open a PR. Never edit the principles' wording
