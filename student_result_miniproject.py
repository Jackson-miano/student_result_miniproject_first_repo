import student_result_module
students =[]
num_students = int(input("how many students?"))
for i in range(num_students):
    name,registration_number,age,marks_list =student_result_module.get_student_marks()
    record = student_result_module.build_student_record(name,registration_number,age,marks_list)
    students.append(record)
    for student in students:
        print("-" * 30)
    print(f"Name: {student['name']}")
    print(f"Registration Number: {student['registration_number']}")
    print(f"Age: {student['age']}")
    print(f"Marks: {student['marks_list']}")
    print(f"Average: {student['average']:.2f}")
    print(f"Grade: {student['grade']}")
    print(f"Result: {student['classify_result']}")
print("-" * 30)
