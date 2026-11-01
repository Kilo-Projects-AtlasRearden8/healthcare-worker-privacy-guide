# STATUS

AI Privacy for Healthcare Workers — beginner manual + static HTML site.
Built by Dylan Asdale for Asdale Dynamics, LLC (Indiana, formed October 2026).
Education only — never medical advice.

## What was built

- `LICENSE` — MIT License, copyright line exactly
  `Copyright (c) 2026 Asdale Dynamics, LLC`
- `README.md` — project overview, credits Asdale Dynamics, LLC
- `docs/` — beginner manual in Markdown:
  - `index.md` — overview and quick starting rule
  - `patient-data-basics.md` — what patient data is, EHR vs. AI chatbots, HIPAA in one paragraph
  - `what-never-to-paste.md` — never-paste list, small-detail trap, safe vs. not safe examples, incident response
  - `safe-habits.md` — before/during/after AI use, at-home guidance, daily checklist
  - `disclaimer.md` — education only, never medical or legal advice
  - `checklist.md` — printable one-page checklist
- `site/` — static HTML version (no build step, no server, no account):
  - `index.html`, `patient-data-basics.html`, `what-never-to-paste.html`,
    `safe-habits.html`, `checklist.html`, `disclaimer.html`
  - `style.css` — warm, plain-English styling
  - `print.css` — print stylesheet for the checklist (one page, ink-friendly)

## How to run

Open any file in `site/` directly in a web browser. No install, no server, no
internet required once you have the files:

```
open site/index.html
```

or double-click `site/index.html` in your file explorer. Print
`site/checklist.html` using your browser's print dialog for the printable
checklist (`print.css` applies automatically when printing).

Markdown sources live in `docs/` and can be read in any text editor.

## Verification results

Verification script run: all checks passed.

- 14 expected files present (LICENSE, README.md, 6 docs, 6 HTML pages, 2 CSS)
- LICENSE contains the exact copyright line `Copyright (c) 2026 Asdale Dynamics, LLC` once
- README.md credits Asdale Dynamics, LLC
- 6 HTML pages parse successfully
- All internal links (`href`/`src`) resolve to existing files
- checklist.html includes `print.css` with `media="print"`
- No `.github/workflows` directory present
- Scan for secrets/API keys/personal data: clean (the word "passwords" appears
  only in educational guidance such as "do not paste passwords")

No test framework was configured for this static site; verification was a
custom link/integrity script run with Python 3.

## Known gaps

- No automated test suite (static HTML/Markdown; no build step to test)
- HTML validated with a custom script, not a formal HTML validator
- Markdown files are not converted to HTML automatically; `docs/` and `site/`
  are manually kept in sync
- No CI/CD workflows (intentionally absent per project rules)

## Credit

Written by Dylan Asdale for Asdale Dynamics, LLC. MIT licensed. See `LICENSE`.
