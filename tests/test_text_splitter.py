from text_splitter import split_text


def test_basic_split():
    txt = "one two three four five six seven eight nine ten"
    parts = split_text(txt, chunk_size=4, overlap=1)
    # with chunk_size=4 and overlap=1 the implementation produces 4 chunks
    assert len(parts) == 4
    assert parts[0].split()[0] == "one"


def test_invalid_args():
    try:
        split_text("a b c", chunk_size=0)
        assert False, "should have raised"
    except ValueError:
        assert True
