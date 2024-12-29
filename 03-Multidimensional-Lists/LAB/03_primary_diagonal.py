def read_matrix(is_test=False):
    if is_test:
        return [
            [11, 2, 4],
            [4, 5, 6],
            [10, 8, - 12],
        ]
    else:
        size = int(input())
        matrix = []
        for row_index in range(size):
            row = list(map(int, input().split()))
            matrix.append(row)
    return matrix


def get_sum_of_primary_diagonal(matrix):
    diagonal_sum = 0
    for r in range(len(matrix)):
        diagonal_sum += matrix[r][r]
    return diagonal_sum


# def get_sum_below_primary_matrix_1(matrix):
#     the_sum = 0
#     size = len(matrix)
#     for r in range(size):
#         for c in range(size):
#             if c <= r:      # including main diagonal
#                 # if c < r: # excluding main diagonal
#                 the_sum += matrix[r][c]
#     return the_sum
#
#
# def get_sum_below_primary_matrix_2(matrix):
#     the_sum = 0
#     size = len(matrix)
#     for r in range(size):
#         for c in range(size):
#             if r <= c:      # including main diagonal
#                 # if r < c: # excluding main diagonal
#                 break
#             the_sum += matrix[r][c]
#     return the_sum
#
#
# def get_sum_below_primary_matrix_3(matrix):
#     the_sum = 0
#     size = len(matrix)
#     for r in range(size):
#         for c in range(r + 1):     # including main diagonal
#             # for c in range(r):   # excluding main diagonal
#
#             the_sum += matrix[r][c]
#     return the_sum
#
#
# def get_sum_above_primary_matrix(matrix):
#     the_sum = 0
#     size = len(matrix)
#     for r in range(size):
#         for c in range(r, size):             # including main diagonal
#             # for c in range(r + 1, size):   # excluding main diagonal
#
#             the_sum += matrix[r][c]
#     return the_sum
#
#
# def get_sum_of_secondary_diagonal(matrix):
#     diagonal_sum = 0
#     size = len(matrix)
#     for r in range(size):
#         diagonal_sum += matrix[i][size - r - 1]
#     return diagonal_sum


print(get_sum_of_primary_diagonal(read_matrix(is_test=True)))




