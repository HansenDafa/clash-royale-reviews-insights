import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import plotly.express as px

st.set_page_config(layout="wide")
st.title("🎮 Clash Royale User Reviews Insights")

# Load dataset lokal langsung
try:
    df = pd.read_csv("data/processed/clash_royale_reviews_clean.csv")
except FileNotFoundError:
    st.error("File data/cleaned_reviews.csv tidak ditemukan. Pastikan file tersedia.")
    st.stop()

# Info dasar
st.subheader("📌 Informasi Umum Dataset")
st.write(df.head())
st.write("Jumlah Komentar:", len(df))

# Sentimen distribution
st.subheader("📊 Distribusi Sentimen")
col1, col2 = st.columns([1, 2])
sentiment_column = None
for col in df.columns:
    if 'sentiment' in col and df[col].dtype == 'object':
        sentiment_column = col
        break

if sentiment_column:
    with col1:
        st.write(df[sentiment_column].value_counts())
    with col2:
        fig1 = px.histogram(df, x=sentiment_column, color=sentiment_column,
                            title="Jumlah Komentar per Sentimen")
        st.plotly_chart(fig1)

    # WordCloud
    st.subheader("☁️ Wordcloud Komentar berdasarkan Sentimen")
    sentiment_selected = st.selectbox("Pilih sentimen:", df[sentiment_column].unique())
    text_data = " ".join(df[df[sentiment_column] == sentiment_selected]["content"].astype(str))
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text_data)
    fig_wc, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis("off")
    st.pyplot(fig_wc)

    # Topic Modeling
    st.subheader("🧠 Distribusi Topik berdasarkan Sentimen")
    if "topic" in df.columns:
        df_topic = df[df["topic"] != -1]  # remove unassigned topics
        fig2 = px.histogram(df_topic, x="topic", color=sentiment_column,
                            barmode='group', title="Distribusi Topik per Sentimen")
        st.plotly_chart(fig2)

        # Topik spesifik
        topik_pilihan = st.selectbox("Lihat komentar berdasarkan topik:", sorted(df_topic["topic"].unique()))
        komentar_topik = df_topic[df_topic["topic"] == topik_pilihan][["content", sentiment_column]]
        st.write(f"Contoh komentar pada topik {topik_pilihan}:")
        st.dataframe(komentar_topik.sample(min(10, len(komentar_topik))))

    else:
        st.warning("Kolom 'topic' tidak ditemukan di dataset.")

else:
    st.error("Kolom sentimen tidak ditemukan. Pastikan ada kolom seperti 'sentiment_label' atau sejenisnya dengan tipe object.")
