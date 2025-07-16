import streamlit as st
import pandas as pd
import plotly.express as px
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def show(data):
    st.title("📊 Insights & Trends")

    # Tag distribution
    all_tags = [tag for p in data for tag in p["tags"]]
    tag_df = pd.DataFrame(Counter(all_tags).most_common(10), columns=["Tag", "Count"])
    st.subheader("Top Tags")
    st.plotly_chart(px.bar(tag_df, x="Tag", y="Count", color="Tag"))

    # Engagement comparison
    df = pd.DataFrame(data)
    top_df = df.sort_values("upvotes", ascending=False).head(15)
    st.subheader("Engagement: Upvotes vs Comments")
    fig = px.bar(top_df, x="name", y=["upvotes", "comments"], barmode="group")
    st.plotly_chart(fig)

    # WordCloud
    taglines = " ".join([p["tagline"] for p in data])
    wc = WordCloud(width=800, height=300, background_color='white').generate(taglines)
    st.subheader("Launch Copy WordCloud")
    fig2, ax = plt.subplots(figsize=(10, 3))
    ax.imshow(wc, interpolation="bilinear")
    ax.axis("off")
    st.pyplot(fig2)

    # st.image("flowchart.png", caption="Category to Tags Flow (Sample)")
    # st.image("https://i.imgur.com/b2nKp4a.png", caption="Category to Tags Flow (Sample)")
