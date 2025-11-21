from batch_embeddings import generate_embeddings


def test_embeddings_local_fallback():
    texts = ["hello world", "test"]
    embs = generate_embeddings(texts)
    assert len(embs) == 2
    assert len(embs[0]) in (384, 768, 512)
