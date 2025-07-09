import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import plotly.express as px

st.set_page_config(layout="wide")
st.title("🎮 Clash Royale User Reviews Insights")

DATA_PATH = "labeled/clash_royale_reviews_labeled.csv"

@st.cache_data
def load_data():
    return pd.read_csv(DATA_PATH)

df = load_data()

# Validasi kolom
if "sentiment_label" not in df.columns or "content" not in df.columns:
    st.error("Dataset tidak memiliki kolom 'sentiment_label' dan 'content'.")
    st.stop()

# ------------------------- 📊 SENTIMEN DINAMIS --------------------------
st.header("📊 Insight Hasil Analisis Komentar Pengguna")

sentiment_counts = df["sentiment_label"].value_counts()
total_comments = len(df)

st.markdown(f"""
### 🎯 Highlight Insight Komentar Pengguna Clash Royale

#### 📌 1. Distribusi Sentimen
Dari total **{total_comments} komentar**, berikut adalah distribusi sentimennya:
""")

# Tabel jumlah
st.dataframe(sentiment_counts.rename_axis("Sentimen").reset_index(name="Jumlah Komentar"))

# Visual
fig_sentiment = px.bar(
    sentiment_counts,
    x=sentiment_counts.index,
    y=sentiment_counts.values,
    labels={"x": "Sentimen", "y": "Jumlah Komentar"},
    title="Distribusi Sentimen Komentar"
)
st.plotly_chart(fig_sentiment, use_container_width=True)

# ---------------------- ☁️ WORDCLOUD PER SENTIMEN ----------------------
st.markdown("#### ☁️ 2. Wordcloud Berdasarkan Sentimen")

col1, col2, col3 = st.columns(3)

for sentiment, col in zip(["positive", "neutral", "negative"], [col1, col2, col3]):
    with col:
        st.subheader(sentiment.capitalize())
        text = " ".join(df[df["sentiment_label"] == sentiment]["content"].astype(str))
        if text.strip():
            wordcloud = WordCloud(width=400, height=300, background_color="white").generate(text)
            fig, ax = plt.subplots()
            ax.imshow(wordcloud, interpolation="bilinear")
            ax.axis("off")
            st.pyplot(fig)
        else:
            st.warning(f"Tidak ada komentar dengan sentimen: {sentiment}.")

# ---------------------- 🧠 DUMMY TOPIK MODELING -----------------------
st.markdown("""
#### 🧠 3. Highlight Topik Utama (Contoh dari LDA)
Berikut beberapa topik yang sering muncul berdasarkan LDA (ini contoh, ubah sesuai model kamu):

- **Topik 0**: Supercell, mode permainan, komunitas → mayoritas positif.
- **Topik 10**: Pay to Win dan ketimpangan → mayoritas negatif.
- **Topik 4**: Masalah jaringan dan lag → dominan negatif.
- **Topik 13 & 17**: Matchmaking dan sistem tidak adil → dikeluhkan pemain.

#### 🔍 4. Insight Strategis
- 🎯 *Perbaikan*: Sistem matchmaking dan performa jaringan.
- 💡 *Peluang*: Tonjolkan sisi strategi dan komunitas dalam promosi game.
""")
