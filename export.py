import streamlit as st
import pandas as pd

def show(data):
    st.title("📥 Export Data")
    df = pd.DataFrame(data)
    st.download_button("Download CSV", df.to_csv(index=False), "producthunt_data.csv", "text/csv")
