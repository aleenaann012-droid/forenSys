import streamlit as st
from utils.helpers import is_valid_url
from utils.api_client import analyze
from utils.state import init_state

init_state(st)

st.header("📩 Email & URL Input")

email = st.text_area(
    "Email Content",
    height=250,
    placeholder="Paste the email content here..."
)

url = st.text_input(
    "Suspicious URL (optional)",
    placeholder="https://example.com"
)

if st.button("🔍 Analyze", use_container_width=True):
    if not email.strip():
        st.error("Email content is required")
    elif url and not is_valid_url(url):
        st.error("Invalid URL format")
    else:
        st.session_state.email_body = email
        st.session_state.url = url
        st.session_state.analysis = analyze(email, url)
        st.success("Analysis completed. Go to next page ▶️")