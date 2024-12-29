PLAYER_SYMBOL = 'P'
EMPTY_SYMBOL = '-'

initial_string = input()


def read_matrix():
    size = int(input())
    matrix = []
    for i in range(size):
        matrix.append(list(input()))

    return matrix


def find_player_position(matrix):
    for row_index in range(len(matrix)):
        if PLAYER_SYMBOL in matrix[row_index]:
            column_index = matrix[row_index].index(PLAYER_SYMBOL)
            return row_index, column_index


def is_valid(row, col, matrix):
    return 0 <= row < len(matrix) and 0 <= col < len(matrix)


matrix = read_matrix()
player_position = find_player_position(matrix)
row = player_position[0]
col = player_position[1]

command_counts = int(input())

for _ in range(command_counts):
    matrix[row][col] = EMPTY_SYMBOL
    command = input()
    previous_row = row
    previous_col = col

    if command == 'up':
        row -= 1
    elif command == 'down':
        row += 1
    elif command == 'left':
        col -= 1
    elif command == 'right':
        col += 1

    if not is_valid(row, col, matrix):
        if len(initial_string) > 0:
            initial_string = initial_string[:-1]
            row = previous_row
            col = previous_col
    else:
        if matrix[row][col].isalpha():
            initial_string += matrix[row][col]

    matrix[row][col] = PLAYER_SYMBOL

print(initial_string)
print(*[''.join(x) for x in matrix], sep="\n")
