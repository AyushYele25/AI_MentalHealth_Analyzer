# health_tips.py

def get_health_tips(state):
    """
    Return daily health tips based on the mental state.
    """
    state = state.strip()  # Remove extra spaces
    tips_dict = {
        "Depression/Stress": [
            "Go outside and get sunlight daily.",
            "Exercise 20-30 minutes each day.",
            "Maintain a consistent sleep schedule (7-9 hours).",
            "Practice mindfulness or meditation.",
            "Connect with friends or family and share your feelings."
        ],
        "Anxiety": [
            "Practice deep breathing exercises.",
            "Write down your worries and possible solutions.",
            "Limit caffeine and sugar intake.",
            "Take short breaks from stressful activities.",
            "Engage in hobbies that relax your mind."
        ],
        "Positive/Neutral": [
            "Keep up your good mental habits.",
            "Maintain regular exercise and healthy diet.",
            "Continue connecting with loved ones.",
            "Try new activities that make you happy."
        ]
    }
    # Default tips if the state is unknown
    return tips_dict.get(state, ["Maintain a healthy routine and positive mindset."])
