def get_student_marks():
    name = input("Enter student name: ")
    registration_number = input("Enter registration_number:")
    age=int(input("Enter age:"))
    marks_list =[]
    for i in range(3):
        mark = float(input(f"Enter mark {i+1} for {name}: "))
        marks_list.append(mark)
    return name,registration_number,age, marks_list
def calculate_average(marks_list):
    return sum(marks_list) / len(marks_list)


def get_grade(average):
    if average >= 70:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    else:
        return "F"


def classify_result(average):
    if average >= 70:
        return "distinction"
    elif average >= 60:
        return "credit"
    elif average >= 50:
        return "pass"
    else:
        return "fail"


def build_student_record(name,registration_number,age, marks_list):
    average = calculate_average(marks_list)
    grade = get_grade(average)
    result = classify_result(average)
    return {
        "name": name,
        "registration_number": registration_number,
        "age":age,
        "marks_list": marks_list,
        "average": average,
        "grade": grade,
        "classify_result": result
    }
    