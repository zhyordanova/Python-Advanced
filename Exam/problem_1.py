from collections import deque


def is_firework_pouch_full(firework_created):
    return all([count >= 3 for count in firework_created.values()])


def print_result(firework_effects, explosive_power, firework_created):
    if firework_effects:
        print(f"Firework Effects left: {', '.join(map(str, firework_effects))}")
    if explosive_power:
        print(f"Explosive Power left: {', '.join(map(str, explosive_power))}")
    for firework, count in firework_created.items():
        print(f"{firework}: {count}")


firework_effects = deque([int(el) for el in input().split(', ')])
explosive_power = [int(el) for el in input().split(', ')]
firework_created = {'Palm Fireworks': 0, 'Willow Fireworks': 0, 'Crossette Fireworks': 0}


while firework_effects and explosive_power:

    current_firework = firework_effects.popleft()
    current_explosive = explosive_power.pop()
    firework_value = current_firework + current_explosive

    if current_firework <= 0:
        explosive_power.append(current_explosive)
    elif current_explosive <= 0:
        firework_effects.appendleft(current_firework)
    elif firework_value % 3 == 0 and not firework_value % 5 == 0:
        firework_created['Palm Fireworks'] += 1
    elif firework_value % 5 == 0 and not firework_value % 3 == 0:
        firework_created['Willow Fireworks'] += 1
    elif firework_value % 3 == 0 and firework_value % 5 == 0:
        firework_created['Crossette Fireworks'] += 1
    else:
        current_firework -= 1
        firework_effects.append(current_firework)
        explosive_power.append(current_explosive)

    if is_firework_pouch_full(firework_created):
        print('Congrats! You made the perfect firework show!')
        break

else:
    print('Sorry. You can’t make the perfect firework show.')

print_result(firework_effects, explosive_power, firework_created)
