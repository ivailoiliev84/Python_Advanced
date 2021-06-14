def even_nums(num):
    if num % 2 ==0:
        return True
    else:
        return False


nums = [int(n) for n in input().split()]

result = list(filter(even_nums, nums))
print(result)





