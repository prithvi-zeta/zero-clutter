#!/usr/bin/env python3
"""Install the Delight Police skill for the agent tools on this machine.

  python3 scripts/install.py                 # copy into each tool found, add /delight-police
  python3 scripts/install.py --link          # link instead of copying (for maintainers)
  python3 scripts/install.py --tools claude,cursor
  python3 scripts/install.py --uninstall

It writes only inside each tool's own folder under your home folder, and marks
what it writes. It never replaces a skill or a command it did not install, and
--uninstall removes only what it marked.

Also removes a prior install named design-for-delight / /delight when present.

Python 3.9 or later, standard library only.
"""
from __future__ import annotations

import argparse
import datetime as dt
import os
import pathlib
import shutil
import sys

HOME = pathlib.Path(os.environ.get("DFD_HOME") or pathlib.Path.home())
# This skill folder (…/delight-police): SKILL.md, principles.md, scripts/
SKILL_SRC = pathlib.Path(__file__).resolve().parent.parent
NAME = "delight-police"
LEGACY_NAME = "design-for-delight"
MARK_FILE = ".installed-by-delight-police"
LEGACY_MARK_FILE = ".installed-by-design-for-delight"
MARK_LINE = "<!-- delight-police install -->"
LEGACY_MARK_LINE = "<!-- design-for-delight install -->"
DESCRIPTION = (
    "Delight Police: review a design screen against Design for Delight principles "
    "(Zero Cognitive Load, Engage the Senses, Purpose-built Unique Design)"
)
HINT = "attach a screen, or describe it"
SKIP = shutil.ignore_patterns("__pycache__", "*.pyc", ".DS_Store", MARK_FILE)

VSCODE_USER = [
    HOME / "Library" / "Application Support" / "Code" / "User",
    HOME / ".config" / "Code" / "User",
    HOME / "AppData" / "Roaming" / "Code" / "User",
]


def vscode_prompts() -> pathlib.Path | None:
    for base in VSCODE_USER:
        if base.is_dir():
            return base / "prompts"
    return None


def tools() -> dict:
    """Each tool: its home folder, whether it is on this machine, where commands go."""
    found = {
        "claude": {
            "label": "Claude Code",
            "home": HOME / ".claude",
            "commands": HOME / ".claude" / "commands",
            "form": "claude",
        },
        "copilot": {
            "label": "GitHub Copilot",
            "home": HOME / ".copilot",
            "commands": vscode_prompts(),
            "form": "copilot",
        },
        "codex": {
            "label": "Codex",
            "home": HOME / ".codex",
            "commands": None,
            "form": None,
        },
        "cursor": {
            "label": "Cursor",
            "home": HOME / ".cursor",
            "commands": HOME / ".cursor" / "commands",
            "form": "cursor",
        },
    }
    for tool in found.values():
        tool["present"] = tool["home"].is_dir()
    found["copilot"]["present"] = found["copilot"]["present"] or vscode_prompts() is not None
    return found


def command_text(form: str, skill: pathlib.Path) -> str:
    body = (
        f"Read `{skill}/SKILL.md` completely and follow it.\n\n"
        f"Run Delight Police: review the design screen the person attached or described\n"
        f"against Design for Delight.\n"
        f"If nothing follows the command, ask them to attach a screenshot, Figma frame, mock,\n"
        f"or short description, and to say who the user is and what the screen is for.\n"
    )
    if form == "claude":
        return (
            f"---\ndescription: {DESCRIPTION}\nargument-hint: \"[{HINT}]\"\n---\n"
            f"{MARK_LINE}\n\n{body}\nWhat the person typed after the command: $ARGUMENTS\n"
        )
    if form == "copilot":
        return (
            f"---\nname: delight-police\ndescription: {DESCRIPTION}.\n"
            f"argument-hint: \"{HINT}\"\n---\n{MARK_LINE}\n\n{body}"
        )
    return f"# Delight Police\n\n{MARK_LINE}\n\n{DESCRIPTION}.\n\n{body}"


def command_files(tool: dict) -> list:
    if not tool["commands"]:
        return []
    suffix = ".prompt.md" if tool["form"] == "copilot" else ".md"
    return [("delight-police", tool["commands"] / ("delight-police" + suffix))]


def legacy_command_files(tool: dict) -> list:
    if not tool["commands"]:
        return []
    suffix = ".prompt.md" if tool["form"] == "copilot" else ".md"
    return [tool["commands"] / ("delight" + suffix)]


def is_ours(dest: pathlib.Path) -> bool:
    """True for a copy this script made, or a link to this skill folder."""
    if dest.is_symlink():
        return (dest / "SKILL.md").is_file() and dest.resolve().name == NAME
    return (dest / MARK_FILE).is_file()


