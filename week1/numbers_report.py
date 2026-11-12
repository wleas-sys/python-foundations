def find_min(numbers):
    min_num = numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num
    return  min_num
print(find_min([12, 7, 25, 3, 18]))
print(find_min([3, 99, 7]))
def find_max(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return  max_num
print(find_max([12, 7, 25, 3, 18]))
print(find_max([3, 99, 7]))

def find_total(numbers):
    # 第 1 步：准备一个变量装总和，初始是 0
    total = 0
    for num in numbers:
       total += num
    return total
print(find_total([12, 7, 25, 3, 18]))
print(find_total([3, 99, 7]))
def find_average(numbers):
    total = find_total(numbers)
    return round(total / len(numbers), 1)
print(find_average([12, 7, 25, 3, 18]))
print(find_average([3, 99, 7]))
