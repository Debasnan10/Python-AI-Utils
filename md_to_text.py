"""
Utility: Markdown to Plain Text
Removes markdown formatting for cleaner embedding.
"""
import re


def markdown_to_text(md: str) -> str:
    # Remove code blocks
    md = re.sub(r"```.*?```", "", md, flags=re.DOTALL)
    # Remove inline code
    md = re.sub(r"`.*?`", "", md)
    # Remove markdown headers, bold, italics, links and other punctuation used by markdown
    md = re.sub(r"[_*#>`\-!\[\]\(\)]", " ", md)
    md = re.sub(r"\s+", " ", md)
    return md.strip()


if __name__ == "__main__":
    print(markdown_to_text("# Hello **World**! This is `code`."))
