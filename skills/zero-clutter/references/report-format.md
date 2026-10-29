# Report format

Zero Clutter answers in a shape people scan in seconds, and writes the same
findings as a file machines parse. It borrows from two standards:

- **[Conventional Comments](https://conventionalcomments.org/):** every
  finding has a kind (issue, question, suggestion) and how much it matters
  (blocking, major, minor).
- **[SARIF 2.1.0](https://docs.oasis-open.org/sarif/sarif/v2.1.0/sarif-v2.1.0.html):**
  every finding has a rule ID, a level, a location and a fix, so CI and code
  hosts can read it.

## The chat answer

One framed block in a `text` code block:

```text
╭─ 🧹 Zero Clutter ──────────────────────────────────────────────────────
│  App Onboarding Option 3 · design (G2) · Flutter · 5 stories
│
│  ❌ FAIL   🔴 2 blocking   🟠 1 major   🟡 1 minor   ⏳ 2 to check   ✅ 7/13 passed
│
├─ 🔧 Fix ───────────────────────────────────────────────────────────────
│
│  🔴 F1  CONS-07 Consistency
│         📍 "3%" hard-coded in 6 places
│            pitch_v3.dart, onboarding_pitch_screen.dart:56 +4
│         🎯 One APY constant, used everywhere
│
│  🟠 F2  HIER-05 Hierarchy
│         📍 White text 2.6:1 on amber, 1.9:1 where trails cross "APY" (needs 3:1)
│            stories 1 and 3 › statement
│         🎯 Darker stripes base behind the text
│
├─ 🤔 Decide · Bhavin ───────────────────────────────────────────────────
│
│  🔴 D1  PROC-07 Process
│         📍 The frames have 8 screens; Option 3 shows 5
│         ❓ Keep 5? · recommend: yes
│
│  🟡 D2  WORD-05 Words
│         📍 "upto" in the frames' copy
│         ❓ Change to "up to"? · recommend: yes
│
├─ ⏳ Check ─────────────────────────────────────────────────────────────
│
│  •  SENSE-02 Senses · haptics and feel → on the sim
│  •  ZCL-01 Zero Cognitive Load · first-run screens → first-use test (G5)
│
├─ ✅ Keep ──────────────────────────────────────────────────────────────
│
│  One statement per screen · sharp vector glyphs · a colour per guarantee
│
├─ 👉 Next ──────────────────────────────────────────────────────────────
│
│  Fix F1 and F2, then send D1 and D2 to Bhavin.
╰────────────────────────────────────────────────────────────────────────
```

### Key

| Symbol | Means |
| --- | --- |
| ✅ PASS · ❌ FAIL | Verdict for design, build, pr, first-use |
| 🟢 READY · 🟡 OPEN | Verdict for spec |
| 🔴 · 🟠 · 🟡 | blocking · major · minor |
| 🔧 Fix | The team fixes it (SARIF `issue`) |
| 🤔 Decide | The approver decides (`question`) |
| 💡 Suggest | Optional, nobody asked (`suggestion`) |
| ⏳ Check | Pending: a device, a person, a capture (`pending`) |
| ✅ Keep | What works (`keep`) |
| 👉 Next | The one thing to do now |
| 📍 · 🎯 · ❓ | what and where · the fix · the question |

### Why it's built this way

- **A code block** looks the same in every terminal, IDE, chat and on GitHub,
  and keeps the indentation, so the eye can run down the dots and numbers.
- **Labelled dividers** (`├─ 🔧 Fix ──`) give each section its own block.
- **A left border only:** emoji and long paths have uneven widths, so a right
  border would never line up.
- **Per-section numbers (F1, D1)** let people answer "fix F1, send D1".
- **One emoji per role**, used the same way every time, so they work as icons,
  not decoration.

### Principle names

| ID prefix | Name |
| --- | --- |
| ZCL | Zero Cognitive Load |
| CLUT | Clutter |
| WORD | Words |
| DEF | Defaults |
| PROG | One context |
| HIER | Hierarchy |
| FB | Feedback |
| CONS | Consistency |
| MENT | Familiar |
| CHOICE | Choices |
| SENSE | Senses |
| UNIQ | Unique design |
| SCI | Science of delight |
| SURF | Surfaces |
| WEB | Web |
| PROC | Process |
| HR | House rule |
| P | Project rule |

## The SARIF file

Written to `.zero-clutter/reports/<date>-<name>.sarif` in pr mode, or when
asked. One run, one tool, one result per finding and per pass. Minimal shape:

```json
{
  "$schema": "https://json.schemastore.org/sarif-2.1.0.json",
  "version": "2.1.0",
  "runs": [{
    "tool": { "driver": {
      "name": "zero-clutter",
      "version": "0.4.0",
      "informationUri": "https://github.com/prithvi-zeta/zero-clutter",
      "rules": [{
        "id": "HIER-05",
        "name": "Hierarchy",
        "shortDescription": { "text": "Every text run meets measured contrast against its worst real background" },
        "defaultConfiguration": { "level": "warning" }
      }]
    }},
    "properties": { "mode": "design", "gate": "G2", "verdict": "FAIL", "subject": "Onboarding Option 3" },
    "results": [{
      "ruleId": "HIER-05",
      "kind": "fail",
      "level": "warning",
      "message": { "text": "White text 2.6:1 on amber (needs 3:1). Fix: darker base behind text." },
      "locations": [{
        "physicalLocation": { "artifactLocation": { "uri": "lib/features/onboarding_app/widgets/pitch_v3.dart" }, "region": { "startLine": 120 } },
        "logicalLocations": [{ "name": "story 3 › statement" }]
      }],
      "properties": { "label": "issue", "severity": "major" }
    }]
  }]
}
```

### Mapping

| Chat section · dot | SARIF `kind` | SARIF `level` |
| --- | --- | --- |
| 🔧 Fix · 🔴 | `fail` | `error` |
| 🔧 Fix · 🟠 | `fail` | `warning` |
| 🔧 Fix · 🟡 | `fail` | `note` |
| 🤔 Decide | `review` | from the dot, as above |
| 💡 Suggest | `informational` | `note` |
| ⏳ Check | `open` | `none` |
| a passed check | `pass` | `none` |
| n/a | `notApplicable` | `none` |

- `properties.label` (`issue`, `question`, `suggestion`, `pending`) and
  `properties.severity` keep the chat meaning.
- `message.text` is `<what>. Fix: <fix>` for issues and suggestions,
  `<what>. Ask: <question> (recommend: <x>)` for questions, and
  `<what>. Next: <step>` for pending. Add SARIF `fixes` only for an exact text change.
- A UI finding without a file uses `logicalLocations` only.
- The CI gate (`scripts/gate.py`) fails the build on any `error` with kind
  `fail` or `review`, and prints the same grouped layout as plain text.
