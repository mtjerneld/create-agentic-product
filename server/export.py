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
    from htmldocx import HtmlToDocx

    doc = Document()
    parser = HtmlToDocx()
    for i, text in enumerate(sections):
        if i > 0:
            doc.add_page_break()
        parser.add_html_to_document(_to_html(text), doc)

    buf = io.BytesIO()
    doc.save(buf)
    return buf.getvalue()
