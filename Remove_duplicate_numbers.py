numbers = [1, 51, 15, 11, 1, 5, 6, 4, ]
unique = []
for number in numbers:
    if number not in unique:
        unique.append(numbers)
print(unique)
