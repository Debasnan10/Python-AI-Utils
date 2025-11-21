"""
Simple CLI wrapper for utilities in this repo.
"""
import argparse
from pathlib import Path


def main():
    parser = argparse.ArgumentParser("python-ai-utils")
    sub = parser.add_subparsers(dest="cmd")

    sp = sub.add_parser("split", help="Split text into chunks")
    sp.add_argument("--text", help="Text to split")
    sp.add_argument("--chunk-size", type=int, default=500)
    sp.add_argument("--overlap", type=int, default=100)

    sp = sub.add_parser("file-to-text", help="Convert file to text")
    sp.add_argument("path")

    sp = sub.add_parser("normalize", help="Normalize text")
    sp.add_argument("--text", help="Text to normalize")

    sp = sub.add_parser("md-to-text", help="Convert markdown to plain text")
    sp.add_argument("--text", help="Markdown text")

    sp = sub.add_parser("csv-to-json", help="Convert CSV to JSON")
    sp.add_argument("csv_path")
    sp.add_argument("json_path")

    sp = sub.add_parser("embed", help="Generate embeddings for texts")
    sp.add_argument("texts", nargs='+', help="Texts to embed")

    args = parser.parse_args()

    if args.cmd == "split":
        from text_splitter import split_text
        print(split_text(args.text, args.chunk_size, args.overlap))

    elif args.cmd == "file-to-text":
        from file_to_text import file_to_text
        print(file_to_text(args.path)[:1000])

    elif args.cmd == "normalize":
        from normalizer import normalize_text
        print(normalize_text(args.text))

    elif args.cmd == "md-to-text":
        from md_to_text import markdown_to_text
        print(markdown_to_text(args.text))

    elif args.cmd == "csv-to-json":
        from csv_to_json import csv_to_json
        csv_to_json(args.csv_path, args.json_path)
        print("Wrote", args.json_path)

    elif args.cmd == "embed":
        from batch_embeddings import generate_embeddings
        embs = generate_embeddings(args.texts)
        print(f"Generated {len(embs)} embeddings; dim={len(embs[0]) if embs else 0}")

    else:
        parser.print_help()


if __name__ == '__main__':
    main()
