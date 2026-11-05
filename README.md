# Python Foundations

记录我的 Python、数学和 AI 基础学习过程。

## 开发环境

- Windows
- Python 3.12.10 (64-bit)
- PyCharm
- Git / GitHub Desktop

## Week 1 目标

- 复习 Python 基础类型和容器
- 学习函数、异常和文件处理
- 完成成绩统计命令行工具
- 完成高数和线性代数基础诊断
- 连续七天记录学习日报

## 当前项目：成绩统计工具

`week1/score_tool.py` 从 `week1/scores.json` 读取学生成绩并计算：

- 平均分
- 最高分学生
- 及格率

程序会检查 JSON 文件是否存在、格式是否正确，并校验分数类型、分数范围、必需字段和空学生列表，最后把结果格式化为易读报告。

### 运行

在 `python-foundations` 目录执行：

```powershell
.\.venv\Scripts\python.exe .\week1\score_tool.py
```

也可以指定其他成绩文件：

```powershell
.\.venv\Scripts\python.exe .\week1\score_tool.py .\week1\scores.json
```

预期输出：

```text
平均分：75.33
最高分：zs（92）
及格率：66.67%
```

### 测试

```powershell
.\.venv\Scripts\python.exe .\week1\test_score_tool.py
```

当前包含 13 个测试，覆盖正常统计、JSON 读取、文件缺失、JSON 格式错误、异常分数和命令行参数。

## 目录结构

```text
python-foundations/
├── README.md
├── .gitignore
└── week1/
    ├── day1_basics.py
    ├── day2_loops.py
    ├── hello_pycharm.py
    ├── math_notes.md
    ├── questions.md
    ├── scores.json
    ├── scope_test.py
    ├── score_tool.py
    ├── test_import.py
    └── test_score_tool.py
```


