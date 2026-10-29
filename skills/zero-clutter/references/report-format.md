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

Grouped under plain headings so it scans in a few seconds, in Markdown so it
renders cleanly in Claude Code, Cursor and chat:

```markdown
**Zero Clutter** · design (G2) · Onboarding Option 3
**FAIL** · 2 blocking · 1 major · 1 minor · 2 pending · 7/13 passed · 2 n/a

**Fix**
1. **CONS-07 Consistency** · blocking
   "3%" hard-coded in 6 places · `pitch_v3.dart:46` +5
   → One APY constant, used everywhere
2. **HIER-05 Hierarchy** · major
   White text 2.6:1 on amber, needs 3:1 · story 3 › statement
   → Darker base behind the text

**Decide** (the approver)
3. **PROC-07 Process** · blocking
   Frames have 8 screens; we show 5
   → Keep 5? (recommend: yes)
4. **WORD-05 Words** · minor
   "upto" in the frames' copy
   → Change to "up to"? (recommend: yes)

**Check**
- **SENSE-02 Senses** · haptics and feel → on a device
- **ZCL-01 Zero Cognitive Load** · first-run screens → first-use test with a person (G5)

**Keep** one statement per screen · sharp vector glyphs · a colour per guarantee

**Next** One APY constant and a darker text base, then send 3 and 4 to the approver.
```

### Headings

| Heading | Holds | Label (SARIF `properties.label`) |
| --- | --- | --- |
| **Fix** | Problems the team fixes | `issue` |
| **Decide** | Spec conflicts, taste calls, missing facts: the approver decides | `question` |
| **Suggest** | Optional improvements nobody asked for | `suggestion` |
| **Check** | Still pending: a device, a person, a capture | `pending` |
| **Keep** | What works (1 to 3 things) | `keep` |

Findings in Fix, Decide and Suggest are numbered across headings. Each is
three lines: **ID Principle** · severity, then what and where, then `→` the
fix. Where is `file:line`, `screen › element` or `R#` for a spec row.

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

| Chat heading · severity | SARIF `kind` | SARIF `level` |
| --- | --- | --- |
| Fix · blocking | `fail` | `error` |
| Fix · major | `fail` | `warning` |
| Fix · minor | `fail` | `note` |
| Decide | `review` | from severity, as above |
| Suggest | `informational` | `note` |
| Check | `open` | `none` |
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
