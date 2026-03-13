# ==========================================
# TASK 3: Conditional Statements & Logical Flow
# Grade Calculator Program
# ==========================================

try:
    # Taking marks input from user
    marks = int(input("Enter marks (0–100): "))

    # Checking for invalid marks
    if marks < 0 or marks > 100:
        print("Invalid marks! Please enter a value between 0 and 100.")

    # Grade A / A+ (Nested condition)
    elif marks >= 90:
        if marks > 95:
            print("Grade: A+")
            print("Remark: Top Performer!")
        else:
            print("Grade: A")
            print("Remark: Excellent performance.")

    # Grade B (Logical AND)
    elif marks >= 75 and marks < 90:
        print("Grade: B")
        print("Remark: Very good.")

    # Grade C
    elif marks >= 60:
        print("Grade: C")
        print("Remark: Good effort.")

    # Grade D
    elif marks >= 40:
        print("Grade: D")
        print("Remark: Needs improvement.")

    # Fail case
    else:
        print("Grade: F")
        print("Remark: Failed. Better luck next time.")

# Handling non-numeric input
except ValueError:
    print("Invalid input! Please enter numeric marks only.")