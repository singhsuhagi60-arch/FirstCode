"""
Your module description
"""
# Assignment Note: 
# This program asks the user to enter the names of three students and their marks in three subjects.
# It then displays each student’s name, their marks, their average score,
# and whether they have passed or failed based on their average.

# Function to calculate average and determine pass/fail
def evaluate_student(name, marks):
    average = sum(marks) / len(marks)
    status = "Passed" if average >= 30 else "Failed"
    print(f"\nStudent Name: {name}")
    print(f"Marks: {marks}")
    print(f"Average: {average:.2f}")
    print(f"Status: {status}")

# Main program
students_data = []

for i in range(3):
    name = input(f"\nEnter name of student {i + 1}: ")
    marks = []
    for j in range(3):
        mark = float(input(f"Enter mark for subject {j + 1}: "))
        marks.append(mark)
    students_data.append((name, marks))

print("\n--- Student Results ---")
for student in students_data:
    evaluate_student(student[0], student[1])
