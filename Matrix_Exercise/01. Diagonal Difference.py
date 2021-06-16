n = int(input())

matrix = []

for i in range(n):
    matrix.append([int(n) for n in input().split()])
left_sum = 0
right_sum = 0
for i in range(n):

    for j in range(n):
        if i == j:
            left_sum += matrix[i][j]

        if i == n -j - 1:
            right_sum += matrix[i][j]

result = abs(left_sum - right_sum)
print(result)





