from PIL import Image
import pytesseract
import easyocr
import os

# -------------------------------
# OCR Functions
# -------------------------------
def extract_text_pytesseract(image_path):
    """Extract text using pytesseract"""
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text.strip()

def extract_text_easyocr(image_path):
    """Extract text using easyocr"""
    reader = easyocr.Reader(['en'])
    result = reader.readtext(image_path, detail=0)
    return " ".join(result).strip()

# -------------------------------
# Test Image Path
# -------------------------------
image_path = r"C:\Users\ayush\Downloads\Sentences-with-Depression-Depression-in-a-Sentence-in-English-Sentences-for-Depression.webp"

if not os.path.exists(image_path):
    raise FileNotFoundError(f"Image not found: {image_path}")

# -------------------------------
# Run OCR
# -------------------------------
print("---- Pytesseract OCR ----")
text_pytesseract = extract_text_pytesseract(image_path)
print(text_pytesseract)

print("\n---- EasyOCR ----")
text_easyocr = extract_text_easyocr(image_path)
print(text_easyocr)
