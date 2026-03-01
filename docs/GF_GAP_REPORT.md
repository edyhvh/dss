# Deadseascrolls → Google Fonts Gap Report

Date: 2026-03-01

## Ready / Passed

- Required submission files exist:
  - `OFL.txt`
  - `METADATA.pb`
  - `DESCRIPTION.en_us.html`
  - `Deadseascrolls-Regular.ttf`
- OFL first-line copyright is concrete and placeholders were removed.
- Font naming matches metadata values:
  - family: Deadseascrolls
  - subfamily: Regular
  - full: Deadseascrolls Regular
  - postscript: Deadseascrolls-Regular
- Basic technical checks:
  - `usWeightClass = 400`
  - `fsType = 0` (installable embedding)
- Hebrew scope check:
  - Hebrew block present
  - niqqud codepoints U+0591..U+05C7 present: **0**

## Blocking gap

- Google Fonts Latin Core support is incomplete.
- Measured against official `GF_Latin_Core.txt` glyphset:
  - Required glyph names: 324
  - Present: 100
  - Missing: 224

This is likely to fail onboarding QA in its current state.

## What you can do today

1. Open the Add Font issue now (use `docs/ADD_FONT_ISSUE_DRAFT.md`) and be explicit this is Hebrew-first, no-niqqud release.
2. Keep Latin Core checkbox unticked for now, request guidance/exception in the issue.
3. If reviewer requests strict compliance, expand Latin Core and resubmit.

## PR-ready package prepared

- `legacy/submission/ofl/deadseascrolls/` contains all required family files for `google/fonts` repo layout.
