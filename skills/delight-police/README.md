# Delight Police

A portable skill that reviews a design screen against Design for Delight
principles — same bar as a tough CRO delight review. Product managers and
designers use the same skill.

**Version:** 0.1.1

## Who it is for

- **Designers** — layout, words, hierarchy, motion
- **Product managers** — what the product should stop asking, default, or split
  into one context

Attach a screenshot, a Figma frame, a mock, or a short description. Say who
the user is and what the screen is for. Say when the feature is high frequency
if you want Purpose-built Unique Design assessed.

## What it does

Reviews in principle priority order:

1. Zero Cognitive Load (clutter → fewer words → smart defaults → one context →
   hierarchy → instant feedback → consistency → familiar models → fewer
   analytical choices)
2. Engage the Senses
3. Purpose-built Unique Design (only when marked high frequency)

Every review returns a first-use read, findings in that order, what to leave
alone, designer changes, and product calls.

## Install

Delight Police ships inside the [Zero Clutter](https://github.com/prithvi-zeta/zero-clutter)
plugin (installing Zero Clutter installs it too). To install it on its own,
clone the repo, then from this skill folder:

```bash
cd skills/delight-police
python3 scripts/install.py
```

That copies the skill into each agent tool found on the machine:

| Tool | Skills folder | Slash command |
| --- | --- | --- |
| Claude Code | `~/.claude/skills/delight-police` | `/delight-police` |
| Cursor | `~/.cursor/skills/delight-police` | `/delight-police` |
| Codex | `~/.codex/skills/delight-police` | none — say "run delight police on this" |
| GitHub Copilot | `~/.copilot/skills/delight-police` | `/delight-police` (VS Code prompts when available) |

Options:

```bash
python3 scripts/install.py --link              # symlink for maintainers
python3 scripts/install.py --tools claude,cursor
python3 scripts/install.py --uninstall
```

After a pull, run the installer again (or use `--link` once so updates are
picked up automatically). Restart the agent after install.

### Claude chat and ChatGPT

These tools do not load `SKILL.md` by themselves. Attach `SKILL.md` and
`principles.md` from this folder, or add this folder as project knowledge,
then ask to run Delight Police on a screen. There is no install that registers
the skill inside ChatGPT.

## How to run a review

- Claude Code / Cursor / Copilot: `/delight-police` then attach the screen, or
  say "run delight police on this"
- Codex: "run delight police on this" (no slash commands)

## Where it works

- Screenshots, Figma frames, mocks, and short screen descriptions
- First-use cognitive load, clutter, copy length, defaults, hierarchy,
  consistency, familiar patterns, analytical choices
- High-frequency features, when you say so, for Purpose-built Unique Design

## Where it fails

- **Stills cannot prove** haptics, sound, motion quality, or the under-100ms
  feedback rule. The skill says so instead of guessing.
- **A unique gesture that needs instructions** fails Zero Cognitive Load. The
  skill will not treat that as delight.
- **Elements not on the screen** must not be flagged. Findings point only at
  what is visible or stated.
- **Chat-only tools** need the files attached; the installer cannot register
  them there.

## Update the skill

1. Change files in this folder (and bump the version in `SKILL.md`
   frontmatter and this README).
2. Add a line to [CHANGELOG.md](CHANGELOG.md).
3. Run the two fixtures in [examples.md](examples.md) and check the required
   findings still appear before you release.
4. Commit. Teammates pull and from this folder run
   `python3 scripts/install.py` again (or use `--link`).

## Layout

```
delight-police/
  README.md
  CHANGELOG.md
  SKILL.md
  principles.md
  examples.md
  commands/delight-police.md
  scripts/install.py
```

This skill lives in the [zero-clutter](https://github.com/prithvi-zeta/zero-clutter)
repo alongside other shared skills.

## Agent Fluency note

Authoring and publishing this skill is Building & Customization. Org Influence
starts when the real skill file is in a shared place teammates can take, you
write where it works and where it fails (this README), you answer their
questions, and at least one teammate reuses it on their own screen. A copy only
in your personal skills folder is not enough for Org Influence.
