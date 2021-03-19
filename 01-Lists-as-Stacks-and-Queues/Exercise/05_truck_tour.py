from collections import deque

n = int(input())
pumps = deque()

for _ in range(n):
    pumps.append(input())

for big_circle_iteration in range(n):
    is_valid = True
    tank_petrol = 0
    for small_circle_iteration in range(n):
        current_station = pumps[small_circle_iteration]

        petrol, distance_to_next_station = current_station.split()
        petrol = int(petrol)
        distance_to_next_station = int(distance_to_next_station)
        tank_petrol += petrol - distance_to_next_station

        if tank_petrol < 0:
            is_valid = False
            pumps.append(pumps.popleft())
            break

    if is_valid:
        print(big_circle_iteration)
        break
