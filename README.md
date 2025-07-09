

```markdown
# 📊 Clash Royale Reviews Insights

Proyek ini bertujuan untuk **mengambil, membersihkan, menganalisis, dan memvisualisasikan** komentar pengguna dari Google Play Store terhadap game **Clash Royale**. Analisis mencakup *sentiment analysis*, *topic modeling*, dan visualisasi interaktif menggunakan **Streamlit**.

---

## 🔧 Struktur Proyek

```

clash-royale-reviews-insights/
│
├── app.py                         # Aplikasi Streamlit untuk visualisasi interaktif
├── labeled/
│   └── clash\_royale\_reviews\_with\_topic.csv   # Dataset final yang sudah diberi label sentimen dan topik
├── raw/
│   └── clash\_royale\_reviews\_raw\.json         # Hasil scraping awal dari Google Play
├── src/
│   ├── scraper.py                # Pengambil komentar dari Google Play Store
│   ├── sentiment\_indobert.py    # Analisis sentimen menggunakan IndoBERT
│   ├── topic\_modeling.py        # Model LDA untuk ekstraksi topik utama
├── insights.ipynb               # Notebook eksplorasi awal dan insight statis
├── requirements.txt             # Dependensi Python untuk proyek ini
└── README.md                    # Dokumentasi proyek

````

---

## 🚀 Cara Menjalankan

### 1. Kloning repositori dan masuk ke direktori

```bash
git clone https://github.com/username/clash-royale-reviews-insights.git
cd clash-royale-reviews-insights
````

### 2. Aktifkan environment Python

```bash
conda create -n play-insight python=3.10
conda activate play-insight
pip install -r requirements.txt
```

### 3. Jalankan aplikasi Streamlit

```bash
streamlit run app.py
```

---

## 📌 Fitur Analisis

### ✅ Sentiment Analysis (IndoBERT)

* Mengklasifikasi komentar menjadi: **positif**, **netral**, atau **negatif**.
* Model: [`hanifnoerr/Fine-tuned-Indonesian-Sentiment-Classifier`](https://huggingface.co/hanifnoerr/Fine-tuned-Indonesian-Sentiment-Classifier)

### ✅ Topic Modeling (LDA)

* Ekstraksi topik utama dari komentar pengguna.
* Topik seperti: *bug*, *lag*, *strategi permainan*, *sistem matchmaking*, dll.

### ✅ Visualisasi

* **Wordcloud** berdasarkan sentimen.
* **Distribusi sentimen & topik**.
* Insight interaktif dan dinamis di halaman Streamlit.

---

## 📈 Insight Utama

* Komentar terbagi rata antara positif, netral, dan negatif.
* Keluhan umum meliputi sistem matchmaking, lag, dan elemen *pay-to-win*.
* Topik dengan sentimen negatif didominasi oleh kata-kata seperti `lag`, `tidak adil`, `level`, `bug`.

---

## 📬 Kontribusi

Silakan buat pull request atau buka issue jika ingin berkontribusi atau menemukan bug.

---

## 📄 Lisensi

MIT License © 2025 Hansen Dafa

