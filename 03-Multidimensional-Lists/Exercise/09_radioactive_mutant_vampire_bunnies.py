def player_dies(player_position, row, col, lair):
    lair[player_position[0]][player_position[1]] = "."
    spread_bunnies(rows_count, cols_count, lair, player_position)
    lair[player_position[0]][player_position[1]] = "B"
    [print(''.join(row)) for row in lair]
    print(f"dead: {row} {col}")
    exit()


def player_wins(player_position, lair):
    lair[player_position[0]][player_position[1]] = "."
    spread_bunnies(rows_count, cols_count, lair, player_position)
    [print(''.join(row)) for row in lair]
    print(f"won: {player_position[0]} {player_position[1]}")
    exit()


def is_valid(row, col, rows_count, cols_count):
    return 0 <= row < rows_count and 0 <= col < cols_count


def spread_bunnies(rows_count, cols_count, lair, player_position):
    bunny_rows = []
    bunny_cols = []
    has_died = False

    for row in range(rows_count):
        for col in range(cols_count):
            if lair[row][col] == "B":
                bunny_rows.append(row)
                bunny_cols.append(col)

    for i in range(len(bunny_rows)):
        possible_spreads = [
            [bunny_rows[i] - 1, bunny_cols[i]],
            [bunny_rows[i] + 1, bunny_cols[i]],
            [bunny_rows[i], bunny_cols[i] - 1],
            [bunny_rows[i], bunny_cols[i] + 1],
                          ]

        for spread in possible_spreads:
            if is_valid(spread[0], spread[1], rows_count, cols_count):
                if lair[spread[0]][spread[1]] == "P":
                    has_died = True
                else:
                    lair[spread[0]][spread[1]] = "B"

    if has_died:
        lair[player_position[0]][player_position[1]] = "B"
        [print(''.join(row)) for row in lair]
        print(f"dead: {player_position[0]} {player_position[1]}")
        exit()


def check_player_move(row, col, lair, player_position, rows_count, cols_count):
    if not is_valid(row, col, rows_count, cols_count):
        player_wins(player_position, lair)
    elif lair[row][col] == "B":
        player_dies(player_position, row, col, lair)
    else:
        lair[row][col] = "P"
        lair[player_position[0]][player_position[1]] = "."
        return [row, col]


rows_count, cols_count = list(map(int, input().split()))
lair = [list(input()) for _ in range(rows_count)]
commands = list(input())

player_position = [0, 0]

for row in range(rows_count):
    for col in range(cols_count):
        if lair[row][col] == "P":
            player_position = [row, col]
            break


for command in commands:
    curr_player_row = player_position[0]
    curr_player_col = player_position[1]

    if command == "U":
        curr_player_row -= 1

    elif command == "D":
        curr_player_row += 1

    elif command == "L":
        curr_player_col -= 1

    elif command == "R":
        curr_player_col += 1

    player_position = check_player_move(curr_player_row, curr_player_col, lair, player_position, rows_count, cols_count)
    spread_bunnies(rows_count, cols_count, lair, player_position)
