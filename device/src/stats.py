import json
from collections import Counter
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_FILE = BASE_DIR / "input" / "records.json"
RITUAL_DAYS_FILE = BASE_DIR / "input" / "ritual-days.json"
SUMMARY_FILE = BASE_DIR / "input" / "ritual-summary.json"
OUTPUT_FILE = BASE_DIR / "output" / "stats.json"


def load_json(path):
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def build_stats(records, ritual_days, summary=None):
    if summary is None:
        dates = [day["date"] for day in ritual_days if day.get("date")]
        completed = [day for day in ritual_days if day.get("status") == "completed"]
        in_progress = [day for day in ritual_days if day.get("status") == "in_progress"]
        practice_counts = Counter(
            day["practice_status"] for day in completed if day.get("practice_status")
        )
        totals = {
            "period_start": min(dates) if dates else None,
            "period_end": max(dates) if dates else None,
            "total_days": len(set(dates)),
            "completed_days": len(completed),
            "in_progress_days": len(in_progress),
            "practice_completed_days": practice_counts.get("실천했다", 0),
            "practice_partial_days": practice_counts.get("일부 실천했다", 0),
        }
    else:
        keys = (
            "period_start", "period_end", "total_days", "completed_days",
            "in_progress_days", "practice_completed_days", "practice_partial_days",
        )
        totals = {key: summary[key] for key in keys}
        if totals["total_days"] != totals["completed_days"] + totals["in_progress_days"]:
            raise ValueError("기록한 날 수와 마감·진행 중 기록 수가 일치하지 않습니다.")
        if totals["completed_days"] != totals["practice_completed_days"] + totals["practice_partial_days"]:
            raise ValueError("마감 기록 수와 실천 상태별 집계가 일치하지 않습니다.")

        dates = sorted({day["date"] for day in ritual_days if day.get("date")})
        completed = [day for day in ritual_days if day.get("status") == "completed"]
        in_progress = [day for day in ritual_days if day.get("status") == "in_progress"]
        practice_counts = Counter(
            day["practice_status"] for day in completed if day.get("practice_status")
        )
        observed = {
            "period_start": dates[0] if dates else None,
            "period_end": dates[-1] if dates else None,
            "total_days": len(dates),
            "completed_days": len(completed),
            "in_progress_days": len(in_progress),
            "practice_completed_days": practice_counts.get("실천했다", 0),
            "practice_partial_days": practice_counts.get("일부 실천했다", 0),
        }
        if totals != observed:
            raise ValueError(
                "집계 요약과 날짜별 기록이 일치하지 않습니다. "
                f"summary={totals}, observed={observed}"
            )

    categories = Counter(record["category"] for record in records if record.get("category"))
    return {
        **totals,
        "curated_record_count": len(records),
        "curated_ability_count": len(categories),
        "curated_category_counts": dict(categories),
    }


def main():
    records = load_json(INPUT_FILE)
    ritual_days = load_json(RITUAL_DAYS_FILE)
    summary = load_json(SUMMARY_FILE)
    stats = build_stats(records, ritual_days, summary)

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_FILE.open("w", encoding="utf-8") as file:
        json.dump(stats, file, ensure_ascii=False, indent=2)

    print(json.dumps(stats, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
