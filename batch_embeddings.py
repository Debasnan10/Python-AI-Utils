"""
Utility: Batch Embeddings Generator
Uses OpenAI API or a local HF embedding model.
"""
import os
from typing import List
import hashlib


def _local_fallback(texts: List[str], dim: int = 384) -> List[List[float]]:
    """Deterministic fallback embedding: hash-based pseudo-embedding."""
    out = []
    for t in texts:
        h = hashlib.sha256(t.encode("utf-8")).digest()
        vals = []
        # expand to requested dim by repeating hash bytes
        i = 0
        while len(vals) < dim:
            vals.append((h[i % len(h)] % 100) / 100.0)
            i += 1
        out.append(vals[:dim])
    return out


def generate_embeddings(texts: List[str], model: str = "text-embedding-3-small") -> List[List[float]]:
    """Generate embeddings using OpenAI if available, otherwise try HF `sentence-transformers`, otherwise a local fallback.

    Returns a list of float vectors.
    """
    # Try OpenAI first
    try:
        import openai  # type: ignore
    except Exception:
        openai = None

    if openai is not None:
        api_key = os.getenv("OPENAI_API_KEY")
        if api_key:
            openai.api_key = api_key
            try:
                response = openai.embeddings.create(model=model, input=texts)
                return [item.embedding for item in response.data]
            except Exception:
                # fall through to other options
                pass

    # Try Hugging Face sentence-transformers
    try:
        from sentence_transformers import SentenceTransformer  # type: ignore
        hf_model = SentenceTransformer("all-MiniLM-L6-v2")
        return hf_model.encode(texts, show_progress_bar=False).tolist()
    except Exception:
        pass

    # Local deterministic fallback
    return _local_fallback(texts, dim=384)


if __name__ == "__main__":
    out = generate_embeddings(["hello world", "this is a test"])
    print(len(out), "embeddings generated")
