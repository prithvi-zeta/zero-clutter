#!/usr/bin/env python3
"""Zero Clutter CI gate: read SARIF reports, print the short summary, fail on blockers.

  python3 gate.py .zero-clutter/reports/            # every *.sarif in the folder
  python3 gate.py report.sarif --github             # also GitHub annotations
  python3 gate.py report.sarif --max-major 0        # also fail on majors

Exit 1 when any finding is blocking (level "error" with kind "fail" or
"review"), when majors exceed --max-major, or when no report is found. Exit 0
otherwise. Python 3.9+, standard library only.
"""
from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys

SEVERITY = {"error": "🔴 blocking", "warning": "🟠 major", "note": "🟡 minor"}
VERDICT = {
    "PASS": "✅ PASS",
    "FAIL": "❌ FAIL",
    "READY": "🟢 READY",
    "OPEN": "🟡 OPEN",
}


def cell(value) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ").strip()


def count_cell(emoji: str, n) -> str:
    return f"{emoji} {n}"


def reports(paths: list[str]) -> list[pathlib.Path]:
    found = []
    for raw in paths:
        p = pathlib.Path(raw)
        found += sorted(p.glob("*.sarif")) if p.is_dir() else ([p] if p.is_file() else [])
    return found


def where(result: dict) -> str:
    places = []
    for loc in result.get("locations", []):
        phys = loc.get("physicalLocation", {})
        uri = phys.get("artifactLocation", {}).get("uri")
        line = phys.get("region", {}).get("startLine")
        if uri:
            places.append(f"{uri}:{line}" if line else uri)
        places += [l["name"] for l in loc.get("logicalLocations", []) if l.get("name")]
    if not places:
        return ""
    more = f" +{len(places) - 2}" if len(places) > 2 else ""
    return ", ".join(places[:2]) + more


def split(text: str) -> tuple[str, str]:
    """ "<what>. Fix: <fix>" (or Ask: / Next:) -> (what, fix). """
    parts = re.split(r" (?:Fix|Ask|Next): ", text, maxsplit=1)
    return parts[0].rstrip("."), (parts[1].rstrip(".") if len(parts) > 1 else "")


def annotate(result: dict, github: bool) -> None:
    if not github or result.get("level") not in ("error", "warning"):
        return
    loc = (result.get("locations") or [{}])[0].get("physicalLocation", {})
    file = loc.get("artifactLocation", {}).get("uri")
    line = loc.get("region", {}).get("startLine")
    anchor = (f" file={file}" + (f",line={line}" if line else "")) if file else ""
    level = "error" if result.get("level") == "error" else "warning"
    print(f"::{level}{anchor}::{result.get('ruleId', '')} {result.get('message', {}).get('text', '')}")


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("paths", nargs="+", help="SARIF files or folders")
    parser.add_argument("--github", action="store_true", help="print GitHub Actions annotations")
    parser.add_argument("--max-major", type=int, default=None, help="fail when majors exceed this")
    args = parser.parse_args(argv)

    files = reports(args.paths)
    if not files:
        print("Zero Clutter gate: no SARIF report found. Run zero-clutter in pr mode first.")
        return 1

    blocking = major = 0
    for path in files:
        data = json.loads(path.read_text(encoding="utf-8"))
        for run in data.get("runs", []):
            props = run.get("properties", {})
            rules = {r["id"]: r for r in run.get("tool", {}).get("driver", {}).get("rules", [])}
            results = run.get("results", [])
            count = lambda k: sum(1 for r in results if r.get("kind") == k)
            sev = lambda s: sum(1 for r in results if r.get("kind") in ("fail", "review") and r.get("level") == s)
            # Everything that was judged, i.e. all but n/a and suggestions.
            checked = len(results) - count("notApplicable") - count("informational")
            verdict = VERDICT.get(props.get("verdict", ""), props.get("verdict", "?"))
            passed = f"{count('pass')}/{checked}"
            print("| Gate | Subject | Verdict | Blocking | Major | Minor | Pending | Passed | N/A |")
            print("| --- | --- | --- | --- | --- | --- | --- | --- | --- |")
            print(
                f"| {cell(props.get('mode', '?'))} ({cell(props.get('gate', '?'))}) | "
                f"{cell(props.get('subject', path.name))} | {cell(verdict)} | "
                f"{count_cell('🔴', sev('error'))} | {count_cell('🟠', sev('warning'))} | "
                f"{count_cell('🟡', sev('note'))} | {count_cell('⏳', count('open'))} | "
                f"{count_cell('✅', passed)} | {count_cell('➖', count('notApplicable'))} |"
            )
            order = {"error": 0, "warning": 1, "note": 2, "none": 3}
            ranked = sorted(results, key=lambda r: order.get(r.get("level", "none"), 3))
            rows = []
            number = 0
            for kind, kind_label in (("fail", "🔧 Fix"), ("review", "🤔 Decide"), ("informational", "💡 Suggest")):
                for r in [item for item in ranked if item.get("kind") == kind]:
                    number += 1
                    rule = rules.get(r.get("ruleId"), {})
                    what, fix = split(r.get("message", {}).get("text", ""))
                    rows.append((
                        str(number), kind_label, r.get("ruleId", ""), rule.get("name", ""),
                        SEVERITY.get(r.get("level"), "🟡 minor"), what, where(r), fix,
                    ))
                    annotate(r, args.github)
            for r in [item for item in ranked if item.get("kind") == "open"]:
                rule = rules.get(r.get("ruleId"), {})
                what, fix = split(r.get("message", {}).get("text", ""))
                rows.append((
                    "", "⏳ Check", r.get("ruleId", ""), rule.get("name", ""),
                    "⏳ pending", what, where(r), fix,
                ))
            if rows:
                print()
                print("| # | Kind | ID | Principle | Severity | What's wrong | Where | Fix |")
                print("| --- | --- | --- | --- | --- | --- | --- | --- |")
                for row in rows:
                    print("| " + " | ".join(cell(part) for part in row) + " |")
            print()
            blocking += sev("error")
            major += sev("warning")

    if blocking:
        print(f"Gate: ❌ FAIL · {blocking} blocking")
        return 1
    if args.max_major is not None and major > args.max_major:
        print(f"Gate: ❌ FAIL · {major} major (max {args.max_major})")
        return 1
    print("Gate: ✅ PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
