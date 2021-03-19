from collections import deque

players = input().split()
step = int(input())

que = deque(players)

while len(que) > 1:
    for _ in range(step - 1):
        que.append(que.popleft())
    print(f"Removed {que.popleft()}")

print(f"Last is {que.popleft()}")