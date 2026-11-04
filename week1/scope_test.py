
# 作用域实验：为什么函数里改不了外层的变量
#
# 下面这段取消注释就会报错：
#
#   count = 0
#
#   def add_one_broken():
#       count = count + 1
#       print(count)
#
#   add_one_broken()
#
# 报错：UnboundLocalError: cannot access local variable 'count'
#       where it is not associated with a value
#
# 原因：函数里只要给某个名字赋过值，Python 在整个函数范围内都把它当局部变量。
#      所以 count + 1 右边的 count 也是局部的，而那一刻它还没被赋值。
#
# 正确做法：数据靠参数进、靠 return 出，不要用 global。


def add_one(value):
    return value + 1


count = 0
count = add_one(count)
print(count)
