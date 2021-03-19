from collections import deque

price_of_bullet = int(input())
size_gun_barrel = int(input())
bullets = [int(el) for el in input().split()]
locks = deque([int(el) for el in input().split()])
value_intelligence = int(input())

count_shoots = 0
shot = 0

while bullets and locks:
    bullet = bullets.pop()
    current_lock = locks.popleft()
    if bullet <= current_lock:
        print("Bang!")
    else:
        print("Ping!")
        locks.appendleft(current_lock)
    count_shoots += 1
    shot += 1

    if size_gun_barrel - shot == 0 and len(bullets) > 0:
        print('Reloading!')
        shot = 0

if len(locks) > 0:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    bullet_cost = count_shoots * price_of_bullet
    earned = value_intelligence - bullet_cost
    print(f"{len(bullets)} bullets left. Earned ${earned}")








