rows, cols = [int(el) for el in input().split()]


def init_matrix():
    matrix = []
    for _ in range(rows):
        matrix.append(input().split())

    return matrix


def check_elements_are_equal(row, col, matr):
    current_element = matr[row][col]
    next_element_same_row = matr[row][col + 1]
    element_bottom = matr[row + 1][col]
    element_bottom_right = matr[row + 1][col + 1]
    if current_element == next_element_same_row and next_element_same_row == element_bottom and element_bottom == element_bottom_right:
        return True
    return False


matrix = init_matrix()

counter = 0

for row_index in range(rows - 1):
    for col_index in range(cols - 1):
        if check_elements_are_equal(row_index, col_index, matrix):
            counter += 1

print(counter)
