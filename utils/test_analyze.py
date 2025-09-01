# test_analyze.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.ocr import extract_text_pytesseract
from utils.analyze_text import predict_mental_state

image_path = r"C:\Users\ayush\Downloads\Sentences-with-Depression-Depression-in-a-Sentence-in-English-Sentences-for-Depression.webp"

# Step 1: Extract text
text = extract_text_pytesseract(image_path)
print("Extracted Text:\n", text)

# Step 2: Predict mental state
label, confidence = predict_mental_state(text)
print("\nPredicted Mental State:", label)
print("Confidence:", confidence)
