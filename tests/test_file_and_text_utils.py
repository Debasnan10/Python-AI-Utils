from pathlib import Path

from file_to_text import file_to_text
from normalizer import normalize_text
from md_to_text import markdown_to_text


def test_file_to_text_txt(tmp_path: Path):
    p = tmp_path / "a.txt"
    p.write_text("Hello world\nLine two", encoding="utf-8")
    t = file_to_text(str(p))
    assert "Hello world" in t


def test_normalizer_and_md():
    s = "Hello!!! THIS --- is 99% *TEXT*"
    n = normalize_text(s)
    assert "hello" in n
    md = "# Title\nThis is `code` and **bold**"
    plain = markdown_to_text(md)
    assert "Title" in plain
