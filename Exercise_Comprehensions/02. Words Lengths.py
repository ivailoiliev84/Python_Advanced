data = input().split(', ')

print(', '.join([f'{name} -> {len(name)}' for name in data]))
