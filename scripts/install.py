#!/usr/bin/env python3
"""Install Zero Clutter where there's no plugin marketplace, or set up a repo.

  python3 scripts/install.py                       # every agent tool found
  python3 scripts/install.py --tools codex,copilot
  python3 scripts/install.py --link                # link to this clone (maintainers)
  python3 scripts/install.py --project ~/code/app  # set up a repo (project-level skills too)
  python3 scripts/install.py --uninstall

Claude Code and Cursor users should prefer the plugin (see README). This script
copies the skills (zero-clutter, delight-police) and the reviewer agent into:

  Claude Code   ~/.claude/skills, ~/.claude/agents
  Cursor        ~/.cursor/skills, ~/.cursor/agents
  Codex         ~/.agents/skills
  Copilot       ~/.copilot/skills

--project also writes, only where absent (never overwriting):
  .zero-clutter/adapter.md, house-rules.md, feedback-log.md
  .github/pull_request_template.md
  a marked Zero Clutter section in AGENTS.md

It only removes what it marked. Python 3.9+, standard library only.
"""
from __future__ import annotations

import argparse
import datetime as dt
import os
import pathlib
import re
import shutil
import sys

HOME = pathlib.Path(os.environ.get("ZC_HOME") or pathlib.Path.home())
ROOT = pathlib.Path(__file__).resolve().parent.parent
MARK_FILE = ".installed-by-zero-clutter"
OTHER_MARKS = [".installed-by-delight-police"]
MARK_LINE = "<!-- zero-clutter -->"
SKIP = shutil.ignore_patterns("__pycache__", "*.pyc", ".DS_Store", MARK_FILE, *OTHER_MARKS)
START, END = "<!-- zero-clutter:start -->", "<!-- zero-clutter:end -->"
TEMPLATES = ROOT / "skills" / "zero-clutter" / "references" / "templates"

TOOLS = {
    "claude": ("Claude Code", HOME / ".claude", HOME / ".claude" / "skills", HOME / ".claude" / "agents"),
    "cursor": ("Cursor", HOME / ".cursor", HOME / ".cursor" / "skills", HOME / ".cursor" / "agents"),
    "codex": ("Codex", HOME / ".codex", HOME / ".agents" / "skills", None),
    "copilot": ("GitHub Copilot", HOME / ".copilot", HOME / ".copilot" / "skills", None),
}


def skills() -> list[pathlib.Path]:
    return sorted(p for p in (ROOT / "skills").iterdir() if (p / "SKILL.md").is_file())


def agents() -> list[pathlib.Path]:
    return sorted((ROOT / "agents").glob("*.md"))


def ours(path: pathlib.Path) -> bool:
    if path.is_symlink():
        try:
            return ROOT in path.resolve().parents or path.resolve() == ROOT
        except OSError:
            return False
    if path.is_dir():
        return any((path / m).is_file() for m in [MARK_FILE, *OTHER_MARKS])
    try:
        return MARK_LINE in path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return False


def remove(path: pathlib.Path) -> None:
    if path.is_symlink() or path.is_file():
        path.unlink()
    elif path.is_dir():
        shutil.rmtree(path)


def place(src: pathlib.Path, dest: pathlib.Path, link: bool, force: bool) -> str | None:
    """Copy or link src to dest. Returns a note when it leaves something alone."""
    if (dest.exists() or dest.is_symlink()) and not ours(dest) and not force:
        return f"{dest} exists and isn't ours. Left alone (use --force)."
    remove(dest)
    dest.parent.mkdir(parents=True, exist_ok=True)
    if link:
        dest.symlink_to(src, target_is_directory=src.is_dir())
    elif src.is_dir():
        shutil.copytree(src, dest, ignore=SKIP)
        (dest / MARK_FILE).write_text(f"From {ROOT}, {dt.date.today().isoformat()}.\n", encoding="utf-8")
    else:
        text = src.read_text(encoding="utf-8")
        dest.write_text(text if MARK_LINE in text else text + f"\n{MARK_LINE}\n", encoding="utf-8")
    return None


def install(key: str, link: bool, force: bool, undo: bool) -> list[str]:
    label, home, skill_dir, agent_dir = TOOLS[key]
    notes = []
    targets = [(s, skill_dir / s.name) for s in skills()]
    if agent_dir:
        targets += [(a, agent_dir / a.name) for a in agents()]
    for src, dest in targets:
        if undo:
            if (dest.exists() or dest.is_symlink()) and ours(dest):
                remove(dest)
        else:
            note = place(src, dest, link, force)
            if note:
                notes.append(f"{label}: {note}")
    notes.append(f"{label}: {'removed' if undo else ('linked' if link else 'installed')} "
                 f"{', '.join(s.name for s in skills())}{' + reviewer agent' if agent_dir else ''}")
    return notes


