"""Export av markdown-dokument till Word (.docx) och PDF.

Markdown renderas till HTML och konverteras sedan till önskat format.
PDF-styling speglar utseendet i webbappens .doc-render-vy (samma typografi,
färger och rubrikstilar) — den baseras alltså på HTML-vyn, inte Word-filen.
"""

import io
from html import escape

import markdown as md

_EXT = ["extra", "sane_lists", "toc", "tables"]


def _to_html(text: str) -> str:
    return md.markdown(text or "", extensions=_EXT)


def md_to_docx(sections: list) -> bytes:
    """Bygger ett .docx av en lista markdown-texter.

    `sections` är en lista strängar (varje = ett markdown-dokument). Flera
    sektioner separeras med sidbrytning.
    """
    from docx import Document
    from docx.shared import Mm
    from htmldocx import HtmlToDocx

    doc = Document()

    # A4 (210 × 297 mm) med 25 mm marginaler — annars defaultar python-docx till Letter.
    for section in doc.sections:
        section.page_width = Mm(210)
        section.page_height = Mm(297)
        section.left_margin = Mm(25)
        section.right_margin = Mm(25)
        section.top_margin = Mm(25)
        section.bottom_margin = Mm(25)

    parser = HtmlToDocx()
    for i, text in enumerate(sections):
        if i > 0:
            doc.add_page_break()
        parser.add_html_to_document(_to_html(text), doc)

    buf = io.BytesIO()
    doc.save(buf)
    return buf.getvalue()


# CSS som speglar .doc-render i web/style.css — anpassad för xhtml2pdf
# (begränsad CSS-stöd, inga CSS-variabler, ingen rem, inga moderna selektorer).
_PDF_CSS = """
@page {
  size: A4;
  margin: 22mm 20mm;
}
body {
  font-family: "Helvetica", "Arial", sans-serif;
  font-size: 10.5pt;
  color: #1a2434;
  line-height: 1.55;
}
h1 {
  font-family: "Times-Roman", "Georgia", serif;
  color: #0e1a2b;
  font-size: 22pt;
  font-weight: normal;
  margin: 0 0 10pt 0;
  line-height: 1.2;
}
h2 {
  font-family: "Times-Roman", "Georgia", serif;
  color: #0e1a2b;
  font-size: 16pt;
  font-weight: normal;
  margin: 18pt 0 7pt 0;
  padding-bottom: 3pt;
  border-bottom: 1pt solid #d8dde6;
}
h3 {
  color: #3a6f8f;
  font-size: 12pt;
  font-weight: bold;
  margin: 14pt 0 5pt 0;
}
h4, h5, h6 {
  color: #0e1a2b;
  font-size: 11pt;
  font-weight: bold;
  margin: 12pt 0 4pt 0;
}
p {
  margin: 0 0 8pt 0;
}
ul, ol {
  margin: 0 0 8pt 0;
  padding-left: 16pt;
}
li {
  margin: 2pt 0;
}
a {
  color: #3a6f8f;
  text-decoration: none;
}
strong, b {
  color: #0e1a2b;
  font-weight: bold;
}
em, i {
  font-style: italic;
}
code {
  background: #f3f5f9;
  border: 1pt solid #d8dde6;
  font-family: "Courier", "Consolas", monospace;
  font-size: 9pt;
  padding: 0pt 3pt;
}
pre {
  background: #f3f5f9;
  border: 1pt solid #d8dde6;
  padding: 8pt;
  font-family: "Courier", "Consolas", monospace;
  font-size: 9pt;
  white-space: pre-wrap;
}
pre code {
  background: transparent;
  border: none;
  padding: 0;
}
blockquote {
  margin: 0 0 8pt 0;
  padding: 3pt 9pt;
  border-left: 3pt solid #3a6f8f;
  color: #5a6679;
}
table {
  border-collapse: collapse;
  width: 100%;
  margin: 0 0 8pt 0;
  font-size: 9.5pt;
}
th, td {
  border: 1pt solid #d8dde6;
  padding: 4pt 7pt;
  text-align: left;
}
th {
  background: #f3f5f9;
  color: #0e1a2b;
  font-weight: bold;
}
hr {
  border: none;
  border-top: 1pt solid #d8dde6;
  margin: 12pt 0;
}
.page-break {
  page-break-before: always;
}
"""


def _wrap_html(sections: list, title: str = "Dokument") -> str:
    parts = []
    for i, text in enumerate(sections):
        cls = ' class="page-break"' if i > 0 else ""
        parts.append(f'<div{cls}>{_to_html(text)}</div>')
    body = "\n".join(parts)
    return (
        "<!DOCTYPE html><html><head>"
        f"<meta charset='utf-8'><title>{escape(title)}</title>"
        f"<style>{_PDF_CSS}</style>"
        f"</head><body>{body}</body></html>"
    )


def md_to_pdf(sections: list, title: str = "Dokument") -> bytes:
    """Bygger en PDF av en lista markdown-texter.

    Stylingen speglar webbappens HTML-vy (.doc-render) — typografi, rubriker,
    färger och tabeller motsvarar det användaren ser i appen. Flera sektioner
    separeras med sidbrytning.
    """
    from xhtml2pdf import pisa

    html = _wrap_html(sections, title=title)
    buf = io.BytesIO()
    result = pisa.CreatePDF(src=html, dest=buf, encoding="utf-8")
    if result.err:
        raise RuntimeError(f"PDF-generering misslyckades ({result.err} fel)")
    return buf.getvalue()
