def even_odd(*args):
    if args[-1] == "even":
        return [args[n] for n in range(len(args) - 1) if int(args[n]) % 2 == 0]
    elif args[-1] == "odd":
        return [args[n] for n in range(len(args) - 1) if int(args[n] % 2 != 0)]


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))