import pytest # 用到 pytest.approx 和 pytest.raises，必须导入

import score_tool # 导入被测模块，和原文件一样
from pathlib import Path

def test_average(): # 顶格函数：pytest 只收顶层名字
    students = [
        {"name": "zs", "score": 92},
        {"name": "ls", "score": 58},
        {"name": "ww", "score": 76},
    ]

    # unittest 的 assertAlmostEqual(x, 75.333333, places=2)
    # → pytest 写成 assert x == pytest.approx(75.333333, abs=0.01)
    # 原理：平均值是无限小数，浮点无法精确相等，approx 允许误差内相等
    assert score_tool.calculate_average(students) == pytest.approx(
        75.333333,
        abs=0.01,
    )


def test_rejects_non_numeric_score(): # 顶格函数，与上一个同级，不要缩进
    # unittest: with self.assertRaisesRegex(ValueError, "score must be a number"):
    # pytest  : with pytest.raises(ValueError, match="score must be a number"):
    # 原理：raises 第一个参数是"期望的异常类型"；
    #       match 用 re.search 语义匹配异常消息（包含关系，非完全相等）
    with pytest.raises(ValueError, match="score must be a number"):
        score_tool.get_student_score({"name": "bad", "score": "92"})
def test_rejects_empty_students():
    # 被测行为：calculate_average 收到空列表必须拒绝，不能返回 0 或崩溃成 ZeroDivisionError
    # 原 unittest 写法：with self.assertRaisesRegex(ValueError, "students cannot be empty"):
    # pytest 写法：pytest.raises(类型, match=正则)
    # match 用 re.search 语义 —— 异常消息里"包含"这段文本即可，不要求完全相等
    with pytest.raises(ValueError, match="students cannot be empty"):
        score_tool.calculate_average([])
def test_load_students(tmp_path):
    fake = tmp_path / "scores.json"
    fake.write_text('[{"name":"a","score":1},{"name":"b","score":2}]', encoding="utf-8")
    students = score_tool.load_students(fake)
    # 被测行为：load_students 不传参时读默认文件，返回 3 条记录
    # ⚠️ 这个测试依赖真实的 week1/scores.json —— 文件一变，测试就挂（下一步用 tmp_path 解决）
    # unittest: self.assertEqual(len(students), 3)
    # pytest  : assert 实际值 == 期望值
    # 原理：assert 是语句不是函数，所以不需要括号；表达式为假时抛 AssertionError
    assert len(students) == 2
    assert students[0]["name"] == "a"
    # unittest: self.assertEqual(students[0], {"name": "zs", "score": 92})
    # 原理：字典的 == 比较内容，与键的书写顺序无关
    assert students[0] == {"name": "a", "score": 1}
def test_highest_student():
    students = [
        {"name": "zs", "score": 92},
        {"name": "ls", "score": 58},
        {"name": "ww", "score": 76},
    ]
    assert score_tool.find_highest_student(students)== {"name": "zs", "score": 92}
def test_pass_rate():
    students = [
        {"name": "zs", "score": 92},
        {"name": "ls", "score": 58},
        {"name": "ww", "score": 76},
    ]
    assert score_tool.calculate_pass_rate(students) == pytest.approx(
        66.666666,
        abs=0.01,
    )

@pytest.mark.parametrize("score", [-5,150])# ① 参数名字符串
def test_rejects_out_of_range_score(score):
        with pytest.raises(ValueError, match="score must be between 0 and 100"):
            score_tool.get_student_score({"name": "bad", "score": score})
def test_rejects_student_without_score():
        with pytest.raises(ValueError, match="student must contain score"):
            score_tool.calculate_average([{"name": "bad"}])
def test_rejects_missing_scores_file():
        with pytest.raises(FileNotFoundError, match="scores file not found"):
            score_tool.load_students(Path("missing.json"))
def test_rejects_invalid_json(tmp_path):
    bad = tmp_path / "1.json"                    # ① 文件名随便起
    bad.write_text("invalid json", encoding="utf-8")        # ② 写一段坏 JSON
    with pytest.raises(ValueError, match="invalid JSON"):   # ③ 期望消息
         score_tool.load_students(bad)


