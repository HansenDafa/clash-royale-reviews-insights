# main.py
from src.scraper import scrape_reviews, save_reviews

if __name__ == "__main__":
    data = scrape_reviews(total=1000)
    save_reviews(data)

# main.py (lanjutan)

from src.preprocess import load_reviews, preprocess, save_cleaned

if __name__ == "__main__":
    data = scrape_reviews(total=1000)
    save_reviews(data)

    # Proses data
    df_raw = load_reviews()
    df_clean = preprocess(df_raw)
    save_cleaned(df_clean)
    print("✅ Data preprocessing selesai dan disimpan di CSV.")
