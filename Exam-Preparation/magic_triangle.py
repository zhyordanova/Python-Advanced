def get_magic_triangle(rows_count):
    triangle = [[1 for _ in range(row)] for row in range(1, rows_count + 1)]

    for row in range(2, rows_count):
        for col in range(1, row):
            triangle[row][col] = triangle[row - 1][col - 1] + triangle[row - 1][col]

    return triangle


get_magic_triangle(5)