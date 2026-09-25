"""Build a dependency-free single-page public edition for GitHub Pages upload."""
from pathlib import Path
import markdown

root = Path(__file__).resolve().parents[1]
pages = [
    "index.md", "01-access-the-lab.md", "02-webex-calling-org.md",
    "03-local-gateway.md", "04-captions-transcripts.md", "05-recording-summaries.md",
]
body = []
for page in pages:
    text = (root / "docs" / page).read_text(encoding="utf-8")
    body.append(markdown.markdown(text, extensions=["tables", "toc", "sane_lists"]))

html = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Next Gen Calling AI Elevate with Webex | LABCOL-2376</title>
<style>body{font-family:Arial,sans-serif;line-height:1.55;color:#172b4d;margin:auto;max-width:960px;padding:28px}h1{color:#0b5cab;margin-top:2.5rem}h2{color:#123b68;margin-top:2rem}li{margin:.35rem 0}blockquote{border-left:4px solid #0b5cab;background:#eef6ff;padding:1rem;margin:1.2rem 0}a{color:#0b5cab}code{background:#f1f3f5;padding:.15rem .3rem} .lab-meta{color:#52606d;font-weight:bold}</style>
</head><body>""" + "\n<hr>\n".join(body) + "</body></html>"
(root / "index.html").write_text(html, encoding="utf-8")
print("Wrote", root / "index.html")
