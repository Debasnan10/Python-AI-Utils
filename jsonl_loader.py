"""
Utility: JSONL Loader
Reads .jsonl files (one JSON per line) into a Python list.
"""
import json
from typing import List


def load_jsonl(path: str) -> List[dict]:
    data = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            data.append(json.loads(line))
    return data


if __name__ == "__main__":
    items = load_jsonl("sample.jsonl")
    print("Loaded:", len(items), "records")
