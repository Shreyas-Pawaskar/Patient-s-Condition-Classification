
import streamlit as st
import joblib

# Load model and vectorizer
model = joblib.load('svm_model.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')

label_map = {0: "Depression", 1: "Diabetes, Type 2", 2: "High Blood Pressure"}

st.title("🧠 Patient's Condition Classifier")
st.subheader("Enter a drug review and let the model predict the condition...")

user_input = st.text_area("📝 Paste or write the patient's review here:")

if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        vec_input = vectorizer.transform([user_input])
        prediction = model.predict(vec_input)[0]
        st.success(f"🩺 Predicted Condition: **{label_map[prediction]}**")
