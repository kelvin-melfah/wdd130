import csv

def load_students(filename):
    """Reads students.csv and returns a dictionary {id: name}"""
    students = {}

    try:
        with open(filename, mode="r") as file:
            reader = csv.reader(file)

            # Skip header
            next(reader)

            for row in reader:
                student_id = row[0]
                name = row[1]
                students[student_id] = name

    except FileNotFoundError:
        print("Error: File not found.")
    
    return students


def clean_id(user_id):
    """Removes dashes from ID"""
    return user_id.replace("-", "")


def validate_id(user_id):
    """Validates the ID number"""

    # Check invalid characters
    for char in user_id:
        if not (char.isdigit() or char == "-"):
            return "Invalid ID Number"

    # Remove dashes for length check
    clean = clean_id(user_id)

    if len(clean) < 6:
        return "Invalid ID Number: too few digits"
    elif len(clean) > 6:
        return "Invalid ID Number: too many digits"

    return clean


def main():
    students = load_students("students.csv")

    user_input = input("Enter student ID: ")

    result = validate_id(user_input)

    # If validation returns an error message
    if isinstance(result, str) and result.startswith("Invalid"):
        print(result)
        return

    # Otherwise it's a cleaned ID
    student_id = result

    if student_id in students:
        print("Student Name:", students[student_id])
    else:
        print("No such student")


# Run program
if __name__ == "__main__":
    main()