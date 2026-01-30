students = [
    {"roll": 1, "name": "Ankit", "marks": 85},
    {"roll": 2, "name": "Riya", "marks": 92},
    {"roll": 3, "name": "Aman", "marks": 78}
]
def sort_by_marks(students):
    n = len(students)
    for i in range(n):
        for j in range(0, n - i - 1):
            if students[j]["marks"] > students[j + 1]["marks"]:
                students[j], students[j + 1] = students[j + 1], students[j]
    return students
if __name__ == "__main__":
    sorted_students = sort_by_marks(students)
    for student in sorted_students:
        print(f'Roll: {student["roll"]}, Name: {student["name"]}, Marks: {student["marks"]}')