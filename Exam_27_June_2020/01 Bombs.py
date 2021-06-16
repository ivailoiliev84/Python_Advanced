from collections import deque

bomb_effect = deque([int(x) for x in input().split(", ")])
bomb_casings = [int(x) for x in input().split(", ")]
bombs = {'Datura Bombs': 0, 'Cherry Bombs': 0, 'Smoke Decoy Bombs': 0}
is_collect = False
while bomb_effect or bomb_casings:
    try:
        if bombs['Datura Bombs'] >= 3 and bombs['Cherry Bombs'] >= 3 and bombs['Smoke Decoy Bombs'] >= 3:
            is_collect = True
            break
        if bomb_effect[0] + bomb_casings[-1] == 40:
            bombs['Datura Bombs'] += 1
            bomb_effect.popleft()
            bomb_casings.pop()

        elif bomb_effect[0] + bomb_casings[-1] == 60:
            bombs['Cherry Bombs'] += 1
            bomb_effect.popleft()
            bomb_casings.pop()
        elif bomb_effect[0] + bomb_casings[-1] == 120:
            bombs['Smoke Decoy Bombs'] += 1
            bomb_effect.popleft()
            bomb_casings.pop()
        else:
            bomb_casings[-1] = bomb_casings[-1] - 5
    except IndexError:
        break

if is_collect:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if not bomb_effect:
    print("Bomb Effects: empty")
else:
    print(f"Bomb Effects: {', '.join(str(x) for x in bomb_effect)}")

if not bomb_casings:
    print("Bomb Casings: empty")
else:
    print(f"Bomb Casings: {', '.join(str(x) for x in bomb_casings)}")

sorted_bombs = sorted(bombs.items(), key=lambda kvp: kvp)
for key, value in sorted_bombs:
    print(f"{key}: {value}")
