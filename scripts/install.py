#!/usr/bin/env python3
"""Install Zero Clutter: every skill for your agent tools, and optionally a repo.

  python3 scripts/install.py                         # all skills, every tool found
  python3 scripts/install.py --link                  # link instead of copy (maintainers)
  python3 scripts/install.py --tools claude,cursor
  python3 scripts/install.py --project ~/code/app    # also adopt Zero Clutter in a repo
  python3 scripts/install.py --uninstall

Skills: delight-police and everything under skills/. A copied skill gets a
`shared/` folder (principles, checklist, feedback log, templates) so its
paths work outside this repo; a linked skill reads them from the repo.

Adopting a repo writes, only if absent or written by this script before:
  .github/pull_request_template.md   the gates and the 15 checks
  zero-clutter.md                    the project's adapter (fill it in)
  AGENTS.md                          a marked Zero Clutter section, appended

It never replaces a skill, command or file it didn't write; --uninstall removes
only what it marked. Python 3.9 or later, standard library only.
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
OTHER_MARKS = [".installed-by-delight-police"]  # delight-police's own installer
MARK_LINE = "<!-- zero-clutter -->"
SHARED = ["principles", "checklist", "feedback-log", "templates"]
SKIP = shutil.ignore_patterns("__pycache__", "*.pyc", ".DS_Store", MARK_FILE, *OTHER_MARKS)
AGENTS_START = "<!-- zero-clutter:start -->"
AGENTS_END = "<!-- zero-clutter:end -->"


def skills() -> dict:
    found = {"delight-police": ROOT / "delight-police"}
    for path in sorted((ROOT / "skills").iterdir()):
        if (path / "SKILL.md").is_file():
            found[path.name] = path
    return found


def description(skill: pathlib.Path) -> str:
    head = (skill / "SKILL.md").read_text(encoding="utf-8").split("---")[1]
    m = re.search(r"description:\s*>-?\s*\n((?:\s+.+\n)+)", head) or re.search(
        r"description:\s*(.+)", head
    )
    text = " ".join(m.group(1).split()) if m else skill.name
    return text.split(". ")[0].rstrip(".") + "."


def vscode_prompts() -> pathlib.Path | None:
    for base in [
        HOME / "Library" / "Application Support" / "Code" / "User",
        HOME / ".config" / "Code" / "User",
        HOME / "AppData" / "Roaming" / "Code" / "User",
    ]:
        if base.is_dir():
            return base / "prompts"
    return None


def tools() -> dict:
    found = {
        "claude": {"label": "Claude Code", "home": HOME / ".claude",
                   "commands": HOME / ".claude" / "commands", "suffix": ".md"},
        "cursor": {"label": "Cursor", "home": HOME / ".cursor",
                   "commands": HOME / ".cursor" / "commands", "suffix": ".md"},
        "codex": {"label": "Codex", "home": HOME / ".codex", "commands": None, "suffix": ""},
        "copilot": {"label": "GitHub Copilot", "home": HOME / ".copilot",
                    "commands": vscode_prompts(), "suffix": ".prompt.md"},
    }
    for key, tool in found.items():
        tool["present"] = tool["home"].is_dir() or (key == "copilot" and (HOME / ".copilot").is_dir())
    return found


def ours(dest: pathlib.Path) -> bool:
    if dest.is_symlink():
        try:
            return dest.resolve().is_relative_to(ROOT)
        except (OSError, AttributeError):
            return False
    return any((dest / m).is_file() for m in [MARK_FILE, *OTHER_MARKS])


def marked(path: pathlib.Path) -> bool:
    try:
        return MARK_LINE in path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return False


def remove(path: pathlib.Path) -> None:
    if path.is_symlink() or path.is_file():
        path.unlink()
    elif path.is_dir():
        shutil.rmtree(path)


def command_text(name: str, skill_dir: pathlib.Path, about: str) -> str:
    return (
        f"---\ndescription: {about}\nargument-hint: \"[what to check]\"\n---\n{MARK_LINE}\n\n"
        f"Read `{skill_dir}/SKILL.md` completely and follow it.\n\n"
        f"What the person typed after the command: $ARGUMENTS\n"
    )


def install_skill(tool: dict, name: str, src: pathlib.Path, link: bool, force: bool) -> list:
    notes = []
    dest = tool["home"] / "skills" / name
    if (dest.exists() or dest.is_symlink()) and not ours(dest) and not force:
        return [f"{tool['label']}: {dest} exists and isn't ours. Left alone (use --force)."]
    remove(dest)
    dest.parent.mkdir(parents=True, exist_ok=True)
    if link:
        dest.symlink_to(src, target_is_directory=True)
    else:
        shutil.copytree(src, dest, ignore=SKIP)
        for folder in SHARED:
            shutil.copytree(ROOT / folder, dest / "shared" / folder, ignore=SKIP)
        (dest / MARK_FILE).write_text(
            f"Installed from {ROOT} on {dt.date.today().isoformat()}.\n", encoding="utf-8"
        )
    notes.append(f"{tool['label']}: {name} {'linked' if link else 'copied'}")
    if tool["commands"]:
        cmd = tool["commands"] / f"{name}{tool['suffix']}"
        if cmd.exists() and not marked(cmd) and not force:
            notes.append(f"{tool['label']}: {cmd} exists and isn't ours. Left alone.")
        else:
            cmd.parent.mkdir(parents=True, exist_ok=True)
            cmd.write_text(command_text(name, dest, description(src)), encoding="utf-8")
    return notes


def uninstall_skill(tool: dict, name: str) -> list:
    notes = []
    dest = tool["home"] / "skills" / name
    if (dest.exists() or dest.is_symlink()) and ours(dest):
        remove(dest)
        notes.append(f"{tool['label']}: removed {name}")
    if tool["commands"]:
        cmd = tool["commands"] / f"{name}{tool['suffix']}"
        if cmd.is_file() and marked(cmd):
            cmd.unlink()
    return notes


def agents_section() -> str:
    return (
        f"{AGENTS_START}\n"
        "## Zero Clutter (quality gates)\n\n"
        "Everything built here follows [Zero Clutter](https://github.com/prithvi-zeta/zero-clutter): "
        "Bhavin's Design for Delight principles, the checklist, the six gates (G1 spec, G2 design, "
        "G3 build, G4 PR, G5 first use, G6 release) and the house rules. "
        "How each gate runs in this repo is in [zero-clutter.md](zero-clutter.md).\n\n"
        "- New work from a ticket, doc or Loom: run `spec-check` first; build nothing until "
        "Bhavin's blocker questions are answered.\n"
        "- Every change: run `build-gate` (quick) before showing anyone.\n"
        "- Before merge: `build-gate` (full); attach the report to the PR.\n"
        "- Any review feedback: run `feedback-intake` so it becomes a house rule.\n"
        f"{AGENTS_END}\n"
    )


def adopt(project: pathlib.Path, undo: bool) -> list:
    notes = []
    if not project.is_dir():
        return [f"{project} is not a folder."]
    files = {
        project / ".github" / "pull_request_template.md": (ROOT / "templates" / "pull_request_template.md").read_text(encoding="utf-8"),
        project / "zero-clutter.md": (ROOT / "templates" / "project-adapter.md").read_text(encoding="utf-8"),
    }
    for path, text in files.items():
        if undo:
            if path.is_file() and marked(path):
                path.unlink()
                notes.append(f"removed {path}")
        elif path.exists() and not marked(path):
            notes.append(f"{path} exists and isn't ours. Left alone; add the Zero Clutter parts by hand.")
        elif path.exists():
            notes.append(f"{path} kept (already ours; edit it freely)")
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")
            notes.append(f"wrote {path}")
    agents = project / "AGENTS.md"
    current = agents.read_text(encoding="utf-8") if agents.is_file() else ""
    block = re.compile(re.escape(AGENTS_START) + r".*?" + re.escape(AGENTS_END) + r"\n?", re.S)
    if undo:
        if block.search(current):
            agents.write_text(block.sub("", current), encoding="utf-8")
            notes.append(f"removed the Zero Clutter section from {agents}")
    else:
        updated = block.sub(agents_section(), current) if block.search(current) else (
            current + ("\n" if current and not current.endswith("\n\n") else "") + agents_section()
        )
        if updated != current:
            agents.write_text(updated, encoding="utf-8")
            notes.append(f"updated {agents}")
    return notes


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--tools", help="comma-separated: claude, cursor, codex, copilot (default: all found)")
    parser.add_argument("--link", action="store_true", help="link skills to this repo instead of copying")
    parser.add_argument("--force", action="store_true", help="replace skills or commands this script didn't write")
    parser.add_argument("--project", type=pathlib.Path, help="also adopt Zero Clutter in this repo")
    parser.add_argument("--uninstall", action="store_true", help="remove what this script installed")
    args = parser.parse_args(argv)

    known = tools()
    wanted = [t.strip() for t in args.tools.split(",")] if args.tools else list(known)
    unknown = [t for t in wanted if t not in known]
    if unknown:
        parser.error("unknown tool: " + ", ".join(unknown))
    notes, found = [], 0
    for key in wanted:
        tool = known[key]
        if not tool["present"]:
            if args.tools:
                notes.append(f"{tool['label']}: not found on this machine. Skipped.")
            continue
        found += 1
        for name, src in skills().items():
            notes += uninstall_skill(tool, name) if args.uninstall else install_skill(tool, name, src, args.link, args.force)
    if args.project:
        notes += adopt(args.project.expanduser().resolve(), args.uninstall)
    if not found and not args.project:
        print("No supported agent tool found (Claude Code, Cursor, Codex, GitHub Copilot).")
        return 1
    print("\n".join(notes) if notes else "Nothing to do.")
    if not args.uninstall and found:
        print("\nRestart your agent. Commands: /spec-check /build-gate /first-use /feedback-intake /delight-police")
    return 0


if __name__ == "__main__":
    sys.exit(main())
