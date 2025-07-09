import pandas as pd
import os
import sys

# Import fungsi prediksi dari src/
sys.path.append(os.path.abspath("src"))
from sentiment_indobert import predict_sentiment

# Load data CSV
df = pd.read_csv("data/processed/clash_royale_reviews_clean.csv")

# Pastikan kolom content tersedia
if "content" not in df.columns:
    raise ValueError("Kolom 'content' tidak ditemukan dalam dataset.")

# Prediksi sentimen
print("🔍 Melabeli sentimen menggunakan IndoBERT...")
df["sentiment_label"] = predict_sentiment(df["content"].tolist())

# Simpan ke folder labeled/
os.makedirs("labeled", exist_ok=True)
df.to_csv("labeled/clash_royale_reviews_labeled.csv", index=False)
print("✅ Data sudah dilabeli dan disimpan di 'labeled/clash_royale_reviews_labeled.csv'")
