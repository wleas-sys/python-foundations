numbers = [2, 4, 6, 8]
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
