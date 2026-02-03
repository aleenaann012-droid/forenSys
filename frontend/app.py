import streamlit as st
from utils.state import init_state

st.set_page_config(
    page_title="Phishing DNA",
    layout="wide"
)

init_state(st)

st.title("🧬 Phishing DNA Dashboard")
st.caption("Email, URL & Visual Phishing Detection System")

st.markdown(
    "➡️ Use the **sidebar** to move through each analysis step."
)