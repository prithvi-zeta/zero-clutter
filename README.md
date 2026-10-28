# Zero Clutter

Shared agent skills for product managers and designers. One repo, skills you
can take and run in Claude Code, Cursor, Codex, Copilot, or by attaching the
files in chat.

## Skills

| Skill | Folder | What it does |
| --- | --- | --- |
| [Delight Police](delight-police/) | `delight-police/` | Reviews a design screen against Design for Delight |

## Install a skill

Each skill has its own installer. From the skill folder:

```bash
cd delight-police
python3 scripts/install.py
```

See that skill’s README for slash commands, where it works, and where it fails.

## Add another skill

1. Create a folder at the repo root (same layout as `delight-police/`).
2. Put `SKILL.md`, a short README (install, where it works, where it fails),
   and a versioned changelog in that folder.
3. List it in the table above.
