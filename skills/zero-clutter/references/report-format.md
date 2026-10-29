# Report format

Zero Clutter answers in a shape that people scan and machines parse. It
borrows from two standards:

- **[Conventional Comments](https://conventionalcomments.org/):** every
  finding starts with a label word (`issue`, `question`, `suggestion`) and a
  decoration for how much it matters.
- **[SARIF 2.1.0](https://docs.oasis-open.org/sarif/sarif/v2.1.0/sarif-v2.1.0.html):**
  every finding has a rule ID, a level, a location and a fix, so CI and code
  hosts can read it.

## The chat answer

```text
Zero Clutter · design (G2) · Onboarding Option 3 · FAIL
2 blocking · 1 major · 1 minor · 2 pending · 7/13 passed · 2 n/a

issue (blocking) CONS-07 Consistency · "3%" hard-coded at pitch_v3.dart:46, pitch_screen.dart:56 +4 → one APY constant
issue (major) HIER-05 Hierarchy · white text 2.6:1 on amber at story 3 › statement (needs 3:1) → darker base behind text
question (blocking) PROC-07 Process · frames have 8 screens, we show 5 → keep 5? (recommend: yes)
question (minor) WORD-05 Words · "upto" vs "up to" in the frames' copy → fix the spelling? (recommend: yes)
pending SENSE-02 Senses · haptics and feel can't be judged from stills → check on a device
pending ZCL-01 Zero Cognitive Load · first-run screens need a person → run first-use (G5)
keep: one statement per screen · sharp vector glyphs · a colour per guarantee

Next: one APY constant and a darker text base, then send the 2 questions to the approver.
```

### Line grammar

```
<label> [(<severity>)] <ID> <Principle> · <what> [at <where>] → <fix or next step>
```

| Part | Values |
| --- | --- |
| label | `issue`, `question`, `suggestion`, `pending`, `keep` |
| severity | `blocking`, `major`, `minor` (from the item); omitted on `pending` and `keep` |
| ID | a checklist ID (`HIER-05`), a shared house rule (`HR-03`) or a project rule (`P-02`) |
| Principle | from the table below |
| where | `file:line`, `screen › element`, or `R#` for a spec row; first two, then `+n` |

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

| Chat | SARIF `kind` | SARIF `level` |
| --- | --- | --- |
| `issue (blocking)` | `fail` | `error` |
| `issue (major)` | `fail` | `warning` |
| `issue (minor)` | `fail` | `note` |
| `question` | `review` | from severity, as above |
| `suggestion` | `informational` | `note` |
| `pending` | `open` | `none` |
| a passed check | `pass` | `none` |
| n/a | `notApplicable` | `none` |

- `properties.label` and `properties.severity` keep the chat words.
- `message.text` is `<what>. Fix: <fix>` for issues and suggestions,
  `<what>. Ask: <question> (recommend: <x>)` for questions, and
  `<what>. Next: <step>` for pending. Add SARIF `fixes` only for an exact text change.
- A UI finding without a file uses `logicalLocations` only.
- The CI gate (`scripts/gate.py`) fails the build on any `error` with kind
  `fail` or `review`, and prints the chat summary.
