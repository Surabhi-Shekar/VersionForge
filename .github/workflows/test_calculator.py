# test_calculator.py

from calculator import calculate_average, get_grade

def test_calculate_average():
    scores = [80, 90, 100]
    assert calculate_average(scores) == 90.0

def test_get_grade():
    average = 85
    assert get_grade(average) == "A"
