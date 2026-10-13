# Student Grade Calculator


def get_grade(marks):
    if marks >= 90:
        return "A", "Excellent work! 🌟"
    elif marks >= 80:
        return "B", "Very Good! Keep it up! 👍"
    elif marks >= 70:
        return "C", "Good job! You can do even better! 😊"
    elif marks >= 60:
        return "D", "You passed! A little more effort will help! 💪"
    else:
        return "F", "Don't give up! Keep practicing! 📚"


def get_valid_marks():
    while True:
        try:
            marks = float(input("Enter marks (0-100): "))
            if 0 <= marks <= 100:
                return marks
            else:
                print("Marks must be between 0 and 100. Try again.")
        except ValueError:
            print("Please enter a number. Try again.")


name = input("Enter student name: ")
marks = get_valid_marks()
grade, message = get_grade(marks)

print()
print(f"📊 RESULT FOR {name.upper()}:")
print(f"Marks: {marks:g}/100")
print(f"Grade: {grade}")
print(f"Message: {message}")
