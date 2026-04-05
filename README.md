# AI-Fake-News-Detection
# 📰 Fake News Detection AI

An AI-powered web application that classifies news articles as **Fake or Real** using **Natural Language Processing (NLP)** and **Machine Learning**.

---

## 🚀 Overview

Fake news is a major issue in today’s digital world. This project detects whether a news article is fake or real by analyzing its text using machine learning techniques.

The system uses **TF-IDF vectorization** and a **Logistic Regression model**, along with a **Streamlit web app** for real-time predictions.

---

## 🧠 Features

- Detects fake vs real news using AI  
- Accepts user input (headline or full article)  
- Provides instant predictions  
- Uses NLP for text processing  
- Interactive web interface using Streamlit  

---

## 🛠️ Tech Stack

- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- NLP (TF-IDF Vectorization)  
- Logistic Regression  
- Streamlit  
- Matplotlib & Seaborn  

---

## 📂 Dataset

- Dataset contains **40,000+ news articles**  
- Files used:
  - Fake.csv  
  - True.csv  

⚠️ Note: Dataset is not included in this repository due to large file size.

---

## ⚙️ How It Works

1. Load fake and real news datasets  
2. Clean and preprocess text data  
3. Convert text into numerical format using TF-IDF  
4. Train a Logistic Regression model  
5. Predict whether input news is Fake or Real  

---

## 💻 How to Run 

1. Clone the repository: git clone https://github.com/yourusername/AI-Fake-News-Detection.git
2. Install dependencies:pip install -r requirements.txt
3. Run the app: streamlit run app.py
4. Open in browser: http://localhost:8501


---

## 📁 Project Structure
AI-Fake-News-Detection
│
├── app.py
├── fake_news_model.py
├── visualization.py
├── requirements.txt
└── README.md



---

## 📈 Results

- Accurate classification using Logistic Regression  
- Efficient text processing with TF-IDF  
- Real-time predictions via Streamlit  

---

## 🔮 Future Improvements

- Add prediction confidence score  
- Use advanced models (BERT, LSTM)  
- Improve UI/UX design  
- Deploy the app online  

---

## 👨‍💻 Author

Sahil Desai  
Computer Engineering Student  

---

## 📌 Conclusion

This project demonstrates how **AI and data analytics** can be used to solve real-world problems like fake news detection using machine learning and NLP.

---
