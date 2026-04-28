import streamlit as st

def metric_card(title, value):
    st.markdown(f"""
    <div class="card">
        <b>{title}</b><br>
        <h2>{value}</h2>
    </div>
    """, unsafe_allow_html=True)
