# Deadseascrolls Submission Tracker

Date: 2026-03-01

## Source docs summarized

- `docs/ADD_FONT_ISSUE_DRAFT.md`
- `docs/Deadseascrolls_GF_Summary_2026-03-01.md`
- `docs/GF_GAP_REPORT.md`
- `docs/TODAY_UPLOAD_CHECKLIST.md`

## Ownership

- Co-owners/co-authors of the font project: Jhonny and Adi Greenberg.
- Ownership is reflected in `OFL.txt` and `METADATA.pb`.

## Current status

### Completed

- Required family files are prepared:
  - `Deadseascrolls-Regular.ttf`
  - `METADATA.pb`
  - `DESCRIPTION.en_us.html`
  - `OFL.txt`
- Naming/metadata alignment verified:
  - Family: Deadseascrolls
  - Subfamily: Regular
  - PostScript: Deadseascrolls-Regular
- Technical checks noted as passed:
  - `usWeightClass = 400`
  - `fsType = 0`
- Script scope check noted as passed:
  - Hebrew present
  - No niqqud codepoints (U+0591..U+05C7)

### In progress / open

- Google Fonts Latin Core coverage is incomplete:
  - Required: 324 glyph names
  - Present: 100
  - Missing: 224
- This is the primary blocker/risk for smooth onboarding QA.

## Directory layout (current)

- Root (`~/dss`) keeps primary submission files.
- `~/dss/docs` stores planning/checklist/report markdown docs.
- `~/dss/legacy` stores files not needed for immediate submission.

## Immediate next steps

1. Open Google Fonts **Add Font** issue using `docs/ADD_FONT_ISSUE_DRAFT.md`.
2. State clearly: Hebrew-first release, no niqqud by design, current Latin Core gap.
3. Attach specimen image (currently in `legacy/Deadseascrolls.jpg`).
4. Ask reviewers whether onboarding can proceed now or requires full Latin Core first.

## After reviewer feedback

- If exception/guidance allows: proceed with submission package as-is.
- If strict compliance is required: expand glyph coverage toward full Latin Core, then resubmit.

## Submission package currently in root

- `Deadseascrolls-Regular.ttf`
- `METADATA.pb`
- `DESCRIPTION.en_us.html`
- `OFL.txt`
