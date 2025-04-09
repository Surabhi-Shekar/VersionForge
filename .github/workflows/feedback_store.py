# feedback_store.py

import json
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "data.json")

def load_feedback():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_feedback(feedback_list):
    with open(DATA_FILE, "w") as f:
        json.dump(feedback_list, f, indent=2)

def add_feedback(entry):
    feedbacks = load_feedback()
    feedbacks.append(entry)
    save_feedback(feedbacks)

def calculate_average():
    feedbacks = load_feedback()
    if not feedbacks:
        return 0.0
    total = sum(entry['rating'] for entry in feedbacks)
    return round(total / len(feedbacks), 2)
