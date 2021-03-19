def check_remaining_coals(field_size):
    remaining_coals_count = 0
    for row in range(field_size):
        for col in range(field_size):
            if field[row][col] == "c":
                remaining_coals_count += 1

    return remaining_coals_count


def is_valid(move, field_size):
    return 0 <= move < field_size


def move_miner(field, position):
    row = position[0]
    col = position[1]
    coals_count = 0

    if field[row][col] == "e":
        print(f"Game over! ({row}, {col})")
        exit()
    elif field[row][col] == "c":
        field[row][col] = "*"
        coals_count += 1
        if not check_remaining_coals(field_size):
            print(f"You collected all coals! ({row}, {col})")
            exit()

    return coals_count


field_size = int(input())
commands = input().split()
field = [input().split() for _ in range(field_size)]

curr_position = [0, 0]
total_coals_count = 0

for row in range(field_size):
    for col in range(field_size):
        if field[row][col] == "s":
            curr_position = [row, col]
            break


for command in commands:
    row = curr_position[0]
    col = curr_position[1]

    if command == "left":
        move = col - 1
        if is_valid(move, field_size):
            curr_position = [row, move]

    elif command == "right":
        move = col + 1
        if is_valid(move, field_size):
            curr_position = [row, move]

    elif command == "up":
        move = row - 1
        if is_valid(move, field_size):
            curr_position = [move, col]

    elif command == "down":
        move = row + 1
        if is_valid(move, field_size):
            curr_position = [move, col]

    total_coals_count += move_miner(field, curr_position)


print(f"{check_remaining_coals(field_size)} coals left. ({curr_position[0]}, {curr_position[1]})")
