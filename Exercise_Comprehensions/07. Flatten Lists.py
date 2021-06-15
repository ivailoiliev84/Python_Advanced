data = input().split("|")

result = []
numbers = [[int(x) for x in el.split()]for el in data]

numbers.reverse()

numbers = [number for seq in numbers for number in seq]



print(' '.join(str(n) for n in numbers))

