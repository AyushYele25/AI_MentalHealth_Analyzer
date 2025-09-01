# utils/analyze_text.py
from transformers import pipeline

# Force PyTorch backend
sentiment_classifier = pipeline(
    "text-classification",
    model="distilbert-base-uncased-finetuned-sst-2-english",
    framework="pt"  # force PyTorch
)

def predict_mental_state(text):
    """
    Input: text string
    Output: label (Anxiety, Depression/Stress, Positive/Neutral, Neutral) and confidence score
    """

    text_lower = text.lower()

    # 1️⃣ Keyword-based detection
    if any(word in text_lower for word in ['anxious', 'anxiety', 'nervous', 'worried', 'panic']):
        return 'Anxiety', 0.95
    elif any(word in text_lower for word in ['depressed', 'depression', 'sad', 'unhappy', 'lonely', 'stress']):
        return 'Depression/Stress', 0.95
    elif any(word in text_lower for word in ['happy', 'joy', 'excited', 'good', 'great', 'motivated']):
        return 'Positive/Neutral', 0.95
    else:
        # fallback to sentiment model
        result = sentiment_classifier(text[:512])  # limit to 512 tokens
        label = result[0]['label']
        score = result[0]['score']

        if label == 'POSITIVE':
            return 'Positive/Neutral', score
        else:
            return 'Depression/Stress', score
        