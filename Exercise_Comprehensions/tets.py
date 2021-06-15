heroes = input().split(", ")

data = input()
inventory = {hero: {} for hero in heroes}
while not data == "End":
    hero, item, cost = data.split("-")
    if item not in inventory[hero]:
        inventory[hero][item] = int(cost)

    data = input()

for hero in heroes:
    cost = sum(inventory[hero].values())
    item_count = len(inventory[hero])
    print(f"{hero} -> Items: {item_count}, Cost: {cost}")

