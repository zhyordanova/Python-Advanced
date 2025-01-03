def add_value(matr, r, c, v):
    matr[r][c] += v
    return matr


def subtract(matr, r, c, v):
    matr[r][c] -= v
    return matr


n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]

while True:
    line = input()
    if line == "END":
        break
    tokens = line.split()
    row = int(tokens[1])
    col = int(tokens[2])
    value = int(tokens[3])

    if 0 <= row < n and 0 <= col < n:
        if tokens[0] == "Add":
            matrix = add_value(matrix, row, col, value)
        elif tokens[0] == "Subtract":
            matrix = subtract(matrix, row, col, value)
    else:
        print("Invalid coordinates")


[print(' '.join([str(x)for x in row])) for row in matrix]
