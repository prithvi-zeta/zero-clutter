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

DOT = {"error": "🔴", "warning": "🟠", "note": "🟡"}
RULE = "─" * 48


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
    return " · " + ", ".join(places[:2]) + more


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
            verdict = props.get("verdict", "?")
            badge = {"PASS": "✅ PASS", "FAIL": "❌ FAIL", "READY": "🟢 READY", "OPEN": "🟡 OPEN"}.get(verdict, verdict)
            print(f"🧹 Zero Clutter · {props.get('subject', path.name)}")
            print(f"{props.get('mode', '?')} ({props.get('gate', '?')})")
            print()
            print(f"{badge} · 🔴 {sev('error')} blocking · 🟠 {sev('warning')} major · 🟡 {sev('note')} minor · "
                  f"⏳ {count('open')} to check · ✅ {count('pass')}/{checked} passed")
            print()
            order = {"error": 0, "warning": 1, "note": 2, "none": 3}
            ranked = sorted(results, key=lambda r: order.get(r.get("level", "none"), 3))
            sections = (("🔧 Fix", "fail", "F", "✏️"), ("🤔 Decide", "review", "D", "💬"), ("💡 Suggest", "informational", "S", "💡"))
            for heading, kind, prefix, mark in sections:
                group = [r for r in ranked if r.get("kind") == kind]
                if not group:
                    continue
                print(f"{RULE}\n{heading}\n")
                for n, r in enumerate(group, 1):
                    rule = rules.get(r.get("ruleId"), {})
                    what, fix = split(r.get("message", {}).get("text", ""))
                    print(f"{DOT.get(r.get('level'), '🟡')} {prefix}{n} · {r.get('ruleId', '')} {rule.get('name', '')}")
                    print(f"   📍 {what}{where(r)}")
                    if fix:
                        print(f"   {mark} {fix}")
                    print()
                    annotate(r, args.github)
            pending = [r for r in ranked if r.get("kind") == "open"]
            if pending:
                print(f"{RULE}\n⏳ Check\n")
                for r in pending:
                    rule = rules.get(r.get("ruleId"), {})
                    what, fix = split(r.get("message", {}).get("text", ""))
                    print(f"   • {r.get('ruleId', '')} {rule.get('name', '')} · {what}" + (f" → {fix}" if fix else ""))
                print()
            print(RULE)
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
