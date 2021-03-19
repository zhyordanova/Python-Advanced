from sys import maxsize


def find_subrectangle_sum(matrix, row, col):
    subrectangle_sum = 0

    for r in range(row, row + 3):
        for c in range(col, col + 3):
            subrectangle_sum += matrix[r][c]

    return subrectangle_sum


def find_subrectangle_values(matrix, row, col):
    subrectangle_values = []

    for r in range(row, row + 3):
        subrectangle_row = []
        for c in range(col, col + 3):
            subrectangle_row += [matrix[r][c]]
        subrectangle_values += [subrectangle_row]

    return subrectangle_values


def solve(matrix, rows_count, cols_count):
    max_subrectangle_sum = -maxsize
    max_subrectangle_values = []

    for row in range(rows_count - 2):
        for col in range(cols_count - 2):
            subrectangle_sum = find_subrectangle_sum(matrix, row, col)
            if subrectangle_sum > max_subrectangle_sum:
                max_subrectangle_sum = subrectangle_sum
                max_subrectangle_values = find_subrectangle_values(matrix, row, col)

    return max_subrectangle_sum, max_subrectangle_values


rows_count, cols_count = list(map(int, input().split()))
matrix = [list(map(int, input().split())) for _ in range(rows_count)]

max_subrectangle_sum, max_subrectangle_values = solve(matrix, rows_count, cols_count)

print(f"Sum = {max_subrectangle_sum}")
[print(' '.join(map(str, row))) for row in max_subrectangle_values]
