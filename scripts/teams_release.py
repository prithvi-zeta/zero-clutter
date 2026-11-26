#!/usr/bin/env python3
"""Post a version's release notes to a Microsoft Teams channel.

Reads release-notes/<version>.md (Added, Updated, Based on, in plain words),
or the version's CHANGELOG.md section when there is no note, and sends it as
an Adaptive Card to a Teams Workflows webhook ("Post to a channel when a
webhook request is received"). The webhook URL comes from TEAMS_WEBHOOK_URL.

  python3 scripts/teams_release.py              # version from plugin.json
  python3 scripts/teams_release.py 0.6.0        # a given version
  python3 scripts/teams_release.py --dry-run    # print the card, send nothing
"""

import json
import os
import re
import sys
import urllib.request
from datetime import date as Date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPO_URL = "https://github.com/prithvi-zeta/zero-clutter"


def current_version():
    return json.loads((ROOT / ".claude-plugin/plugin.json").read_text())["version"]


def bullets(lines):
    """Turn markdown list lines into (depth, text), joining wrapped lines."""
    items = []
    for line in lines:
        match = re.match(r"^( *)- (.*)", line)
        if match:
            items.append([len(match.group(1)) // 2, match.group(2).strip()])
        elif line.strip() and items:
            items[-1][1] += " " + line.strip()
    # Teams markdown has no inline code, so drop the backticks.
    return [(depth, text.replace("`", "")) for depth, text in items]


def changelog_section(version):
    """Return (date, text) for a version's CHANGELOG.md section."""
    text = (ROOT / "CHANGELOG.md").read_text()
    match = re.search(
        rf"^## {re.escape(version)}(?: — (\S+))?\s*$(.*?)(?=^## |\Z)",
        text,
        re.M | re.S,
    )
    if not match:
        sys.exit(f"No CHANGELOG.md entry for {version}")
    return match.group(1), match.group(2)


def sections(version, changelog_text):
    """Return [(heading, bullets)]: the release note if there is one, else the changelog."""
    note = ROOT / "release-notes" / f"{version}.md"
    if not note.exists():
        return [(None, bullets(changelog_text.splitlines()))]
    parts = re.split(r"^## (.+)$", note.read_text(), flags=re.M)[1:]
    return [(heading.strip(), bullets(body.splitlines()))
            for heading, body in zip(parts[::2], parts[1::2])]


def list_blocks(items):
    """Top-level bullets as TextBlocks, with nested bullets indented under them."""
    blocks, run = [], []

    def flush():
        if run:
            depth = run[0][0]
            block = {"type": "TextBlock", "wrap": True, "spacing": "Small",
                     "text": "\n".join(f"- {text}" for _, text in run)}
            if depth:
                block = {"type": "ColumnSet", "spacing": "None", "columns": [
                    {"type": "Column", "width": "16px", "items": []},
                    {"type": "Column", "width": "stretch", "items": [block]},
                ]}
            blocks.append(block)
            run.clear()

    for depth, text in items:
        if run and min(depth, 1) != min(run[0][0], 1):
            flush()
        run.append((depth, text))
    flush()
    return blocks


def card(version, date, groups):
    if date:
        date = Date.fromisoformat(date).strftime("%-d %b %Y")
    heading = f"Zero Clutter {version}" + (f" · {date}" if date else "")
    body = [{"type": "TextBlock", "text": heading, "size": "Large",
             "weight": "Bolder", "wrap": True}]
    for title, items in groups:
        if title:
            body.append({"type": "TextBlock", "text": title, "weight": "Bolder",
                         "spacing": "Medium", "wrap": True})
        body += list_blocks(items)
    return {
        "type": "message",
        "attachments": [
            {
                "contentType": "application/vnd.microsoft.card.adaptive",
                "content": {
                    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
                    "type": "AdaptiveCard",
                    "version": "1.4",
                    "msteams": {"width": "Full"},
                    "body": body,
                    "actions": [
                        {"type": "Action.OpenUrl", "title": "Full changelog",
                         "url": f"{REPO_URL}/blob/main/CHANGELOG.md"},
                        {"type": "Action.OpenUrl", "title": "Update the skill",
                         "url": f"{REPO_URL}#install"},
                    ],
                },
            }
        ],
    }


def main():
    args = [a for a in sys.argv[1:] if a != "--dry-run"]
    dry_run = "--dry-run" in sys.argv
    version = args[0] if args else current_version()
    date, changelog_text = changelog_section(version)
    payload = card(version, date, sections(version, changelog_text))

    if dry_run:
        print(json.dumps(payload, indent=2, ensure_ascii=False))
        return
    url = os.environ.get("TEAMS_WEBHOOK_URL")
    if not url:
        sys.exit("TEAMS_WEBHOOK_URL is not set")
    request = urllib.request.Request(
        url,
        data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(request) as response:
        print(f"Posted {version} to Teams ({response.status})")


if __name__ == "__main__":
    main()
