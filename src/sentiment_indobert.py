# src/sentiment_indobert.py
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

# Pilih model public
MODEL_NAME = "hanifnoerr/Fine-tuned-Indonesian-Sentiment-Classifier"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)

sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model=model,
    tokenizer=tokenizer
)

# Fungsi wrapper
def predict_sentiment(texts):
    results = sentiment_pipeline(texts, batch_size=16)
    return [r["label"].lower() for r in results]
