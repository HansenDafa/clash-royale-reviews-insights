import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(layout="wide")
st.title("🎮 Clash Royale User Reviews Insights")

# Load data lokal
@st.cache_data
def load_data():
    return pd.read_csv("/home/xerces/project/clash-royale-reviews-insights/data/processed/clash_royale_reviews_clean.csv")

df = load_data()

# Sidebar filter
st.sidebar.header("🔎 Filter")
sentiment_filter = st.sidebar.multiselect("Pilih Sentimen:", options=df["sentiment_label"].unique(), default=df["sentiment_label"].unique())
filtered_df = df[df["sentiment_label"].isin(sentiment_filter)]

# Statistik Sentimen
st.header("📊 Distribusi Sentimen Komentar")
sentiment_count = filtered_df["sentiment_label"].value_counts().reset_index()
sentiment_count.columns = ["Sentiment", "Jumlah"]
fig_sentiment = px.pie(sentiment_count, names='Sentiment', values='Jumlah', color='Sentiment',
                       color_discrete_map={"Positif": "green", "Netral": "gray", "Negatif": "red"},
                       title="Proporsi Sentimen Komentar Pengguna")
st.plotly_chart(fig_sentiment, use_container_width=True)

# Wordcloud per sentimen
st.header("☁️ Wordcloud Berdasarkan Sentimen")
col1, col2, col3 = st.columns(3)
for sentiment, col in zip(["Positif", "Netral", "Negatif"], [col1, col2, col3]):
    with col:
        st.subheader(sentiment)
        text = " ".join(filtered_df[filtered_df["sentiment_label"] == sentiment]["content"].dropna())
        wc = WordCloud(width=300, height=200, background_color="white").generate(text)
        fig, ax = plt.subplots(figsize=(4, 3))
        ax.imshow(wc, interpolation='bilinear')
        ax.axis("off")
        st.pyplot(fig)

# Topik
st.header("🧠 Topik Komentar (Topic Modeling)")
topic_dist = filtered_df["topic"].value_counts().reset_index()
topic_dist.columns = ["Topik", "Jumlah"]
fig_topic = px.bar(topic_dist.sort_values("Jumlah", ascending=False).head(10), x="Topik", y="Jumlah",
                   title="10 Topik Komentar Terpopuler", color="Jumlah", color_continuous_scale="viridis")
st.plotly_chart(fig_topic, use_container_width=True)

# Heatmap Topik vs Sentimen
st.header("📌 Korelasi Sentimen dengan Topik")
heatmap_df = pd.crosstab(filtered_df["topic"], filtered_df["sentiment_label"])
fig_heatmap = px.imshow(heatmap_df, text_auto=True, aspect="auto",
                        color_continuous_scale="RdBu_r", title="Heatmap Sentimen terhadap Topik")
st.plotly_chart(fig_heatmap, use_container_width=True)

# Kesimpulan
st.header("📝 Insight Strategis")
st.markdown("""
- **Topik-topik seperti koneksi, bug, dan sistem matchmaking mendominasi sentimen negatif**.
- **Komentar positif biasanya membahas strategi permainan dan keseruan bermain**.
- **Rekomendasi untuk developer**: Perbaiki sistem matchmaking, kurangi lag, dan optimalkan pengalaman pengguna.
- **Peluang**: Promosi fitur strategis dan komunitas dapat meningkatkan persepsi positif.
""")
