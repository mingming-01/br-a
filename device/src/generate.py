import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_FILE = BASE_DIR / "input" / "records.json"
OUTPUT_FILE = BASE_DIR / "output" / "candidates.json"


def load_records():
    with INPUT_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)


def generate_candidates(records):
    candidates = []

    for record in records:
        candidates.append({
            "date": record["date"],
            "category": record["category"],
            "text": record["text"],
            "source_type": record["type"]
        })

    candidates.sort(key=lambda item: (item["category"], item["date"]))

    return candidates


def save_candidates(candidates):
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    with OUTPUT_FILE.open("w", encoding="utf-8") as file:
        json.dump(candidates, file, ensure_ascii=False, indent=2)


def main():
    records = load_records()
    candidates = generate_candidates(records)
    save_candidates(candidates)

    print(f"입력 기록: {len(records)}개")
    print(f"후보 기록: {len(candidates)}개")
    print(f"결과 파일: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
