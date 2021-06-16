rows, columns = [int(n) for n in input().split()]

matrix = []

for _ in range(rows):
    matrix.append(input().split())

command = input()
while not command == "END":
    data = command.split()
    current_command = data[0]
    if current_command.startswith('swap'):
        indexes = data[1], data[2], data[3], data[4]
        row1 = int(indexes[0])
        col1 = int(indexes[1])
        row2 = int(indexes[2])
        col2 = int(indexes[3])
        if current_command == 'swap' and len(indexes) == 4:
            try:
                a = matrix[row1][col1]
                b = matrix[row2][col2]
                matrix[row1][col1] = b
                matrix[row2][col2] = a
                for i in matrix:
                    print(*i)

            except IndexError:
                print("Invalid input!")

        else:
            print("Invalid input!")
    else:
        print("Invalid input!")
    command = input()
