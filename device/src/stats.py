import json
from collections import Counter
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_FILE = BASE_DIR / "input" / "records.json"
RITUAL_DAYS_FILE = BASE_DIR / "input" / "ritual-days.json"
OUTPUT_FILE = BASE_DIR / "output" / "stats.json"


def load_json(path):
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def build_stats(records, ritual_days):
    dates = [
        day["date"]
        for day in ritual_days
        if day.get("date")
    ]
    completed_days = [
        day for day in ritual_days
        if day.get("status") == "completed"
    ]
    in_progress_days = [
        day for day in ritual_days
        if day.get("status") == "in_progress"
    ]

    practice_counts = Counter(
        day["practice_status"]
        for day in completed_days
        if day.get("practice_status")
    )
    curated_category_counts = Counter(
        record["category"]
        for record in records
        if record.get("category")
    )

    return {
        "period_start": min(dates) if dates else None,
        "period_end": max(dates) if dates else None,
        "total_days": len(set(dates)),
        "completed_days": len(completed_days),
        "in_progress_days": len(in_progress_days),
        "practice_completed_days": practice_counts.get("실천했다", 0),
        "practice_partial_days": practice_counts.get("일부 실천했다", 0),
        "curated_record_count": len(records),
        "curated_ability_count": len(curated_category_counts),
        "curated_category_counts": dict(curated_category_counts)
    }


def main():
    records = load_json(INPUT_FILE)
    ritual_days = load_json(RITUAL_DAYS_FILE)
    stats = build_stats(records, ritual_days)

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    with OUTPUT_FILE.open("w", encoding="utf-8") as file:
        json.dump(stats, file, ensure_ascii=False, indent=2)

    print(json.dumps(stats, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
