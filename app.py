import streamlit as st
from utils.load_data import load_producthunt_data
from pages import about, overview, insights, export, tips

st.set_page_config(page_title="Product Hunt Dashboard", layout="wide")
st.sidebar.title("🔍 Navigation")
page = st.sidebar.radio("Go to", ["📘 About", "🏠 Overview", "📊 Insights", "📥 Export", "🧠 Tips"])

data = load_producthunt_data()

if page == "📘 About":
    about.show()
elif page == "🏠 Overview":
    overview.show(data)
elif page == "📊 Insights":
    insights.show(data)
elif page == "📥 Export":
    export.show(data)
elif page == "🧠 Tips":
    tips.show()
