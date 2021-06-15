n = int(input())
matrix = []
for _ in range(n):
    matrix.append([int(n) for n in input().split()])
command = input()
while not command == "END":
    current_command, row, column, value = command.split()
    row = int(row)
    column = int(column)
    value = int(value)
    if current_command == "Add":
        if 0 <= row <= n - 1 and 0 <= column <= n - 1:
            matrix[row][column] += value
        else:
            print("Invalid coordinates")
    elif current_command == "Subtract":
        if 0 <= row <= n - 1 and 0 <= column <= n - 1:
            matrix[row][column] -= value
        else:
            print("Invalid coordinates")
    command = input()
for el in matrix:
    print(' '.join(str(n) for n in el))
