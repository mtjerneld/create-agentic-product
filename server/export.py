"""Export av markdown-dokument till Word (.docx).

Markdown renderas till HTML och konverteras sedan till ett Word-dokument.
"""

import io

import markdown as md

_EXT = ["extra", "sane_lists", "toc"]


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