def agents_section() -> str:
    return (
        f"{START}\n## Zero Clutter\n\n"
        "Every user-facing change here passes [Zero Clutter](https://github.com/prithvi-zeta/zero-clutter) "
        "(Bhavin's Design for Delight principles, the checklist and the house rules). "
        "How this project runs it: [.zero-clutter/adapter.md](.zero-clutter/adapter.md).\n\n"
        "- New work from a ticket, doc or Loom: run `zero-clutter` on it first (spec mode).\n"
        "- Before showing or calling anything done: run `zero-clutter` (build mode); fix every blocker.\n"
        "- Before merge: `zero-clutter` (pr mode); put the verdict in the PR.\n"
        "- Review feedback: run `zero-clutter` with it (feedback mode).\n"
        f"{END}\n"
    )


def adopt(project: pathlib.Path, undo: bool) -> list[str]:
    if not project.is_dir():
        return [f"{project} is not a folder."]
    notes = []
    files = {
        project / ".zero-clutter" / "adapter.md": (TEMPLATES / "project-adapter.md").read_text(encoding="utf-8"),
        project / ".zero-clutter" / "house-rules.md": f"{MARK_LINE}\n# House rules (this project)\n\nRules learned here, IDs P-01, P-02, … Same format as the shared house rules.\n",
        project / ".zero-clutter" / "feedback-log.md": f"{MARK_LINE}\n# Feedback log (this project)\n\n| ID | Date | Source | Feature | What was said (quoted) | Should have caught it | Root cause | Rule |\n| --- | --- | --- | --- | --- | --- | --- | --- |\n",
        project / ".github" / "pull_request_template.md": (TEMPLATES / "pull_request_template.md").read_text(encoding="utf-8"),
    }
    for path, text in files.items():
        rel = path.relative_to(project)
        if undo:
            if path.is_file() and ours(path) and path.name != "feedback-log.md" and path.name != "house-rules.md":
                path.unlink()
                notes.append(f"removed {rel}")
        elif path.exists():
            notes.append(f"kept {rel}" if ours(path) else f"left {rel} alone (not ours)")
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")
            notes.append(f"wrote {rel}")
    agents_md = project / "AGENTS.md"
    current = agents_md.read_text(encoding="utf-8") if agents_md.is_file() else ""
    block = re.compile(re.escape(START) + r".*?" + re.escape(END) + r"\n?", re.S)
    if undo:
        if block.search(current):
            agents_md.write_text(block.sub("", current), encoding="utf-8")
            notes.append("removed the Zero Clutter section from AGENTS.md")
    else:
        sep = "" if not current or current.endswith("\n\n") else ("\n" if current.endswith("\n") else "\n\n")
        updated = block.sub(agents_section(), current) if block.search(current) else current + sep + agents_section()
        if updated != current:
            agents_md.write_text(updated, encoding="utf-8")
            notes.append("updated AGENTS.md")
    if not undo:
        notes.append("next: open .zero-clutter/adapter.md and fill it in (or ask your agent: \"zero-clutter setup\")")
    return notes


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--tools", help="comma-separated: claude, cursor, codex, copilot (default: all found)")
    parser.add_argument("--link", action="store_true", help="link to this clone instead of copying")
    parser.add_argument("--force", action="store_true", help="replace files this script didn't write")
    parser.add_argument("--project", type=pathlib.Path, help="also set up Zero Clutter in this repo")
    parser.add_argument("--uninstall", action="store_true", help="remove what this script installed")
    args = parser.parse_args(argv)

    wanted = [t.strip() for t in args.tools.split(",")] if args.tools else list(TOOLS)
    unknown = [t for t in wanted if t not in TOOLS]
    if unknown:
        parser.error("unknown tool: " + ", ".join(unknown))
    notes, found = [], 0
    for key in wanted:
        if not TOOLS[key][1].is_dir():
            if args.tools:
                notes.append(f"{TOOLS[key][0]}: not found on this machine. Skipped.")
            continue
        found += 1
        notes += install(key, args.link, args.force, args.uninstall)
    if args.project:
        notes += adopt(args.project.expanduser().resolve(), args.uninstall)
    if not found and not args.project:
        print("No agent tool found (Claude Code, Cursor, Codex, GitHub Copilot).")
        return 1
    print("\n".join(notes))
    if found and not args.uninstall:
        print('\nRestart your agent, then type /zero-clutter or say "zero clutter this".')
    return 0


if __name__ == "__main__":
    sys.exit(main())
