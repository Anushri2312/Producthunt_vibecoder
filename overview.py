import streamlit as st
import pandas as pd

def show(data):
    st.title("🏠 Trending Product Overview")

    all_tags = sorted({tag for p in data for tag in p["tags"]})
    selected_tag = st.selectbox("Filter by tag", ["All"] + all_tags)
    sort_by = st.radio("Sort by", ["Upvotes", "Comments", "A–Z"], horizontal=True)

    if selected_tag != "All":
        filtered = [p for p in data if selected_tag in p["tags"]]
    else:
        filtered = data

    if sort_by == "Upvotes":
        filtered.sort(key=lambda x: x["upvotes"], reverse=True)
    elif sort_by == "Comments":
        filtered.sort(key=lambda x: x["comments"], reverse=True)
    else:
        filtered.sort(key=lambda x: x["name"])

    for p in filtered:
        score = p["upvotes"] * 2 + p["comments"]
        vibe = "🔥" if score > 2000 else "🚀" if score > 1000 else "💡"
        st.markdown(f"""
            <div style='border:1px solid #eee; padding:10px; border-radius:10px;'>
            <h4>{vibe} {p['name']}</h4>
            <p>{p['tagline']}</p>
            <p><b>Tags:</b> {", ".join(p['tags'])}</p>
            <p>⬆️ {p['upvotes']} &nbsp;&nbsp; 💬 {p['comments']} &nbsp;&nbsp; 🌟 Score: {score}</p>
            </div>
        """, unsafe_allow_html=True)

    with st.expander("📋 View All Products in Table"):
        df = pd.DataFrame(filtered)
        df["score"] = df["upvotes"] * 2 + df["comments"]
        st.dataframe(df[["name", "tagline", "upvotes", "comments", "score", "tags"]])
