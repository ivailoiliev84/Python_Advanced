categories = input().split(", ")
n = int(input())

sheet = {category: [] for category in categories}
for el in range(n):
    category, item, other = input().split(" - ")
    quantities, qualities = other.split(";")
    quantity, quality = int(quantities.split(":")[1]), int(qualities.split(":")[1])

    # print(category, item, quantity, quality)
    sheet[category].append({
        "item": item,
        "quantity": quantity,
        "quality": quality
    })
count_of_items = sum([it['quantity'] for n in sheet.values() for it in n])
average_quality = sum([item['quality'] for items in sheet.values() for item in items])
total_quality = average_quality / len(categories)
print(f'Count of items: {count_of_items}')
print(f'Average quality: {total_quality:.2f}')

for name in categories:
    print(f"{name} -> {', '.join(x['item'] for x in sheet[name])}")
