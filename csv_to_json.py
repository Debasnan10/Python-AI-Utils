"""
Utility: CSV to JSON Converter
"""
import csv
import json
from typing import Any


def csv_to_json(csv_path: str, json_path: str) -> str:
    with open(csv_path, newline='', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    return json_path


if __name__ == "__main__":
    print(csv_to_json("sample.csv", "output.json"))
