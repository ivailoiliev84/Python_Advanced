def create_matrix(r, c):
    matrix = []
    for i in range(r):
        matrix.append([])
        for j in range(c):
            matrix[-1].append("")

    return matrix


rows, columns = input().split(" ")
rows, columns = int(rows), int(columns)
matrix = create_matrix(rows, columns)

snake = [el for el in input()]
snake_index = 0

for i in range(rows):
    for j in range(columns):
        if i % 2 == 0:
            matrix[i][j] = snake[snake_index]
            if snake_index >= len(snake) - 1:
                snake_index = 0
            else:
                snake_index += 1
        else:

            matrix[i][columns - 1 - j] = snake[snake_index]
            if snake_index >= len(snake) - 1:
                snake_index = 0
            else:
                snake_index += 1
for i in matrix:
    print(''.join(x for x in i))
