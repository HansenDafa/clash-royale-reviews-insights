import json
import pandas as pd
import os
import re

def load_reviews(json_path="data/raw/clash_royale_reviews_raw.json"):
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return pd.DataFrame(data)

def clean_text(text):
    if not isinstance(text, str):
        return ""
    text = re.sub(r"http\S+", "", text)  # hapus link
    text = re.sub(r"\s+", " ", text)     # hapus spasi berlebih
    return text.strip()

def preprocess(df):
    df = df.copy()
    df["content"] = df["content"].apply(clean_text)
    df = df[df["content"] != ""]                      # buang komentar kosong
    df["length"] = df["content"].apply(len)           # panjang komentar
    df["at"] = pd.to_datetime(df["at"])               # pastikan datetime format
    return df[["userName", "score", "content", "length", "at"]]

def save_cleaned(df, output_path="data/processed/clash_royale_reviews_clean.csv"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
