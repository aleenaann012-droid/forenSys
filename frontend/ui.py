import streamlit as st
from api_client import analyze_url
from report_view import show_report

st.set_page_config(page_title="Phish-DNA", layout="centered")

st.title("🔍 Phish-DNA")
st.subheader("Phishing Detection & Forensic Report")

url = st.text_input("Enter URL to analyze")

if st.button("Analyze"):
    if not url.strip():
        st.warning("Please enter a URL")
    else:
        result = analyze_url(url)
        show_report(result)