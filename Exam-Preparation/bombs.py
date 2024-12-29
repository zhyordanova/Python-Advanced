from collections import deque


def is_bombs_pouch_full(bombs_created):
    return all([count >= 3 for count in bombs_created.values()])


def print_effects_and_castings(bomb_effects, bomb_casings):
    print(f"Bomb Effects: {'empty' if not bomb_effects else ', '.join(map(str, bomb_effects))}")
    print(f"Bomb Casings: {'empty' if not  bomb_casings else ', '.join(map(str, bomb_casings))}")


def print_bombs_created(bombs_created):
    for bomb, count in sorted(bombs_created.items()):
        print(f"{bomb}: {count}")


bomb_effects = deque([int(el) for el in input().split(', ')])
bomb_casings = [int(el) for el in input().split(', ')]
BOMBS = {40: "Datura Bombs", 60: "Cherry Bombs", 120: "Smoke Decoy Bombs"}
bombs_created = {"Datura Bombs": 0, "Cherry Bombs": 0, "Smoke Decoy Bombs": 0}

while bomb_effects and bomb_casings:
    values_sum = bomb_effects[0] + bomb_casings[-1]

    if values_sum in BOMBS:
        bomb_created = BOMBS[values_su]
        bombs_created[bomb_created] += 1
        bomb_effects.popleft()
        bomb_casings.pop()
    else:
        bomb_casings[-1] -= 5

    if is_bombs_pouch_full(bombs_created):
        print("Bene! You have successfully filled the bomb pouch!")
        break

else:
    print("You don't have enough materials to fill the bomb pouch.")

print_effects_and_castings(bomb_effects, bomb_casings)
print_bombs_created(bombs_created)






