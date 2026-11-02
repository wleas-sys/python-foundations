numbers = [2, 4, 6, 8]
total = 0
for number in numbers:
    total = total + number

print(total)

average = total / len(numbers)
print(average)
maximum = numbers[0]

for number in numbers:
    if number > maximum:
        maximum = number

print(maximum)
greater_than_five = []

for number in numbers:
    if number > 5:
        greater_than_five.append(number)

print(greater_than_five)
result = {
    "total": total,
    "average": average,
    "maximum": maximum,
    "greater_than_five": greater_than_five,
}

print(result)
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count = count + 1
    # 遍历 text，判断每个字符是否在 vowels 中
    # 如果属于元音，让 count 加 1

    return count
print(count_vowels("hello"))
print(count_vowels("AEIOU"))
print(count_vowels(""))
def average(numbers):
    if not numbers:
        raise ValueError("numbers cannot be empty")

    total = 0
    for number in numbers:
        total = total + number

    return total / len(numbers)


print(average([2, 4, 6, 8]))
print(average([10]))

try:
    average([])
except ValueError as error:
    print(type(error).__name__, error)


def reverse_text(text):
    result = ""
    for char in text:
        result = char + result
    return result


print(reverse_text("hello"))
print(reverse_text(""))


def is_palindrome(text):
    normalized = text.lower()
    return normalized == reverse_text(normalized)


print(is_palindrome("level"))
print(is_palindrome("Hello"))
print(is_palindrome(""))