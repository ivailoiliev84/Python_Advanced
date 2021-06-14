def calculate(num):
    print(f"The minimum number is {min(num)}")
    print(f"The maximum number is {max(num)}")
    print(f"The sum number is: {sum(num)}")


nums = [int(n) for n in input().split()]

calculate(nums)