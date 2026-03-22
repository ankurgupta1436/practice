# Student Result System

name = input("Enter student name: ")
roll = input("Enter roll number: ")

subjects = 5
total_marks = 0

for i in range(subjects):
    marks = int(input(f"Enter marks for subject {i+1}: "))
    total_marks += marks

percentage = total_marks / subjects

# Grade Calculation
if percentage >= 90:
    grade = 'A+'
elif percentage >= 75:
    grade = 'A'
elif percentage >= 60:
    grade = 'B'
elif percentage >= 50:
    grade = 'C'
else:
    grade = 'Fail'

# Output
print("\n--- Result ---")
print("Name:", name)
print("Roll No:", roll)
print("Total Marks:", total_marks)
print("Percentage:", percentage)
print("Grade:", grade)