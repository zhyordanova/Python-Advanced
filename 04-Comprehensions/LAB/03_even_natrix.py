def stars_to_ints(strs):
    return [int(x) for x in strs]


def read_matrix():
    rows_count = int(input())
    return [stars_to_ints(input().split(", ")) for _ in range(rows_count)]


def get_eve_matrix(matrix):
    return [[x for x in row if x % 2 == 0] for row in matrix]


def print_result(matrix):
    print(matrix)



matrix = read_matrix()
even_matrix = get_eve_matrix(matrix)
print_result(even_matrix)