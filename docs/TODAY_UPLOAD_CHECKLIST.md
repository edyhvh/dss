# Deadseascrolls Google Fonts Submission Checklist (Today)

## 1) Final technical checks

- [x] `OFL.txt` first line uses real copyright string
- [x] No template placeholder lines left in `OFL.txt`
- [x] `METADATA.pb` exists and matches font naming
- [x] `DESCRIPTION.en_us.html` exists
- [x] `Deadseascrolls-Regular.ttf` has `usWeightClass=400`
- [x] `fsType=0` (installable embedding)
- [x] Hebrew block present
- [x] No niqqud codepoints in U+0591..U+05C7
- [ ] Confirm Latin Core support (full set) — measured 100/324 present, 224 missing

## 2) Files ready to copy into your google/fonts fork

Prepared at:

- `legacy/submission/ofl/deadseascrolls/`

Contains:

- `Deadseascrolls-Regular.ttf`
- `METADATA.pb`
- `DESCRIPTION.en_us.html`
- `OFL.txt`

## 3) Required workflow (to avoid merge blockers)

1. Open a GitHub issue using “Add Font” template first.
2. Paste content from `docs/ADD_FONT_ISSUE_DRAFT.md`.
3. Attach one preview image.
4. Fork `google/fonts` and create branch `deadseascrolls`.
5. Copy prepared folder to `ofl/deadseascrolls/` in your fork.
6. Commit message: `Deadseascrolls: 1.000 added` (or your actual version).
7. Open PR and include in body:
   - upstream repo URL
   - exact source commit URL
   - note that this release targets Hebrew without niqqud

## 4) Known risk before submit

- Latin Core requirement is stricter than ASCII. If this is not met, PR may fail QA and need glyph expansion.
