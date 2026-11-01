# STATUS

AI Privacy for Healthcare Workers — beginner manual + static HTML site.
Built by Dylan Asdale for Asdale Dynamics, LLC (Indiana, formed October 2026).
Education only — never medical advice.

## What was built

- `LICENSE` — MIT License, copyright line exactly
  `Copyright (c) 2026 Asdale Dynamics, LLC`
- `README.md` — warm, plain-English project overview; credits Asdale Dynamics,
  LLC and Dylan Asdale; explains audience, contents, how to use, and the
  education-only disclaimer
- `test/verify.py` — verification test suite (Python 3), runnable with
  `python3 test/verify.py`
- `docs/` — beginner manual in Markdown (substantive, step by step, plain
  English, never condescending):
  - `index.md` — overview, who this is for, quick-start rule, how to use
  - `patient-data-basics.md` — what patient data is, the small-detail trap,
    EHR vs. AI chatbots, HIPAA in one paragraph, workplace comes first
  - `what-never-to-paste.md` — never-paste list, safe vs. not-safe examples,
    what to do if you already pasted something
  - `safe-habits.md` — before/during/after AI use, approved tools, at-home
    guidance, daily checklist
  - `disclaimer.md` — education only, never medical or legal advice
  - `checklist.md` — printable one-page checklist
- `site/` — static HTML version (no build step, no server, no account):
  - `index.html`, `patient-data-basics.html`, `what-never-to-paste.html`,
    `safe-habits.html`, `checklist.html`, `disclaimer.html`
  - `style.css` — warm, plain-English styling with skip link, focus styles,
    responsive max-width
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

## How to run tests

Run the verification suite with Python 3:

```
python3 test/verify.py
```

It checks that all expected files exist, the LICENSE copyright line is exact,
README credits Asdale Dynamics, LLC, HTML pages parse and all internal links
resolve, every page carries the education-only disclaimer and an Asdale credit,
the checklist print stylesheet is wired up, no `.github/workflows` exists, and
no secrets/API keys/personal data are present. Exit code 0 = all pass.

## Verification results

`python3 test/verify.py` — PASSED, all 54 checks passed.

- 17 expected files present
- LICENSE contains the exact copyright line once
- README credits Asdale Dynamics, LLC; states education only and never medical
  advice
- No `.github/workflows` directory present
- 6 HTML pages parse; all internal links resolve; each page has viewport meta
  tag, meta description, education-only disclaimer, and Asdale credit
- checklist.html links `print.css` with `media="print"`
- All docs credit Asdale Dynamics, LLC
- Secrets scan: clean (no API keys, secrets, or personal data)

No formal test framework was configured (this is a static HTML/Markdown site
with no build step); `test/verify.py` is the verification suite.

## Known gaps

- No automated unit/integration test framework (static HTML/Markdown; nothing
  to compile or run beyond `test/verify.py`)
- HTML verified with the custom Python script, not a formal HTML validator
- Markdown files are not auto-converted to HTML; `docs/` and `site/` are kept
  in sync manually
- No CI/CD workflows (intentionally absent per project rules)
- The manual is US/HIPAA-focused; healthcare workers outside the US should
  confirm local rules with their privacy officer

## Credit

Written by Dylan Asdale for Asdale Dynamics, LLC. MIT licensed. See `LICENSE`.
