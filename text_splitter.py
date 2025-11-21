"""
Utility: Text Splitter
Splits large text into clean, overlapping chunks for embeddings / RAG pipelines.
"""
from typing import List


def split_text(text: str, chunk_size: int = 500, overlap: int = 100) -> List[str]:
    """Split text into overlapping chunks by words.

    Args:
        text: input text to split
        chunk_size: number of words per chunk
        overlap: number of words to overlap between chunks

    Returns:
        list of text chunks
    """
    text = text.strip().replace("\n", " ")
    words = text.split()

    if chunk_size <= 0:
        raise ValueError("chunk_size must be > 0")
    if overlap < 0:
        raise ValueError("overlap must be >= 0")
    if overlap >= chunk_size:
        raise ValueError("overlap must be smaller than chunk_size")

    chunks: List[str] = []
    start = 0
    while start < len(words):
        end = start + chunk_size
        chunk = " ".join(words[start:end])
        if chunk:
            chunks.append(chunk)
        # advance by chunk_size - overlap (at least 1)
        step = max(1, chunk_size - overlap)
        start += step

    return chunks


if __name__ == "__main__":
    sample = (
        "This is a long text that we want to split into manageable chunks for embeddings. "
        "Each chunk contains a fixed number of words and overlaps the previous chunk by some words."
    )
    parts = split_text(sample, chunk_size=10, overlap=2)
    print(parts)
