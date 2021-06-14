def chek_od_or_even(command, num, odd=0, even=0):
    if command == "Odd":
        for el in num:
            if el % 2 != 0:
                odd += el
        print(odd * len(nums))
    elif command == "Even":
        for el in num:
            if el % 2 == 0:
                even += el
        print(even * len(nums))


data = input()
nums = [int(n) for n in input().split()]

chek_od_or_even(data, nums)