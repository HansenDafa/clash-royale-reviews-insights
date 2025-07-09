# main.py
from src.scraper import scrape_reviews, save_reviews

if __name__ == "__main__":
    data = scrape_reviews(total=1000)
    save_reviews(data)
