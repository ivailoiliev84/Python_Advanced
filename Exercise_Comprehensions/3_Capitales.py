n = input().split(", ")
c = input().split(", ")

sheet = zip(n, c)

[print(f'{key} -> {value}') for key, value in sheet]
