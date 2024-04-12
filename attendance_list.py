students_list = {"Andy":"Present", "Lucia":"Present", "Alice":"Absent", "John":"Present", "Doe":"Absent"}

for student, status in students_list.copy().items():
    if status == "Absent":
        del students_list[student]

present_student = {}
for student, status in students_list.items():
    if status == "Present":
        present_student[student] = status

print(present_student)
print(students_list)