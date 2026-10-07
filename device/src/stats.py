import json
from collections import Counter
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_FILE = BASE_DIR / "input" / "records.json"
OUTPUT_FILE = BASE_DIR / "output" / "stats.json"


def load_records():
    with INPUT_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)


def build_stats(records):
    category_counts = Counter(
        record["category"]
        for record in records
        if record.get("category")
    )

    dates = [
        record["date"]
        for record in records
        if record.get("date")
    ]

    return {
        "period_start": min(dates) if dates else None,
        "period_end": max(dates) if dates else None,
        "total_days": len(set(dates)),
        "total_records": len(records),
        "ritual_count": sum(
            1 for record in records
            if record.get("type") == "ritual"
        ),
        "project_count": sum(
            1 for record in records
            if record.get("type") == "project"
        ),
        "ability_count": len(category_counts),
        "category_counts": dict(category_counts)
    }


def main():
    records = load_records()
    stats = build_stats(records)

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    with OUTPUT_FILE.open("w", encoding="utf-8") as file:
        json.dump(stats, file, ensure_ascii=False, indent=2)

    print(json.dumps(stats, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
