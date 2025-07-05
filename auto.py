import csv
import subprocess
import time
import json
from pathlib import Path

SAVE_DIR = Path("autowini_json")
SAVE_DIR.mkdir(exist_ok=True)

CSV_FILE = Path("autowini_data.csv")
START_PAGE = 1
END_PAGE = 5398

FIELDS = [
    "code", "listingId", "itemName", "make", "subModel", "modelYear", "fuelType",
    "transmission", "steeringType", "engineVolume", "numberOfPassenger", "locationName",
    "price", "mileage", "odometerCheck", "mainThumbnailPath", "detailUrl"
]

def download_page(page: int) -> Path:
    temp_file = SAVE_DIR / f"page_{page}.json"
    url = f"https://v2api.autowini.com/items?pageOffset={page}"
    print(f"📦 Downloading page {page}")
    result = subprocess.run(
        ["curl", "-s", "-H", "Accept: application/json", url, "-o", str(temp_file)],
        capture_output=True
    )
    if result.returncode != 0:
        print(f"❌ curl failed on page {page}")
        return None

    if temp_file.exists():
        preview = temp_file.read_text(encoding="utf-8")[:500]
        print(f"🔍 Preview of page {page} JSON:\n{preview}\n{'-'*60}")
    return temp_file

def extract_items(json_path: Path):
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            items = data.get("data", {}).get("items", [])
            return items if isinstance(items, list) else []
    except Exception as e:
        print(f"❌ JSON parsing error in {json_path.name}: {e}")
        return []

def extract_row(item: dict):
    row = {field: item.get(field, "") for field in FIELDS}
    if row["detailUrl"]:
        row["detailUrl"] = "https://www.autowini.com" + row["detailUrl"]
    return row

def ensure_csv_header():
    if not CSV_FILE.exists():
        with CSV_FILE.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDS)
            writer.writeheader()

def main():
    ensure_csv_header()
    page = START_PAGE

    while page <= END_PAGE:
        json_file = download_page(page)
        if not json_file or not json_file.exists():
            print(f"❌ Retrying page {page} in 5 seconds...")
            time.sleep(5)
            continue

        items = extract_items(json_file)
        if not items:
            print(f"⚠️ No items found on page {page}. Retrying in 5 seconds...")
            json_file.unlink(missing_ok=True)
            time.sleep(5)
            continue

        with CSV_FILE.open("a", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDS)
            for item in items:
                row = extract_row(item)
                writer.writerow(row)

        print(f"✅ Saved {len(items)} listings from page {page}")
        json_file.unlink(missing_ok=True)
        page += 1
        time.sleep(0.5)

if __name__ == "__main__":
    main()
