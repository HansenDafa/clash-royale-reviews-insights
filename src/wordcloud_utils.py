# src/wordcloud_utils.py
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import re

factory = StemmerFactory()
stemmer = factory.create_stemmer()

def preprocess_text(text):
    # Hilangkan karakter non-alfabet, angka, dll
    text = re.sub(r"[^a-zA-Z\s]", " ", text)
    text = text.lower()
    text = stemmer.stem(text)  # stemming
    return text

def generate_wordcloud(text, title=""):
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title(title, fontsize=16)
    plt.show()
