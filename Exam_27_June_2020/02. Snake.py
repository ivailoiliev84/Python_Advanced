n = int(input())

matrix = []
for i in range(n):
    matrix.append([x for x in input()])
snake_position = tuple()
holes_position = []
for i in range(n):
    for j in range(n):
        if matrix[i][j] == "S":
            snake_position = i, j
        if matrix[i][j] == "B":
            holes_position.append((i, j))
out_of_range = False
collect_food = False
food_counter = 0

while not collect_food:
    row, col = snake_position
    command = input()

    try:
        if command == "up":
            row -= 1
            if not 0 <= row <= n - 1:
                matrix[row + 1][col] = "."
                out_of_range = True
                break
            snake_position = row, col
            matrix[row + 1][col] = "."
            if matrix[row][col] == "*":
                food_counter += 1
            if matrix[row][col] == "B":
                matrix[row][col] = "."
                for el in holes_position:
                    if snake_position != el:
                        snake_position = el
                        row, col = snake_position
            matrix[row][col] = "S"
            if food_counter == 10:
                collect_food = True
                break

        elif command == "down":
            row += 1
            if not 0 <= row <= n - 1:
                matrix[row - 1][col] = "."
                out_of_range = True
                break
            snake_position = row, col
            matrix[row - 1][col] = "."
            if matrix[row][col] == "*":
                food_counter += 1

            if matrix[row][col] == "B":
                matrix[row][col] = "."
                for el in holes_position:
                    if snake_position != el:
                        snake_position = el
                        row, col = snake_position

            matrix[row][col] = "S"

            if food_counter == 10:
                collect_food = True
                break

        elif command == "left":
            col -= 1
            if not 0 <= col <= n - 1:
                matrix[row][col + 1] = "."
                out_of_range = True
                break
            snake_position = row, col
            matrix[row][col + 1] = "."
            if matrix[row][col] == "*":
                food_counter += 1
            if matrix[row][col] == "B":
                matrix[row][col] = "."
                for el in holes_position:
                    if snake_position != el:
                        snake_position = el
                        row, col = snake_position
            matrix[row][col] = "S"
            if food_counter == 10:
                collect_food = True
                break

        elif command == "right":
            col += 1
            if not 0 <= col <= n - 1:
                matrix[row][col - 1] = "."
                out_of_range = True
                break
            snake_position = row, col
            matrix[row][col - 1] = "."
            if matrix[row][col] == "*":
                food_counter += 1
            if matrix[row][col] == "B":
                matrix[row][col] = "."
                for el in holes_position:
                    if snake_position != el:
                        snake_position = el
                        row, col = snake_position
            matrix[row][col] = "S"
            if food_counter == 10:
                collect_food = True
                break
    except IndexError:
        out_of_range = True
        break
if out_of_range:
    print("Game over!")
else:
    print("You won! You fed the snake.")
print(f"Food eaten: {food_counter}")
for el in matrix:
    print(''.join(str(x) for x in el))
