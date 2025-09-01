# app.py
import streamlit as st
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.ocr import extract_text_pytesseract
from utils.analyze_text import predict_mental_state
from utils.health_tips import get_health_tips

st.set_page_config(page_title="Mental Health Analyzer", layout="wide")
st.title("🧠 Mental Health Analyzer & Daily Tips")

choice = st.radio("Choose input type:", ("Text", "Image"))

if choice == "Text":
    user_text = st.text_area("Enter your thoughts or feelings here:")
    if st.button("Analyze Text"):
        if user_text.strip() == "":
            st.warning("Please enter some text to analyze.")
        else:
            label, confidence = predict_mental_state(user_text)
            st.success(f"Predicted Mental State: {label} (Confidence: {confidence})")
            tips = get_health_tips(label)
            st.subheader("💡 Daily Health Tips / Routine")
            for t in tips:
                st.write("- " + t)

elif choice == "Image":
    uploaded_file = st.file_uploader("Upload an image containing text:")
    if uploaded_file is not None:
        if st.button("Analyze Image"):
            try:
                extracted_text = extract_text_pytesseract(uploaded_file)
                st.subheader("📄 Extracted Text")
                st.write(extracted_text)
                
                label, confidence = predict_mental_state(extracted_text)
                st.success(f"Predicted Mental State: {label} (Confidence: {confidence})")
                
                tips = get_health_tips(label)
                st.subheader("💡 Daily Health Tips / Routine")
                for t in tips:
                    st.write("- " + t)
            except Exception as e:
                st.error(f"Error processing image: {e}")

