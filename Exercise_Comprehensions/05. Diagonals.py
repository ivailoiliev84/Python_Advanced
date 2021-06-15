n = int(input())

matrix = [[int(j) for j in input().split(", ")] for i in range(n)]
first = [matrix[j][row] for j in range(n) for row in range(n) if row == j]
second = [matrix[j][row] for j in range(n) for row in range(n) if n - row - 1 == j]


print(f"First diagonal: {', '.join([str(w) for w in first])}. Sum: {sum(first)}")
print(f"Second diagonal: {', '.join([str(w) for w in second])}. Sum: {sum(second)}")

