"""Textextraktion ur bifogade dokument.

Endast den extraherade texten skickas vidare till modellanrop — aldrig
själva PDF-filen. Originalet sparas på disk för referens.
"""

import io

SUPPORTED = ("pdf", "txt", "md")


def _ext(filename: str) -> str:
    return (filename.rsplit(".", 1)[-1] if "." in filename else "").lower()


def is_supported(filename: str) -> bool:
    return _ext(filename) in SUPPORTED


def extract_text(filename: str, data: bytes) -> str:
    """Returnerar ren text ur en bifogad fil. Höjer ValueError för otillåtna typer."""
    ext = _ext(filename)
    if ext == "pdf":
        from pypdf import PdfReader  # importeras lokalt så övriga delar funkar utan beroendet
        reader = PdfReader(io.BytesIO(data))
        parts = [(page.extract_text() or "").strip() for page in reader.pages]
        text = "\n\n".join(p for p in parts if p)
    elif ext in ("txt", "md"):
        text = data.decode("utf-8", errors="replace")
    else:
        raise ValueError(
            f"Filtypen .{ext or '?'} stöds inte. Använd PDF, TXT eller MD."
        )
    return text.strip()
