# Python AI Utilities

![MIT License](https://img.shields.io/badge/License-MIT-green.svg)

Small, reusable Python utilities for AI workflows: text cleaning, file-to-text conversion, chunking for embeddings, simple CSV/JSON helpers, and an embeddings wrapper that supports OpenAI, Hugging Face, and a local deterministic fallback for offline/testing use.

![Banner](/mnt/data/A_banner_in_digital_graphic_design_features_Debasn.png)

## Table of contents

- About
- Files / utilities
- Installation
- Quick usage
- CLI
- Testing
- Contributing
- License

## About

`Python-AI-Utils` collects a set of small, focused scripts and helpers that are commonly useful when building retrieval-augmented generation (RAG) pipelines and embedding-based workflows. The goal is to keep each utility tiny, well-documented, and easy to reuse in other projects.

## Files / utilities

The repository root contains the following important modules (usable via import or the included CLI):

- `text_splitter.py` — split long text into overlapping word-based chunks useful for embeddings (function: `split_text`).
- `jsonl_loader.py` — load one-JSON-per-line files into Python lists (function: `load_jsonl`).
- `file_to_text.py` — universal file-to-text converter supporting `.txt`, `.md`, `.pdf`, `.docx` (function: `file_to_text`).
- `normalizer.py` — fast text normalizer: lowercasing, remove unwanted characters, collapse whitespace (function: `normalize_text`).
- `batch_embeddings.py` — generate embeddings for a batch of texts: tries OpenAI, then Hugging Face `sentence-transformers`, then a deterministic local hash fallback (function: `generate_embeddings`).
- `csv_to_json.py` — convert CSV files to pretty-printed JSON (function: `csv_to_json`).
- `md_to_text.py` — strip Markdown formatting and code blocks to plain text (function: `markdown_to_text`).
- `cli.py` — a tiny command-line wrapper exposing common utilities.
- `tests/` — pytest-based tests covering the utilities (run with `pytest`).
- `requirements.txt` — dependency hints (some packages are optional; see below).

## Installation

1. (Recommended) Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install the minimal/test dependencies:

```bash
python3 -m pip install -r requirements.txt
```

Notes on optional dependencies:

- `python-docx` and `PyPDF2` are listed for reading `.docx` and `.pdf` files in `file_to_text.py`. If you don't need those formats, you can skip installing them.
- `openai` is included if you want to use OpenAI embeddings. If it's not available, `batch_embeddings.py` will try `sentence-transformers` and then a local deterministic fallback which is useful for testing.
- `sentence-transformers` (Hugging Face) is not in `requirements.txt` by default; install it if you want a local, higher-quality embedding model:

```bash
python3 -m pip install sentence-transformers
```

## Quick usage (examples)

Importing and using the utilities from Python:

```python
from text_splitter import split_text
from normalizer import normalize_text
from batch_embeddings import generate_embeddings

text = "Some long text..."
chunks = split_text(text, chunk_size=200, overlap=40)
chunks = [normalize_text(c) for c in chunks]
embs = generate_embeddings(chunks)
```

Using the CLI (from the repo root):

```bash
python cli.py split-text --file input.txt --chunk-size 200 --overlap 40
python cli.py normalize --text "Hello,   WORLD!!"
python cli.py embed --file input.txt
python cli.py file-to-text --file document.pdf
python cli.py csv-to-json --csv input.csv --json output.json
python cli.py md-to-text --file notes.md
```

## CLI

The `cli.py` script exposes the main utilities via command-line arguments. Run:

```bash
python cli.py --help
```

for a list of available commands and options.

## Testing

Run all tests using `pytest`:

```bash
python3 -m pip install pytest
pytest
```

## Contributing

Pull requests, issues, and suggestions are welcome! Please open an issue or PR on GitHub.

- Fork the repo and create a branch for your feature or fix.
- Add or update tests for your changes.
- Run `pytest` to ensure all tests pass.
- Submit a pull request with a clear description.

## License

MIT License. See [`LICENSE`](../LICENSE) for full text.

Copyright (c) 2025 Debasnan Singh

---

**Author:**  
Debasnan Singh  
GitHub: [Debasnan10](https://github.com/Debasnan10)

---

**Acknowledgements:**

- OpenAI for API and embedding model support.
- Hugging Face for `sentence-transformers`.
- Community contributors.

---
