"""
Utility: Text Normalizer
Lowercase, remove special chars, collapse whitespace.
"""
import re


def normalize_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s\.,!?-]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


if __name__ == "__main__":
    print(normalize_text("Hello!!! THIS --- is 99% *TEXT*"))
