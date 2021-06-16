rows, columns = [int(n) for n in input().split()]

matrix = []

for _ in range(rows):
    matrix.append([sym for sym in input().split()])
first = ""
second = ""
count = 0
for i in range(0, rows - 1):
    for j in range(0, columns - 1):
        first = matrix[i][j], matrix[i][j + 1]
        second = matrix[i + 1][j], matrix[i + 1][j + 1]
        if matrix[i][j] == matrix[i][j + 1] and matrix[i][j] == matrix[i + 1][j] \
                and matrix[i][j] == matrix[i + 1][j + 1]:
            count += 1

print(count)
