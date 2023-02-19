student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Braco": 74,
    "Neville": 62,
}

student_grades = {}
for i in student_scores:
    student_grades[i] = student_scores[i]
print(student_grades)

for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds expectation"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"


print(student_grades)