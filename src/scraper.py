# src/scraper.py
from google_play_scraper import reviews
import json
import os
from datetime import datetime


def scrape_reviews(package_name="com.supercell.clashroyale", total=1000, lang='id', country='id'):
    all_reviews = []
    token = None

    while len(all_reviews) < total:
        r, token = reviews(
            package_name,
            lang=lang,
            country=country,
            sort=1,  # terbaru
            count=200,
            continuation_token=token
        )
        all_reviews.extend(r)
        if not token:
            break

    print(f"Total komentar diambil: {len(all_reviews)}")
    return all_reviews


def convert_datetime(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")

def save_reviews(reviews, filename="data/raw/clash_royale_reviews_raw.json"):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(reviews, f, ensure_ascii=False, indent=2, default=convert_datetime)

