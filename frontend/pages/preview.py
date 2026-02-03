import streamlit as st
from utils.state import init_state

init_state(st)

st.header("📄 Email Preview")

if not st.session_state.email_body:
    st.warning("No email submitted yet")
else:
    st.markdown(
        f"""
        <div style="
            background:#ffffff;
            padding:20px;
            border-radius:10px;
            border:1px solid #ddd;
            line-height:1.6;">
            {st.session_state.email_body.replace("\n","<br>")}
        </div>
        """,
        unsafe_allow_html=True
    )