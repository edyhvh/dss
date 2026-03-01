# Deadseascrolls → Google Fonts Summary
Date: 2026-03-01

## What we completed today

1. Reviewed Google Fonts contribution criteria (current GF Guide + google/fonts templates).
2. Audited local project files and identified submission requirements.
3. Created/updated required family submission files:
   - `METADATA.pb`
   - `DESCRIPTION.en_us.html`
   - `OFL.txt` (fixed first line and removed template placeholders)
4. Validated key technical metadata from `Deadseascrolls-Regular.ttf`:
   - Family/Subfamily/Full name/PostScript naming alignment
   - `usWeightClass = 400`
   - `fsType = 0` (installable embedding)
5. Verified Hebrew scope goal:
   - Hebrew block present
   - No niqqud codepoints in U+0591..U+05C7
6. Prepared Google Fonts repo-ready folder:
   - `legacy/submission/ofl/deadseascrolls/`
   - includes `Deadseascrolls-Regular.ttf`, `METADATA.pb`, `DESCRIPTION.en_us.html`, `OFL.txt`
7. Added support docs:
   - `docs/ADD_FONT_ISSUE_DRAFT.md`
   - `docs/TODAY_UPLOAD_CHECKLIST.md`
   - `docs/GF_GAP_REPORT.md`

## Current blocker

- Latin Core coverage is currently below requirement for standard onboarding:
  - Required glyph names: 324
  - Present: 100
  - Missing: 224
- Because of this, a direct PR may fail QA unless reviewers grant guidance/exception after issue review.

## Clarification confirmed

- Hebrew-only intent is valid.
- However, for new Google Fonts onboarding today, basic ASCII alone is usually not enough; reviewers generally expect Latin Core unless exception is granted.

## Recommended next steps (in order)

1. Open **Add Font** issue in `google/fonts` first.
2. Paste content from `docs/ADD_FONT_ISSUE_DRAFT.md`.
3. Be explicit in the issue:
   - Hebrew-first family
   - no niqqud by design
   - current Latin Core measurement (100/324)
   - ask whether onboarding can proceed now or requires full Latin Core first
4. Attach one image specimen (`legacy/Deadseascrolls.jpg` is fine).
5. In parallel, prepare a branch in your fork with `ofl/deadseascrolls/` from `legacy/submission/ofl/deadseascrolls/`.
6. If reviewers require full compliance, expand to Latin Core and resubmit.

## If you want fastest path today

- Submit issue now to get an official reviewer decision.
- Don’t over-claim checklist items not yet verified (already adjusted in draft).
- Treat issue response as gate before final PR push.
