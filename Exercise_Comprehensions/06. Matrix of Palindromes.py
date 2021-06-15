rows, columns = [int(n) for n in input().split()]

matrix = [[f'{chr(97 + i)}{chr(97 + i + j)}{chr(97 + i)}' for j in range(columns)] for i in range(rows)]
[print(' '.join(i)) for i in matrix]