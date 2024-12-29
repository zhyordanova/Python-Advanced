from math import floor

PLAYER_SYMBOL = 'P'
WALL_SYMBOL = 'X'


def player_position(field, symbol):
    for row_index in range(len(field)):
        if symbol in field[row_index]:
            column = field[row_index].index(symbol)
            return row_index, column


def get_new_position(current_position, command, PLAYER_MOVEMENTS):
    current_row, current_col = current_position[0], current_position[1]

    if command == "up":
        current_row += PLAYER_MOVEMENTS['up'][0]
        current_col += PLAYER_MOVEMENTS['up'][1]

    elif command == "down":
        current_row += PLAYER_MOVEMENTS['down'][0]
        current_col += PLAYER_MOVEMENTS['down'][1]

    elif command == 'right':
        current_row += PLAYER_MOVEMENTS['right'][0]
        current_col += PLAYER_MOVEMENTS['right'][1]

    elif command == 'left':
        current_row += PLAYER_MOVEMENTS['left'][0]
        current_col += PLAYER_MOVEMENTS['left'][1]

    return current_row, current_col


def is_valid(row, col, field):
    return 0 <= row < len(field) and 0 <= col < len(field)


def print_result(path):
    print("Your path:")
    [print(row) for row in path]


def read_field():
    size = int(input())
    field = []
    for i in range(size):
        field.append(input().split())
    return field


field = read_field()
player_position = player_position(field, PLAYER_SYMBOL)
player_path = []
coins = 0

PLAYER_MOVEMENTS = {
    'up': (-1, 0),
    'down': (1, 0),
    'right': (0, 1),
    'left': (0, -1),
}

while True:
    command = input()

    if command not in PLAYER_MOVEMENTS:
        continue

    next_row, next_col = get_new_position(player_position, command, PLAYER_MOVEMENTS)
    if not is_valid(next_row, next_col, field) or field[next_row][next_col] == WALL_SYMBOL:
        coins = floor(coins * 0.5)
        print(f"Game over! You've collected {coins} coins.")
        break

    coins += int(field[next_row][next_col])
    player_path.append([next_row, next_col])
    player_position = [next_row, next_col]

    if coins >= 100:
        print(f"You won! You've collected {coins} coins.")
        break

print_result(player_path)
