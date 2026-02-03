import streamlit as st
from utils.state import init_state

init_state(st)

st.header("⚠️ Phishing Risk Scores")

data = st.session_state.analysis

if not data:
    st.warning("Run analysis first")
else:
    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "📧 Email Phishing %",
            f"{data['email_phishing_score']}%"
        )
        st.caption(data["email_reason"])

    with col2:
        st.metric(
            "🔗 URL Phishing %",
            f"{data['url_phishing_score']}%"
        )
        st.caption(data["url_reason"])

    st.divider()

    st.metric(
        "🚨 FINAL RISK SCORE",
        f"{data['final_score']}%"
    )

    st.write("**Detected Domain:**", data["domain"])