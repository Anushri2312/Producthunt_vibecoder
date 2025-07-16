import streamlit as st

def show():
    st.title("📘 About Product Hunt & This App")
    st.markdown("""
    **What is Product Hunt?**  
    Product Hunt is a place where new tech products are discovered daily.

    **Why this dashboard?**  
    - To analyze trends
    - Discover what works in launches
    - Use data to launch smarter

    **Emoji Legend:**
    - 🔥 > 2000 score = viral
    - 🚀 > 1000 score = trending
    - 💡 = moderate buzz
    - ⬆️ Upvotes = Likes
    - 💬 Comments = Discussion
    - 🌟 Score = Engagement Index
    """)
