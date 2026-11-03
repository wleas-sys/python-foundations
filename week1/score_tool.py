students = [
    {"name": "zs", "score": 92},
    {"name": "ls", "score": 58},
    {"name": "ww", "score": 76},
]


def calculate_average(students):
    if not students:
        raise ValueError("students cannot be empty")

    total = 0

    for student in students:
        total = total + student["score"]

    return total / len(students)


def find_highest_student(students):
    if not students:
        raise ValueError("students cannot be empty")

    highest = students[0]

    for student in students:
        if student["score"] > highest["score"]:
            highest = student

    return highest


def calculate_pass_rate(students, passing_score=60):
    if not students:
        raise ValueError("students cannot be empty")

    passed_count = 0

    for student in students:
        if student["score"] >= passing_score:
            passed_count += 1

    return passed_count / len(students) * 100


def build_report(students):
    return {
        "average": calculate_average(students),
        "highest": find_highest_student(students),
        "pass_rate": calculate_pass_rate(students),
    }


print(students)
print(calculate_average(students))
print(find_highest_student(students))
print(calculate_pass_rate(students))
print(build_report(students))
