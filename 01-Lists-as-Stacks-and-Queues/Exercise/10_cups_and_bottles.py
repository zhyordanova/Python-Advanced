from collections import deque

cups = deque([int(el) for el in input().split()])
bottles = [int(el) for el in input().split()]
waste = 0

while cups and bottles:
    cup_value = cups.popleft()
    water = bottles.pop()

    if water > cup_value:
        waste += water - cup_value
    else:
        while water - cup_value < 0:
            water += bottles.pop()
        waste += water - cup_value

if bottles:
    print(f"Bottles: {' '.join([str(el) for el in bottles])}")
elif cups:
    print(f"Cups: {' '.join(str(el) for el in cups)}")
print(f"Wasted litters of water: {waste}")


