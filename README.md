# 🚀 ProductHunt Trendy Dashboard

Welcome to the **ProductHunt Trendy Dashboard** — a beautifully designed, data-rich, and interactive web app built using **Streamlit**.

This project analyzes trending product launches on [ProductHunt](https://www.producthunt.com/) to uncover what makes a product go viral — using real metrics like upvotes, comments, tags, and categories.

## 🔍 Why This Dashboard?

ProductHunt is a launchpad for tech products. But what makes a product **"trendy"** or **"viral"**?

This dashboard helps you:
- 📈 Analyze product trends and engagement
- 💡 Discover what works in product launches
- 🎯 Make data-driven launch decisions

## 📊 Features

### ✅ Overview
- Filter & sort top 10 trending products by:
  - 🔼 Upvotes
  - 💬 Comments
  - 🔤 A–Z
- View product descriptions, tags, and categories
- Instant score calculation: `Score = Upvotes + Comments`

### 🧠 Insights
- 📊 WordCloud of most used tags
- 📈 Category vs Tags usage flowchart
- 🧮 Engagement metrics visualized
- 🧾 Descriptive insights on emoji legends and scoring

### 💾 Export
- Download raw data in `.csv` format
- Snapshot-ready for analysis or portfolio projects

### 💡 Tips & Tricks
- Insights to help **launch better**
- Real-world observations from the data

## 🧠 How to Run

```bash
# Clone the repo
git clone https://github.com/Anushri2312/producthunt-trendy-dashboard.git
cd producthunt-trendy-dashboard

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py

**Live Demo** : https://huntvibecoder.streamlit.app/
