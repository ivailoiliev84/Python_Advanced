data = [int(n) for n in input().split(", ")]
p = [str(n) for n in data if n >=0]
n = [str(n) for n in data if n < 0]
ev = [str(n) for n in data if n % 2 == 0]
od = [str(n) for n in data if n % 2 != 0]
print(f"Positive: {', '.join(p)}")
print(f"Negative: {', '.join(n)}")
print(f"Even: {', '.join(ev)}")
print(f"Odd: {', '.join(od)}")
