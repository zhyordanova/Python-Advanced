def is_valid(row, col, size):
    return 0 <= row < size and 0 <= col < size


def explode(row, col, size, matrix):
    bomb = matrix[row][col]
    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + 2):
            if is_valid(r, c, size) and matrix[r][c] > 0:
                matrix[r][c] -= bomb


n = int(input())


def init_matrix(n):

    matrix = []
    for _ in range(n):
        matrix.append([int(el) for el in input().split()])
    return matrix


def print_result(matrix):
    for row in matrix:
        print(' '.join([str(x) for x in row]))


matrix = init_matrix(n)

bomb_coordinates = input().split()

for bomb in bomb_coordinates:
    tokens = [int(el) for el in bomb.split(',')]
    bomb_row = tokens[0]
    bomb_col = tokens[1]

    if matrix[bomb_row][bomb_col] > 0:
        explode(bomb_row, bomb_col, n, matrix)

alive_cells_count = 0
alive_cells_sum = 0

for row in range(n):
    for col in range(n):
        cell = matrix[row][col]
        if cell > 0:
            alive_cells_count += 1
            alive_cells_sum += cell

print(f"Alive cells: {alive_cells_count}")
print(f"Sum: {alive_cells_sum}")
print_result(matrix)

