import streamlit as st

def show():
    st.title("🧠 Tips & Metric Explanation")
    st.markdown("""
    ### ✨ What Makes Launches Successful?
    - Emotional, result-based taglines
    - Clear call to action
    - Smart tag/category pairing

    ### 📈 Metric Meaning
    - ⬆️ **Upvotes** = surface interest
    - 💬 **Comments** = engagement
    - 🌟 **Score** = combined signal of traction

    ```python
    score = upvotes * 2 + comments
    ```

    Use these metrics to analyze trends & launch better.
    """)
