def validate_score(value):
    if not isinstance(value, (int, float)):
        raise ValueError("score must be a number")

    if value < 0 or value > 100:
        raise ValueError("score must be between 0 and 100")

    return value


def get_student_score(student):
    if "score" not in student:
        raise ValueError("student must contain score")

    return validate_score(student["score"])


def calculate_average(students):
    if not students:
        raise ValueError("students cannot be empty")
    total = 0
    for student in students:
        score = get_student_score(student)
        total = total + score
    return total / len(students)


def find_highest_student(students):
    if not students:
        raise ValueError("students cannot be empty")
    highest = students[0]
    for student in students:
        score = get_student_score(student)

        if score > highest["score"]:
            highest = student
    return highest


def calculate_pass_rate(students, passing_score=60):
    if not students:
        raise ValueError("students cannot be empty")
    passing_score = validate_score(passing_score)
    passed_count = 0

    for student in students:
        score = get_student_score(student)

        if score >= passing_score:
            passed_count += 1
    return passed_count / len(students) * 100


def build_report(students):
    return {
        "average": calculate_average(students),
        "highest": find_highest_student(students),
        "pass_rate": calculate_pass_rate(students),
    }


def main():
    students = [
        {"name": "zs", "score": 92},
        {"name": "ls", "score": 58},
        {"name": "ww", "score": 76},
    ]
    print(students)
    print(calculate_average(students))
    print(find_highest_student(students))
    print(calculate_pass_rate(students))
    print(build_report(students))

if __name__ == "__main__":
    main()
