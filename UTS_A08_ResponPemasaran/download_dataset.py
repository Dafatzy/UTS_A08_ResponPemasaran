#!/usr/bin/env python3
"""Download UCI Bank Marketing and extract the full legacy bank-full.csv."""
from pathlib import Path
from urllib.request import urlopen
from zipfile import ZipFile
from io import BytesIO
import csv, hashlib, json, sys
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parent
RAW = ROOT / "data" / "raw"
RAW.mkdir(parents=True, exist_ok=True)
URL = "https://archive.ics.uci.edu/static/public/222/bank+marketing.zip"
EXPECTED_COLUMNS = [
    "age", "job", "marital", "education", "default", "balance", "housing", "loan",
    "contact", "day", "month", "duration", "campaign", "pdays", "previous", "poutcome", "y"
]
EXPECTED_ROWS = 45211

def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def extract_full(outer_bytes: bytes) -> bytes:
    with ZipFile(BytesIO(outer_bytes)) as outer:
        inner_names = [n for n in outer.namelist() if Path(n).name.lower() == "bank.zip"]
        direct_names = [n for n in outer.namelist() if Path(n).name.lower() == "bank-full.csv"]
        if direct_names:
            return outer.read(direct_names[0])
        if not inner_names:
            raise FileNotFoundError("bank.zip tidak ditemukan dalam arsip UCI.")
        with ZipFile(BytesIO(outer.read(inner_names[0]))) as inner:
            names = [n for n in inner.namelist() if Path(n).name.lower() == "bank-full.csv"]
            if not names:
                raise FileNotFoundError("bank-full.csv tidak ditemukan di dalam bank.zip.")
            return inner.read(names[0])

def validate(data: bytes):
    text = data.decode("utf-8-sig")
    reader = csv.reader(text.splitlines(), delimiter=';')
    header = next(reader)
    if header != EXPECTED_COLUMNS:
        raise ValueError(f"Skema tidak sesuai. Header ditemukan: {header}")
    rows = sum(1 for _ in reader)
    if rows != EXPECTED_ROWS:
        raise ValueError(f"Jumlah baris {rows:,}, seharusnya {EXPECTED_ROWS:,}.")
    return rows, len(header)

def main():
    print("Mengunduh arsip resmi UCI:", URL)
    with urlopen(URL, timeout=90) as response:
        outer = response.read()
    csv_bytes = extract_full(outer)
    rows, cols = validate(csv_bytes)
    dest = RAW / "bank-full.csv"
    dest.write_bytes(csv_bytes)
    record = {
        "dataset": "UCI Bank Marketing - bank-full.csv",
        "dataset_id": 222,
        "source_page": "https://archive.ics.uci.edu/dataset/222/bank+marketing",
        "source_archive": URL,
        "source_method": "downloaded directly from official UCI archive using download_dataset.py",
        "source_zip_sha256": sha256(outer),
        "csv_sha256": sha256(csv_bytes),
        "actual_shape": [rows, cols],
        "validated_at_utc": datetime.now(timezone.utc).isoformat(),
    }
    (RAW / "dataset_provenance.json").write_text(json.dumps(record, indent=2), encoding="utf-8")
    print(f"Berhasil: {dest}")
    print(f"Ukuran terverifikasi: {rows:,} baris x {cols} kolom")
    print("CSV SHA-256:", record["csv_sha256"])

if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print("Gagal mengunduh/memvalidasi dataset:", exc, file=sys.stderr)
        sys.exit(1)
