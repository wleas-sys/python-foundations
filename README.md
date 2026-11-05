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

`week1/score_tool.py` 使用一组内存中的学生成绩计算：

- 平均分
- 最高分学生
- 及格率

程序会校验分数类型、分数范围、必需字段和空学生列表，并把结果格式化为易读报告。

### 运行

在 `python-foundations` 目录执行：

```powershell
.\.venv\Scripts\python.exe .\week1\score_tool.py
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

当前包含 7 个测试，覆盖正常统计和异常输入。

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
    ├── scope_test.py
    ├── score_tool.py
    ├── test_import.py
    └── test_score_tool.py
```

## 当前限制

- 学生数据暂时写在 `main()` 中。
- 尚未实现 JSON 文件读取。
- 尚未实现命令行参数。

