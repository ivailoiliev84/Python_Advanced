def list_manipulator(massive, add_remove, beginning_end, *args_numbers):
    result = []

    if add_remove == "add" and beginning_end == "beginning":
        a = list(args_numbers)
        a.extend(massive)
        result = a

        return result

    if add_remove == "add" and beginning_end == "end":
        a = list(args_numbers)
        massive.extend(a)
        result = massive
        return result

    if add_remove == "remove" and beginning_end == "beginning":
        a = 0
        if args_numbers:
            for el in args_numbers:
                a = int(el)
            result = massive[a::]

            return result
        else:
            result = massive[1::]
            return result

    if add_remove == "remove" and beginning_end == "end":
        a = 0
        if args_numbers:
            for el in args_numbers:
                a = int(el)
            result = massive[:-a]
            return result
        else:
            result = massive[:-1]
            return result


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
