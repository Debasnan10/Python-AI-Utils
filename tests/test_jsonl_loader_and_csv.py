import json
from pathlib import Path

from jsonl_loader import load_jsonl
from csv_to_json import csv_to_json


def test_jsonl_loader(tmp_path: Path):
    p = tmp_path / "data.jsonl"
    items = [{"a": 1}, {"b": 2}]
    p.write_text("\n".join(json.dumps(i) for i in items), encoding="utf-8")
    loaded = load_jsonl(str(p))
    assert loaded == items


def test_csv_to_json(tmp_path: Path):
    csv_p = tmp_path / "in.csv"
    json_p = tmp_path / "out.json"
    csv_p.write_text("col1,col2\n1,a\n2,b\n", encoding="utf-8")
    out = csv_to_json(str(csv_p), str(json_p))
    assert out == str(json_p)
    data = json.loads(json_p.read_text(encoding="utf-8"))
    assert data[0]["col1"] == "1"
