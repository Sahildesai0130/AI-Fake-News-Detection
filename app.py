import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Page config
st.set_page_config(
    page_title="Fake News Detection AI",
    page_icon="📰",
    layout="wide"
)

# Header
st.title("📰 Fake News Detection AI")
st.markdown("### Detect whether a news article is **Real or Fake** using Machine Learning")

st.write(
"This tool analyzes news text and predicts whether it is likely fake or real using an NLP model."
)

# Sidebar
st.sidebar.title("About")

st.sidebar.info(
"""
This project uses **Natural Language Processing (NLP)** and
**Machine Learning** to classify news articles as Fake or Real.

Built using:
- Python
- Scikit-learn
- Streamlit
"""
)

# Load dataset
fake = pd.read_csv("Fake.csv")
true = pd.read_csv("True.csv")

fake["label"] = 0
true["label"] = 1

data = pd.concat([fake, true])

X = data["text"]
y = data["label"]

# Train model
vectorizer = TfidfVectorizer(stop_words="english")
X_vectorized = vectorizer.fit_transform(X)

model = LogisticRegression()
model.fit(X_vectorized, y)

# Input section
st.subheader("Enter News Text")

news_input = st.text_area(
    "Paste a news headline or article below:",
    height=200
)

# Centered button
col1, col2, col3 = st.columns([1,2,1])

with col2:
    check = st.button("🔍 Analyze News")

# Prediction
if check:

    if news_input.strip() == "":
        st.warning("⚠ Please enter some news text.")
    else:
        news_vector = vectorizer.transform([news_input])
        prediction = model.predict(news_vector)

        st.subheader("Result")

        if prediction[0] == 0:
            st.error("🚨 This news appears to be FAKE")
        else:
            st.success("✅ This news appears to be REAL")