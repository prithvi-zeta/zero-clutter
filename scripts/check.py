#!/usr/bin/env python3
"""Check that Zero Clutter is consistent before a change is released.

  python3 scripts/check.py

Fails (exit 1) when:
  - Delight Police's copy of the principles no longer matches the one in the
    zero-clutter skill,
  - a checklist item has no "Enforces" line, or an ID appears twice,
  - any file points at a checklist ID, house rule or log entry that doesn't
    exist,
  - a log entry names a rule that doesn't exist, or a rule cites no entry,
  - a skill is missing its name or version, the manifests disagree on the
    name or version, or a relative Markdown link doesn't resolve.

Python 3.9 or later, standard library only.
"""
from __future__ import annotations

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
REF = "skills/zero-clutter/references"
errors: list[str] = []


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def words(text: str) -> list[str]:
    """The principles' words only: no markup, list markers or quote styles."""
    head = re.search(r"^#+\s*Zero Cognitive Load\s*$", text, re.M)
    text = text[head.start():] if head else text
    text = re.sub(r"<https?://[^>]+>|https?://\S+", " ", text)
    text = re.sub(r"[’‘]", "'", text)
    text = re.sub(r"[“”]", '"', text)
    text = re.sub(r"^\s*(?:(?:[-*]|\d+\.|[a-z]\.|[ivx]+\.)\s+)+", " ", text, flags=re.M)
    text = re.sub(r"[#*_`>]", " ", text)
    return re.findall(r"[A-Za-z0-9$%'\"]+", text)


# 1. Principles copies match the source of truth.
def principles(rel: str) -> list[str]:
    """The principles' words, without the "Further Reading" pointer (a link,
    worded differently in each copy)."""
    got = words(read(rel))
    if "Further" in got:
        i = got.index("Further")
        got = got[:i] + got[got.index("Engage", i):]
    return got


source = principles(f"{REF}/principles/design-for-delight-principles.md")
for copy in ["skills/delight-police/principles.md"]:
    got = principles(copy)
    if got != source:
        at = next((i for i, (a, b) in enumerate(zip(got, source)) if a != b), min(len(got), len(source)))
        errors.append(
            f"{copy} differs from principles/ near word {at}: "
            f"{' '.join(got[at:at + 8])!r} vs {' '.join(source[at:at + 8])!r}"
        )

# 2. Checklist items.
items_text = read(f"{REF}/checklist-items.md")
ids = re.findall(r"^- \*\*([A-Z]+-\d+)\*\*", items_text, re.M)
if len(ids) != len(set(ids)):
    dupes = sorted({i for i in ids if ids.count(i) > 1})
    errors.append(f"checklist/items.md: duplicate IDs {dupes}")
for block in re.split(r"(?=^- \*\*[A-Z]+-\d+\*\*)", items_text, flags=re.M)[1:]:
    item = re.match(r"- \*\*([A-Z]+-\d+)\*\*", block).group(1)
    if "Enforces:" not in block:
        errors.append(f"checklist/items.md: {item} has no Enforces line")
known_ids = set(ids)
prefixes = {i.split("-")[0] for i in ids}

# 3. House rules and log entries.
rules_text = read(f"{REF}/house-rules.md")
log_text = read("examples/ryzedesign/feedback-log.md")
rules = set(re.findall(r"^### (HR-\d+)", rules_text, re.M))
entries = set(re.findall(r"^\| ([FD]-\d{3}) \|", log_text, re.M))

for m in re.finditer(r"^\| ([FD]-\d{3}) \|.*\| (HR-\d+(?:, HR-\d+)*) \|$", log_text, re.M):
    for rule in m.group(2).split(", "):
        if rule not in rules:
            errors.append(f"example log: {m.group(1)} names {rule}, which doesn't exist")
for block in re.split(r"(?=^### HR-\d+)", rules_text, flags=re.M)[1:]:
    rule = re.match(r"### (HR-\d+)", block).group(1)
    cited = re.findall(r"\b([FD]-\d{3})\b", block)
    if not cited:
        errors.append(f"house rules: {rule} cites no log entry")

# 4. Every reference in every doc resolves.
id_pattern = re.compile(r"\b(" + "|".join(sorted(prefixes)) + r")-(\d{2})\b")
for path in sorted(ROOT.rglob("*.md")):
    rel = path.relative_to(ROOT).as_posix()
    if rel.startswith(".git/") or rel == f"{REF}/checklist-items.md":
        continue
    text = path.read_text(encoding="utf-8")
    for m in id_pattern.finditer(text):
        ref = f"{m.group(1)}-{m.group(2)}"
        if ref not in known_ids:
            errors.append(f"{rel}: {ref} is not in the checklist items")
    for ref in re.findall(r"\b(HR-\d{2})\b", text):
        if ref not in rules:
            errors.append(f"{rel}: {ref} is not in the shared house rules")
    for ref in re.findall(r"\b([FD]-\d{3})\b", text):
        if ref not in entries:
            errors.append(f"{rel}: {ref} is not in the example log")

# 5. Skills, and one name and version everywhere.
import json

versions = {}
for skill in sorted(p for p in (ROOT / "skills").iterdir() if p.is_dir()):
    md = skill / "SKILL.md"
    if not md.is_file():
        errors.append(f"{skill.relative_to(ROOT)}: no SKILL.md")
        continue
    head = md.read_text(encoding="utf-8").split("---")[1]
    for field in ("name:", "version:"):
        if field not in head:
            errors.append(f"{md.relative_to(ROOT)}: frontmatter has no {field}")
    if skill.name == "zero-clutter":
        m = re.search(r'version:\s*"?([\d.]+)', head)
        versions["skills/zero-clutter/SKILL.md"] = m.group(1) if m else None
for manifest in [".claude-plugin/plugin.json", ".cursor-plugin/plugin.json", "gemini-extension.json"]:
    data = json.loads(read(manifest))
    if data.get("name") != "zero-clutter":
        errors.append(f"{manifest}: name is {data.get('name')!r}, not 'zero-clutter'")
    versions[manifest] = data.get("version")
if len(set(versions.values())) != 1:
    errors.append(f"versions differ: {versions}")

# 6. Every relative link in a Markdown file points at a file that exists.
for path in sorted(ROOT.rglob("*.md")):
    rel = path.relative_to(ROOT).as_posix()
    if rel.startswith(".git/"):
        continue
    for target in re.findall(r"\]\(([^)#\s]+)(?:#[^)]*)?\)", path.read_text(encoding="utf-8")):
        if re.match(r"[a-z]+:", target):
            continue
        if not (path.parent / target).exists():
            errors.append(f"{rel}: link to {target} doesn't resolve")

if errors:
    print("Zero Clutter check failed:\n  " + "\n  ".join(errors))
    sys.exit(1)
print(
    f"Zero Clutter check passed: {len(known_ids)} checklist items, {len(rules)} house rules, "
    f"{len(entries)} example log entries, principles in sync, version {versions['.claude-plugin/plugin.json']}."
)
