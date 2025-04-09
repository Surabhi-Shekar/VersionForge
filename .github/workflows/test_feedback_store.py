# test_feedback_store.py

import feedback_store

def test_add_feedback():
    feedback_store.feedback_data.clear()  # Reset before test
    feedback_store.add_feedback("Sam", 8)
    assert feedback_store.feedback_data == [{"name": "Sam", "score": 8}]

def test_calculate_average():
    feedback_store.feedback_data.clear()
    feedback_store.add_feedback("Sam", 9)
    feedback_store.add_feedback("Alex", 7)
    assert feedback_store.calculate_average() == 8.0
