import streamlit as st
from core.trends import get_trend
from core.scorer import calculate_score
from core.detector import detect_explosion
from scraper.shopee import scrape_shopee
from scraper.tiktok import scrape_tiktok

from utils.chart import trend_chart
from utils.style import load_css
from utils.components import metric_card

st.markdown(load_css(), unsafe_allow_html=True)

st.title("🚀 TrendHunter PRO")

keyword = st.text_input("Cari produk...")

if st.button("Analisa"):
    data = get_trend(keyword)

    if not data.empty:
        score = calculate_score(data.iloc[:,0])
        status = detect_explosion(data.iloc[:,0])

        col1, col2 = st.columns(2)

        with col1:
            metric_card("Viral Score", score)

        with col2:
            metric_card("Status", status)

        st.plotly_chart(trend_chart(data, keyword))

        st.subheader("🛒 Shopee")
        st.write(scrape_shopee(keyword))

        st.subheader("📱 TikTok")
        st.write(scrape_tiktok(keyword))
