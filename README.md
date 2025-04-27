# 🧠 Patient's Condition Classification Using Drug Reviews

This project uses Natural Language Processing (NLP) and Machine Learning to classify patient drug reviews into one of the following medical conditions:

- **Depression**
- **High Blood Pressure**
- **Diabetes, Type 2**

It helps understand how patients feel about medications based on their reviews and predicts their condition from the review text.

---

## 📊 Dataset

- Source: [Drugs.com Reviews Dataset](https://www.kaggle.com/datasets/jessicali9530/drugscom)
- Total Reviews: ~161,000
- Filtered for 3 conditions listed above

---

## 🧪 Features Used

- **Review** (text)  
- **Rating** (0–10 stars)  
- **Useful Count** (helpfulness votes)  
- **Cleaned text** using NLTK preprocessing  
- **Review length** calculated as a feature  

---

## 🧠 Models Trained

| Model                | Accuracy |
|---------------------|----------|
| Logistic Regression | 94.9%    |
| Naive Bayes         | 92.7%    |
| Random Forest       | 95.5%    |
| **SVM (LinearSVC)** | **96.1% ✅ Final model**

---

## ⚙️ Tech Stack

- Python
- Pandas, NumPy, Scikit-learn, NLTK
- Streamlit for UI
- joblib for model saving
- Google Colab for training

---

## 🚀 How to Run

### Locally:
1. Clone the repo
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
