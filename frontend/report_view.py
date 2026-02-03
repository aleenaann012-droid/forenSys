import streamlit as st
import pandas as pd

def show_report(data):
    st.subheader("🧪 Analysis Report")

    st.write("**URL:**", data["url"])
    st.write("**Verdict:**", data["verdict"])
    st.write("**Risk Score:**", data["final_score"])

    st.subheader("Feature Tests")
    df = pd.DataFrame(data["features"])
    st.table(df)