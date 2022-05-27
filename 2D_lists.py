
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# we can also change values on there lists like:
matrix[0][1] = 20
# now the number 2 will change to 20
print(matrix[0][1])
# also we can use nested loops
for row in matrix:
    for item in row:
        print(item)
