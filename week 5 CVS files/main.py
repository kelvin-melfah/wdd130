# main.py
# Student Grade Analyzer Program
# This program reads student scores from a CSV file,
# calculates averages, assigns grades, and displays results.

import csv


def read_scores(filename):
    """
    Reads student scores from a CSV file.
    Returns a list of dictionaries.
    """
    students = []

    with open(filename, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Convert scores to integers
            row["score"] = int(row["score"])
            students.append(row)

    return students


def calculate_average(scores):
    """
    Calculates the average of a list of scores.
    """
    if len(scores) == 0:
        return 0

    return sum(scores) / len(scores)


def assign_grade(score):
    """
    Assigns a letter grade based on score.
    """
    if score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"


def group_by_student(data):
    """
    Groups scores by student name.
    Returns a dictionary.
    """
    result = {}

    for item in data:
        name = item["name"]
        score = item["score"]

        if name not in result:
            result[name] = []

        result[name].append(score)

    return result


def analyze_students(data):
    """
    Analyzes student data and returns summary.
    """
    grouped = group_by_student(data)
    summary = []

    for name, scores in grouped.items():
        avg = calculate_average(scores)
        grade = assign_grade(avg)

        summary.append({
            "name": name,
            "average": avg,
            "grade": grade
        })

    return summary


def display_results(summary):
    """
    Displays student results.
    """
    print("\nStudent Performance Report")
    print("-" * 30)

    for student in summary:
        print(f"{student['name']}: "
              f"Average = {student['average']:.2f}, "
              f"Grade = {student['grade']}")


def main():
    """
    Main function to run the program.
    """
    filename = "scores.csv"
    data = read_scores(filename)
    summary = analyze_students(data)
    display_results(summary)


# Run the program
if __name__ == "__main__":
    main()