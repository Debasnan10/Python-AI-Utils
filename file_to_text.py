"""
Utility: Universal File-to-Text Converter
Supports: .txt, .md, .pdf, .docx
"""
import os
from typing import Optional

try:
    import docx
except Exception:
    docx = None

try:
    import PyPDF2
except Exception:
    PyPDF2 = None


def file_to_text(path: str) -> str:
    ext = os.path.splitext(path)[1].lower()

    if ext in [".txt", ".md"]:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()

    if ext == ".docx":
        if docx is None:
            raise ImportError("Install python-docx to read DOCX files: pip install python-docx")
        doc = docx.Document(path)
        return "\n".join([p.text for p in doc.paragraphs])

    if ext == ".pdf":
        if PyPDF2 is None:
            raise ImportError("Install PyPDF2 to read PDF files: pip install PyPDF2")
        reader = PyPDF2.PdfReader(path)
        texts = []
        for page in reader.pages:
            txt = page.extract_text()
            if txt:
                texts.append(txt)
        return "\n".join(texts)

    raise ValueError(f"Unsupported file type: {ext}")


if __name__ == "__main__":
    # quick demo (replace with a real path)
    sample_path = "sample.pdf"
    try:
        print(file_to_text(sample_path)[:500])
    except Exception as e:
        print("Error reading file:", e)
