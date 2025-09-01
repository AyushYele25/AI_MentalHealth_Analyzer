# test_health_tips.py
from health_tips import get_health_tips

# List of example mental states
states = ["Depression/Stress", "Anxiety", "Positive/Neutral", "Unknown"]

for state in states:
    print(f"\nMental State: {state}")
    tips = get_health_tips(state)
    for tip in tips:
        print("-", tip)
