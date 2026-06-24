
import streamlit as st
import joblib
import pandas as pd

st.set_page_config(
    page_title="SMS Spam Detector",
    page_icon="📩",
    layout="wide"
)

model = joblib.load("best_spam_classifier.pkl")

st.title("📩 SMS Spam Detector")

st.write(
    "Predict whether an SMS message is spam or legitimate."
)

messages = [
    "Free cash prize waiting",
    "Let's meet tomorrow",
    "Congratulations! You won a free iPhone",
    "See you at lunch"
]

msg = st.selectbox("Choose a message", messages)

if st.button("Predict"):
    pred = model.predict([msg])[0]
    st.write("SPAM" if pred else "HAM")
