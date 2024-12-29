rows, cols = [int(el) for el in input().split()]


def init_matrix(rows, cols):
    matrix = []
    for _ in range(rows):
        matrix.append(input().split())
    return matrix


def check_if_index_is_valid(row_index, col_index, rows, cols):
    if 0 <= row_index < rows and 0 <= col_index < cols:
        return True
    return False


def check_if_command_is_valid(comand, coords, rows, cols):
    if len(coords) == 4 and command == "swap":
        for index in range(0, len(coords), 2):
            if not check_if_index_is_valid(coords[index], coords[index + 1], rows, cols):
                print("Invalid input!")
                return False
            return True
    print("Invalid input!")
    return False


def print_matrix(matr):
    for row_index in range(0, len(matr)):
        for col_index in range(0, len(matr[row_index])):
            print(f"{matr[row_index][col_index]} ",  end='')
        print()



matrix = init_matrix(rows, cols)

data = input()

while not data == "END":
    try:
        split_data = data.split()
        command = split_data[0]
        coordinates = [int(el) for el in split_data[1:]]
        if check_if_command_is_valid(command, coordinates, rows, cols):
            current_row = coordinates[0]
            current_col = coordinates[1]
            row_to_swap = coordinates[2]
            col_to_swap = coordinates[3]
            matrix[current_row][current_col], matrix[row_to_swap][col_to_swap] = matrix[row_to_swap][col_to_swap], \
                                                                                 matrix[current_row][current_col]
            print_matrix(matrix)
    except:
        print("Invalid input!")

    data = input()