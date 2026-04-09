# test_main.py

from main import calculate_average, assign_grade


def test_calculate_average():
    assert calculate_average([80, 90, 100]) == 90
    assert calculate_average([50, 50]) == 50
    assert calculate_average([]) == 0


def test_assign_grade():
    assert assign_grade(85) == "A"
    assert assign_grade(75) == "B"
    assert assign_grade(65) == "C"
    assert assign_grade(55) == "D"
    assert assign_grade(40) == "F"