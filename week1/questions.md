# Questions

## 2026-11-04

### 非数字分数

- 问题：`score` 是字符串 `"92"` 时，不能参与数学计算。
- 相关位置：`get_student_score()` 调用 `validate_score()`。
- 报错：`ValueError: score must be a number`
- 已尝试：`isinstance(value, (int, float))` 检查类型。
- 测试：`test_rejects_non_numeric_score`
- 当前状态：已解决。

### 分数超出范围

- 问题：负数或超过 100 的分数不应参与统计。
- 相关代码：

```python
if value < 0 or value > 100:
    raise ValueError("score must be between 0 and 100")
```

- 报错：`ValueError: score must be between 0 and 100`
- 已尝试：分别测试 `-5` 和 `150`。
- 测试：`test_rejects_out_of_range_score`
- 当前状态：已解决。

### 学生记录缺少分数

- 问题：学生字典没有 `score` 键时，直接访问会产生不清楚的 `KeyError`。
- 相关位置：`get_student_score()`。
- 检查方式：

```python
if "score" not in student:
    raise ValueError("student must contain score")
```

- 报错：`ValueError: student must contain score`
- 已尝试：使用 `in` 在读取前检查键是否存在。
- 测试：`test_rejects_student_without_score`
- 当前状态：已解决。

### 空学生列表

- 问题：空列表没有平均值，直接计算会发生除零错误。
- 相关位置：三个统计函数入口。
- 报错：`ValueError: students cannot be empty`
- 已尝试：使用 `if not students` 提前拦截。
- 测试：`test_rejects_empty_students`
- 当前状态：已解决。
