import argparse
import json
from pathlib import Path


DATA_FILE = Path(__file__).with_name("scores.json")


def parse_args(args=None):
    parser = argparse.ArgumentParser(
        description="Calculate a report from a student scores JSON file."
    )
    parser.add_argument(
        "path",
        nargs="?",
        type=Path,
        default=DATA_FILE,
        help="path to the scores JSON file",
    )
    return parser.parse_args(args)


def load_students(path=DATA_FILE):
    try:
        with path.open("r", encoding="utf-8") as file:
            students = json.load(file)
    except FileNotFoundError as error:
        raise FileNotFoundError(f"scores file not found: {path}") from error
    except json.JSONDecodeError as error:
        raise ValueError(f"invalid JSON in {path}") from error

    if not isinstance(students, list):
        raise ValueError("top-level JSON value must be a list")

    return students


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
def format_report(report):
    highest = report["highest"]

    return (
        f"平均分：{report['average']:.2f}\n"
        f"最高分：{highest['name']}（{highest['score']}）\n"
        f"及格率：{report['pass_rate']:.2f}%"
    )

def main():
    args = parse_args()
    students = load_students(args.path)
    report = build_report(students)
    print(format_report(report))

if __name__ == "__main__":
    main()
