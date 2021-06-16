rows, columns = [int(n) for n in input().split()]

matrix = []

for _ in range(rows):
    matrix.append([int(n) for n in input().split()])
current_sum = 0
result = 0
position = tuple()
if rows >= 3 and columns >= 3:

    for i in range(0, rows - 2):

        for j in range(0, columns - 2):
            current_sum = matrix[i][j] + matrix[i][j + 1] + matrix[i][j + 2] \
                          + matrix[i + 1][j] + matrix[i + 1][j + 1] + matrix[i + 1][j + 2] \
                          + matrix[i + 2][j] + matrix[i + 2][j + 1] + matrix[i + 2][j + 2]
            if current_sum >= result:
                result = current_sum
                position = (i, j)
i, j = position
print(f"Sum = {result}")
print(matrix[i][j], matrix[i][j + 1], matrix[i][j + 2])
print(matrix[i+1][j], matrix[i+1][j+1], matrix[i+1][j+2])
print(matrix[i+2][j], matrix[i+2][j+1], matrix[i+2][j+2])