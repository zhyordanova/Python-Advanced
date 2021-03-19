from collections import deque

START_COMMAND = "Start"
END_COMMAND = "End"
REFILL_COMMAND = "refill"

total_amount = int(input())

people_queue = deque()

while True:
    command = input()
    if command == START_COMMAND:
        break
    people_queue.append(command)

while True:
    command = input()
    if command == END_COMMAND:
        print(f"{total_amount} liters left")
        break
    if command.startswith(REFILL_COMMAND):
        command_params = command.split()
        refill_litters = int(command_params[1])
        total_amount += refill_litters
    else:
        person = people_queue.popleft()
        person_litters = int(command)
        if person_litters <= total_amount:
            print(f"{person} got water")
            total_amount -= person_litters
        else:
            print(f"{person} must wait")