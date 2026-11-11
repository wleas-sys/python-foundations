##   def classify_number(numbers):
## count={"positive": 0, "negative": 0, "zero": 0}
    ## for n in numbers:
        ##  if n > 0:
##count["positive"] += 1
            ##   elif n < 0:
    ## count["negative"] += 1
            ##  else:
            ##  count["zero"] += 1
    ##return count
##print(classify_number([2,-1,0,4,-3]))

numbers = [3, 1, 4]

numbers.append(2)
numbers.insert(0, 5)
numbers.remove(4)
last = numbers.pop()
numbers.sort()

print(numbers)
print(last)
print(len(numbers))
scores = {"math": 90, "english": 75}

print(scores.get("math"))
print(scores.get("physics", 0))

scores["python"] = 88

for subject, score in scores.items():
    print(subject, score)

scores.update({"english": 80, "history": 70})
removed = scores.pop("math")

print(scores)
print(removed)
def count_even(numbers):
    count = 0
    for number in numbers:
        if number % 2 == 0:
            count = count + 1
    return count

print(count_even([1, 2, 4, 7, 8]))
