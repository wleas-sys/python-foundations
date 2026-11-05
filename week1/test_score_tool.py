import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

import score_tool


class TestScoreTool(unittest.TestCase):
    def test_average(self):
        students = [
            {"name": "zs", "score": 92},
            {"name": "ls", "score": 58},
            {"name": "ww", "score": 76},
        ]

        self.assertAlmostEqual(
            score_tool.calculate_average(students),
            75.333333,
            places=2,
        )

    def test_load_students(self):
        students = score_tool.load_students()

        self.assertEqual(len(students), 3)
        self.assertEqual(
            students[0],
            {"name": "zs", "score": 92},
        )

    def test_highest_student(self):
        students = [
            {"name": "zs", "score": 92},
            {"name": "ls", "score": 58},
            {"name": "ww", "score": 76},
        ]

        self.assertEqual(
            score_tool.find_highest_student(students),
            {"name": "zs", "score": 92},
        )

    def test_pass_rate(self):
        students = [
            {"name": "zs", "score": 92},
            {"name": "ls", "score": 58},
            {"name": "ww", "score": 76},
        ]

        self.assertAlmostEqual(
            score_tool.calculate_pass_rate(students),
            66.666666,
            places=2,
        )

    def test_rejects_non_numeric_score(self):
        with self.assertRaisesRegex(ValueError, "score must be a number"):
            score_tool.get_student_score({"name": "bad", "score": "92"})

    def test_rejects_out_of_range_score(self):
        for score in (-5, 150):
            with self.subTest(score=score):
                with self.assertRaisesRegex(
                    ValueError,
                    "score must be between 0 and 100",
                ):
                    score_tool.get_student_score(
                        {"name": "bad", "score": score}
                    )

    def test_rejects_student_without_score(self):
        with self.assertRaisesRegex(
            ValueError,
            "student must contain score",
        ):
            score_tool.calculate_average([{"name": "bad"}])

    def test_rejects_empty_students(self):
        with self.assertRaisesRegex(
            ValueError,
            "students cannot be empty",
        ):
            score_tool.calculate_average([])

    def test_rejects_missing_scores_file(self):
        with self.assertRaisesRegex(
            FileNotFoundError,
            "scores file not found",
        ):
            score_tool.load_students(Path("missing.json"))

    def test_rejects_invalid_json(self):
        with TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "invalid.json"
            path.write_text("{invalid json", encoding="utf-8")

            with self.assertRaisesRegex(
                ValueError,
                "invalid JSON",
            ):
                score_tool.load_students(path)

    def test_rejects_non_list_json(self):
        with TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "student.json"
            path.write_text(
                '{"name": "zs", "score": 92}',
                encoding="utf-8",
            )

            with self.assertRaisesRegex(
                ValueError,
                "top-level JSON value must be a list",
            ):
                score_tool.load_students(path)

    def test_parse_args_uses_default_path(self):
        args = score_tool.parse_args([])

        self.assertEqual(args.path, score_tool.DATA_FILE)

    def test_parse_args_accepts_custom_path(self):
        args = score_tool.parse_args(["custom.json"])

        self.assertEqual(args.path, Path("custom.json"))


if __name__ == "__main__":
    unittest.main()
