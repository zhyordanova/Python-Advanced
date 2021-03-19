matrix_size = int(input())
number_of_bombs = int(input())
field = [['0'] * matrix_size for _ in range(matrix_size)]

# up, down, left, right, upper lft diagonal, upper right diagonal, lower left diagonal, lower right diagonal
rows = [-1, 1, 0, 0, -1, -1, 1, 1]
cols = [0, 0, -1, 1, -1, 1, -1, 1]


def check_position(row, col, len_field):
    return 0 <= row < len_field and 0 <= col < len_field


def calculate_nearby_bombs(row, col, matrix):
    bomb_nearby = 0
    for i in range(8):
        new_row = row + rows[i]
        new_col = col + cols[i]
        if check_position(new_row, new_col, len(matrix)):
            if matrix[new_row][new_col] == '*':
                bomb_nearby += 1
    return bomb_nearby




for i in range(number_of_bombs):
    position = input().split(', ')
    row = int(position[0].strip('()'))
    col = int(position[1].strip('()'))
    field[row][col] = '*'

for row in range(matrix_size):
    for col in range(matrix_size):
        if not field[row][col] == '*':
            cell_value = calculate_nearby_bombs(row, col, field)
            field[row][col] = cell_value

for row in field:
    print(' '.join([str(el) for el in row]))
