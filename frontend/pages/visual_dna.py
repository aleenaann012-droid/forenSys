import streamlit as st
from utils.state import init_state

init_state(st)

st.header("🧬 Visual DNA Analysis")

data = st.session_state.analysis

if not data:
    st.warning("No analysis found")
else:
    similarity = int(data["visual_similarity"] * 100)

    st.metric("🖼 Visual Similarity", f"{similarity}%")
    st.progress(similarity)

    st.caption(data["visual_reason"])

    if similarity > 80:
        st.error("High visual impersonation detected")
    elif similarity > 50:
        st.warning("Moderate visual similarity detected")
    else:
        st.success("Low visual similarity")