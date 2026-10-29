# Zero Clutter

The quality system for everything we design and build: one set of
principles, one checklist, six gates, and a feedback loop that learns from
every review. It works in any project and any agent tool (Claude Code, Cursor,
Codex, Copilot), and for people without one.

**The goal:** when work reaches Bhavin, it has already passed his principles,
his past feedback and a first-use test. Anything he still flags is an
*escape*: we find why the gates missed it and add a rule, so the same miss
can't happen twice. We track escapes per release, and the target is zero.

## The pieces

| Folder | What it is |
| --- | --- |
| [principles/](principles/) | Bhavin's two documents, word for word: *Design for Delight Principles* and *The Science behind Delight*. The one source of truth. |
| [checklist/](checklist/) | The [15-question checklist](checklist/README.md) for people and the [134 items](checklist/items.md) behind it, each with a stable ID. |
| [gates/](gates/) | The six gates from spec to release: who runs each, and what passes it. |
| [feedback-log/](feedback-log/) | Every piece of review feedback, its root cause, and the house rule it became. |
| [skills/](skills/) | Agent skills for each gate. |
| [delight-police/](delight-police/) | Screen and Figma review against the principles (G1, G2). |
| [templates/](templates/) | PR template, review report, ticket checklist, first-use test, escape report. |
| [scripts/](scripts/) | Installer and the consistency check. |

## The loop

```
 Bhavin's spec ──► G1 Spec ──► G2 Design ──► G3 Build ──► G4 PR ──► G5 First use ──► G6 Release ──► Bhavin
                     ▲                                                                              │
                     └──────────── feedback-intake: escape → root cause → house rule → test ◄───────┘
```

| Gate | When | Who | Passes when |
| --- | --- | --- | --- |
| [G1 Spec](gates/README.md#g1-spec) | Before design | PM, with `spec-check` | Every requirement numbered; every open question answered by Bhavin |
| [G2 Design](gates/README.md#g2-design) | Before build | Designer, with `delight-police` | No open Zero Cognitive Load findings |
| [G3 Build](gates/README.md#g3-build) | Every change | Developer or agent, with `build-gate` | The quick checks pass |
| [G4 PR](gates/README.md#g4-pr) | Before merge | `build-gate` report + one person | 0 blocker FAILs; report attached; CI green |
| [G5 First use](gates/README.md#g5-first-use) | Before sign-off | Someone who hasn't seen it, with `first-use` | Finishes it unaided |
| [G6 Release](gates/README.md#g6-release) | Before shipping or showing Bhavin | Release owner | All gates passed; demo + report ready |

## Use it in a project

```bash
git clone https://github.com/prithvi-zeta/zero-clutter
cd zero-clutter
python3 scripts/install.py                          # skills for your agent tools
python3 scripts/install.py --project ~/path/to/repo # adopt in a repo
```

Adopting a repo adds a PR template, an `AGENTS.md` section that points every
agent at the principles and gates, and a `zero-clutter.md` file for that
project's **adapter**: how each checklist item is verified on its stack. The
installer only writes what it marks as its own and never replaces anything
else.

Projects using it:

| Project | Adapter |
| --- | --- |
| RyzeDesign (Flutter app + web funnels) | `docs/delight/checklist.md` (134 items, with Flutter and web verify steps) |

## Rules for the system itself

1. **Principles are verbatim.** Nobody edits `principles/`. A new version of
   Bhavin's docs replaces the files and bumps the version.
2. **Checklist IDs are stable.** Never renumber or reuse an ID. Retire an item
   by marking it retired.
3. **Every escape becomes a rule.** Use `feedback-intake` within 48 hours of the
   feedback.
4. **Taste calls go to Bhavin as questions, before the build.** A gate never
   guesses his taste; it asks at G1 and records the answer.
5. **Check before you release a change here:** `python3 scripts/check.py` must
   pass (copies in sync, every ID resolvable, every rule traced).

See [CHANGELOG.md](CHANGELOG.md) for versions.
