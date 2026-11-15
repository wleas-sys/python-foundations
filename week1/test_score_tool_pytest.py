import pytest # 用到 pytest.approx 和 pytest.raises，必须导入

import score_tool      # 导入被测模块，和原文件一样


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