def is_legacy(dest: pathlib.Path) -> bool:
    if dest.is_symlink():
        try:
            return dest.resolve().name == LEGACY_NAME
        except OSError:
            return False
    return (dest / LEGACY_MARK_FILE).is_file()


def marked(path: pathlib.Path) -> bool:
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return False
    return MARK_LINE in text or LEGACY_MARK_LINE in text


def remove(dest: pathlib.Path) -> None:
    if dest.is_symlink() or dest.is_file():
        dest.unlink()
    elif dest.is_dir():
        shutil.rmtree(dest)


def clear_legacy(tool: dict) -> list:
    notes = []
    dest = tool["home"] / "skills" / LEGACY_NAME
    if dest.exists() or dest.is_symlink():
        if is_legacy(dest) or (dest / LEGACY_MARK_FILE).is_file():
            remove(dest)
            notes.append(f"{tool['label']}: removed legacy {dest}")
        elif not is_ours(dest):
            # Still remove marked legacy installs; leave unknown folders alone
            pass
    for path in legacy_command_files(tool):
        if path.is_file() and marked(path):
            path.unlink()
            notes.append(f"{tool['label']}: removed legacy {path}")
    return notes


def install(tool: dict, link: bool, force: bool) -> list:
    notes = clear_legacy(tool)
    if not SKILL_SRC.is_dir() or not (SKILL_SRC / "SKILL.md").is_file():
        return notes + [f"Missing skill at {SKILL_SRC}. Aborting."]
    dest = tool["home"] / "skills" / NAME
    if (dest.exists() or dest.is_symlink()) and not is_ours(dest) and not force:
        return notes + [
            f"{tool['label']}: {dest} exists and was not installed by this script. "
            f"Left alone. Use --force to replace it."
        ]
    if dest.is_symlink() and dest.resolve() == SKILL_SRC and link:
        notes.append(f"{tool['label']}: already linked at {dest}")
    else:
        remove(dest)
        dest.parent.mkdir(parents=True, exist_ok=True)
        if link:
            dest.symlink_to(SKILL_SRC, target_is_directory=True)
        else:
            shutil.copytree(SKILL_SRC, dest, ignore=SKIP)
            (dest / MARK_FILE).write_text(
                f"Installed from {SKILL_SRC} on {dt.date.today().isoformat()}.\n",
                encoding="utf-8",
            )
        notes.append(f"{tool['label']}: skill {'linked' if link else 'copied'} to {dest}")
    written = []
    for name, path in command_files(tool):
        if path.exists() and not marked(path) and not force:
            notes.append(f"{tool['label']}: {path} exists and is not ours. Left alone.")
            continue
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(command_text(tool["form"], dest), encoding="utf-8")
        written.append("/" + name)
    if written:
        notes.append(f"{tool['label']}: commands {' and '.join(written)} added")
    elif not tool["commands"]:
        notes.append(
            f'{tool["label"]}: no slash command here. '
            f'Say "run delight police on this", or ask in your own words.'
        )
    return notes


def uninstall(tool: dict) -> list:
    notes = clear_legacy(tool)
    dest = tool["home"] / "skills" / NAME
    if dest.exists() or dest.is_symlink():
        if is_ours(dest):
            remove(dest)
            notes.append(f"{tool['label']}: removed {dest}")
        else:
            notes.append(
                f"{tool['label']}: {dest} was not installed by this script. Left alone."
            )
    for _name, path in command_files(tool):
        if path.is_file() and marked(path):
            path.unlink()
            notes.append(f"{tool['label']}: removed {path}")
    return notes


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        description="Install the Delight Police skill for the agent tools on this machine."
    )
    parser.add_argument(
        "--tools",
        help="comma-separated: claude, copilot, codex, cursor (default: every tool found)",
    )
    parser.add_argument(
        "--link",
        action="store_true",
        help="link to this skill folder instead of copying it",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="replace a skill or command this script did not install",
    )
    parser.add_argument(
        "--uninstall",
        action="store_true",
        help="remove what this script installed",
    )
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
        notes += uninstall(tool) if args.uninstall else install(tool, args.link, args.force)
    if not found:
        print(
            "No supported agent tool found in your home folder "
            "(Claude Code, GitHub Copilot, Codex, Cursor)."
        )
        return 1
    print("\n".join(notes) if notes else "Nothing to remove.")
    if not args.uninstall:
        print(
            '\nRestart your agent, then type /delight-police or say '
            '"run delight police on this".'
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
