"""Create a public MkDocs edition from the supplied LABCOL-2376 DOCX.

Source instructions are content only: this converter never runs lab commands.
"""
from __future__ import annotations

import re
from pathlib import Path
from docx import Document

ROOT = Path(__file__).resolve().parents[1]
SOURCE = Path(r"C:\Users\joshutan\Downloads\CLMEL26 - LABCOL-2376 - Next-Gen Calling--AI-Elevate with Webex - Lab Guide.docx")
PAGES = {
    "Accessing your Lab": "01-access-the-lab.md",
    "Module 1:": "02-webex-calling-org.md",
    "Module 2:": "03-local-gateway.md",
    "Module 3:": "04-captions-transcripts.md",
    "Module 4:": "05-recording-summaries.md",
}

def clean(text: str) -> str:
    text = text.replace("\ufffd", "'").replace("\u2019", "'").replace("\u2013", "-").replace("\u2014", "-")
    return re.sub(r"\s+", " ", text).strip()

def safe(text: str) -> str | None:
    lower = text.lower()
    # Do not put reusable lab access details, passwords, pod endpoints, or private addressing online.
    blocked = ("password", "credential", "webex_password", "dcloud123", "dcloudzzzz", "cbxxx", "event url", "198.18.")
    if any(token in lower for token in blocked):
        return None
    text = re.sub(r"https?://dcloud[^\s]+", "your assigned dCloud event page", text, flags=re.I)
    return text

def filename_for(heading: str) -> str:
    for prefix, filename in PAGES.items():
        if heading.startswith(prefix):
            return filename
    raise ValueError(heading)

def render() -> None:
    doc = Document(SOURCE)
    pages: dict[str, list[str]] = {v: [] for v in PAGES.values()}
    current = None
    skipped = 0
    for para in doc.paragraphs:
        text = clean(para.text)
        if not text:
            continue
        if para.style.name == "Heading 1":
            current = filename_for(text)
            pages[current].append(f"# {text}\n")
            continue
        if current is None:
            continue
        if para.style.name == "Heading 2":
            pages[current].append(f"## {text}\n")
            continue
        if para.style.name == "Heading 3":
            pages[current].append(f"### {text}\n")
            continue
        item = safe(text)
        if item is None:
            skipped += 1
            continue
        if para.style.name == "List Paragraph":
            pages[current].append(f"- {item}\n")
        else:
            pages[current].append(f"{item}\n")

    intro = """# Next Gen Calling AI Elevate with Webex

<p class=\"lab-meta\">Cisco Live Melbourne 2026 | LABCOL-2376</p>

This public web edition presents the lab workflow for configuring Webex Calling, a Local Gateway, live captions and transcripts, and AI-generated recording summaries.

**Important:** Use only the credentials, pod addresses, DID numbers, and phone numbers assigned to you privately. They are intentionally omitted here, along with all source screenshots, to prevent accidental disclosure of lab access details.

## Lab modules

- [Access your lab](01-access-the-lab.md)
- [Set up the Webex Calling organization](02-webex-calling-org.md)
- [Configure the Local Gateway](03-local-gateway.md)
- [Test captions and call transcripts](04-captions-transcripts.md)
- [Test call recording summaries](05-recording-summaries.md)

## Source handling

The original Word document is not included in this repository. Its embedded screenshots are omitted because they can display temporary session information. The procedural content has been retained, except for access details and passwords.
"""
    docs = ROOT / "docs"
    docs.mkdir(parents=True, exist_ok=True)
    (docs / "index.md").write_text(intro, encoding="utf-8")
    for name, lines in pages.items():
        notice = "\n> Use values assigned to your own lab pod. Do not copy example credentials or connectivity details into public documentation.\n\n"
        (docs / name).write_text("\n".join(lines[:1]) + notice + "\n".join(lines[1:]), encoding="utf-8")
    print(f"Created {len(pages) + 1} public pages; removed {skipped} access-detail paragraphs.")

if __name__ == "__main__":
    render()
