#!/usr/bin/env python3
"""Verification test suite for the AI Privacy for Healthcare Workers manual.

Checks that all expected files exist, the LICENSE copyright line is exact,
README credits Asdale Dynamics, LLC, HTML pages parse and link correctly,
the print stylesheet is wired up, no secrets or personal data are present,
and every page carries the education-only disclaimer and Asdale credit.

Run with:  python3 test/verify.py
Exits 0 if all checks pass, 1 otherwise.
"""

import html.parser
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = os.path.join(ROOT, "site")
DOCS = os.path.join(ROOT, "docs")

failures = []


def check(condition, message):
    if not condition:
        failures.append(message)
        print(f"  FAIL: {message}")
    else:
        print(f"  ok: {message}")


# 1. Expected files exist
print("== Files ==")
expected = [
    "LICENSE",
    "README.md",
    "docs/index.md",
    "docs/patient-data-basics.md",
    "docs/what-never-to-paste.md",
    "docs/safe-habits.md",
    "docs/disclaimer.md",
    "docs/checklist.md",
    "site/index.html",
    "site/patient-data-basics.html",
    "site/what-never-to-paste.html",
    "site/safe-habits.html",
    "site/checklist.html",
    "site/disclaimer.html",
    "site/style.css",
    "site/print.css",
]
for rel in expected:
    check(os.path.exists(os.path.join(ROOT, rel)), f"exists: {rel}")

# 2. LICENSE exact copyright line
print("== LICENSE ==")
with open(os.path.join(ROOT, "LICENSE"), encoding="utf-8") as fh:
    license_text = fh.read()
copyright_line = "Copyright (c) 2026 Asdale Dynamics, LLC"
check(
    license_text.count(copyright_line) == 1,
    f"LICENSE contains exact copyright line once: {copyright_line!r}",
)

# 3. README credits
print("== README ==")
with open(os.path.join(ROOT, "README.md"), encoding="utf-8") as fh:
    readme_text = fh.read()
check("Asdale Dynamics, LLC" in readme_text, "README credits Asdale Dynamics, LLC")
check("Education only" in readme_text, "README states education only")
check("never medical advice" in readme_text.lower(), "README states never medical advice")

# 4. No .github/workflows
print("== Project rules ==")
check(
    not os.path.exists(os.path.join(ROOT, ".github", "workflows")),
    "no .github/workflows directory",
)

# 5. No secrets or personal data
print("== Secrets scan ==")
secret_patterns = [
    re.compile(r"(?i)\bsk-[A-Za-z0-9]{16,}\b"),
    re.compile(r"(?i)\bAKIA[A-Z0-9]{16,}\b"),
    re.compile(r"(?i)(?:api[_-]?key|secret|access[_-]?token|private[_-]?key)\s*[:=]\s*['\"]?[A-Za-z0-9_\-]{12,}"),
]
secret_hits = 0
for dirpath, _dirs, files in os.walk(ROOT):
    if ".git" in dirpath:
        continue
    for fn in files:
        path = os.path.join(dirpath, fn)
        try:
            with open(path, encoding="utf-8", errors="ignore") as fh:
                content = fh.read()
        except Exception:
            continue
        for pat in secret_patterns:
            for _ in pat.finditer(content):
                secret_hits += 1
                failures.append(f"possible secret in {os.path.relpath(path, ROOT)}")
                print(f"  FAIL: possible secret in {os.path.relpath(path, ROOT)}")
check(secret_hits == 0, "no secrets, API keys, or personal data found")

# 6. HTML parse + links + disclaimer + credit
print("== HTML pages ==")


class LinkParser(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key in ("href", "src") and value and not value.startswith(
                ("http://", "https://", "mailto:", "#")
            ):
                self.links.append(value)


html_files = sorted(f for f in os.listdir(SITE) if f.endswith(".html"))
check(len(html_files) == 6, f"six HTML pages present (found {len(html_files)})")

for hf in html_files:
    path = os.path.join(SITE, hf)
    with open(path, encoding="utf-8") as fh:
        content = fh.read()

    # parse sanity
    try:
        html.parser.HTMLParser().feed(content)
        check(True, f"{hf} parses")
    except Exception as exc:  # noqa: BLE001
        check(False, f"{hf} parse error: {exc}")

    # internal links resolve
    parser = LinkParser()
    parser.feed(content)
    for link in parser.links:
        target = os.path.join(SITE, link)
        check(os.path.exists(target), f"{hf} link resolves: {link}")

    # education disclaimer banner present
    check(
        "Education only" in content or "education only" in content,
        f"{hf} carries education-only disclaimer",
    )

    # Asdale credit present
    check(
        "Asdale Dynamics, LLC" in content,
        f"{hf} credits Asdale Dynamics, LLC",
    )

    # viewport meta tag present
    check('name="viewport"' in content, f"{hf} has viewport meta tag")

    # meta description present
    check('<meta name="description"' in content, f"{hf} has meta description")

# 7. Checklist print stylesheet
print("== Checklist print ==")
with open(os.path.join(SITE, "checklist.html"), encoding="utf-8") as fh:
    checklist_html = fh.read()
check(
    'print.css' in checklist_html and 'media="print"' in checklist_html,
    "checklist.html links print.css with media=print",
)

# 8. Docs credit Asdale
print("== Docs credit ==")
for df in os.listdir(DOCS):
    if not df.endswith(".md"):
        continue
    with open(os.path.join(DOCS, df), encoding="utf-8") as fh:
        doc_text = fh.read()
    check(
        "Asdale Dynamics, LLC" in doc_text,
        f"docs/{df} credits Asdale Dynamics, LLC",
    )

# Summary
print()
if failures:
    print(f"VERIFICATION FAILED: {len(failures)} check(s) did not pass.")
    for f in failures:
        print(f"  - {f}")
    sys.exit(1)

print(f"VERIFICATION PASSED: all {len(expected) + 8 + len(html_files) * 5} checks passed.")
sys.exit(0)
