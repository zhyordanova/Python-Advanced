SNAKE_SYMBOL = 'S'
BURROW_SYMBOL = 'B'
FOOD_SYMBOL = '*'
EMPTY_SYMBOL = '-'
TRAIL_SYMBOL = '.'


def read_matrix():
    size = int(input())
    matrix = []
    for i in range(size):
        matrix.append(list(input()))
    return matrix


def search_position(board, symbol):
    for row_index in range(len(board)):
        for col_index in range(len(board)):
            if board[row_index][col_index] == symbol:
                return row_index, col_index


def get_new_position(command, snake_position):
    new_row, new_col = snake_position[0], snake_position[1]

    if command == "up":
        new_row -= 1
    elif command == "down":
        new_row += 1
    elif command == "left":
        new_col -= 1
    elif command == "right":
        new_col += 1
    return new_row, new_col


def is_valid(row, col, board):
    return 0 <= row < len(board) and 0 <= col < len(board)


def print_result(food_quantity, board):
    print(f"Food eaten: {food_quantity}")
    [print(''.join(row)) for row in board]


board = read_matrix()
snake_position = search_position(board, SNAKE_SYMBOL)
food_quantity = 0


while food_quantity < 10:
    command = input()
    new_row, new_col = get_new_position(command, snake_position)

    if not is_valid(new_row, new_col, board):
        board[snake_position[0]][snake_position[1]] = TRAIL_SYMBOL
        print('Game over!')
        break

    elif board[new_row][new_col] == FOOD_SYMBOL:
        food_quantity += 1

    elif board[new_row][new_col] == BURROW_SYMBOL:
        board[new_row][new_col] = TRAIL_SYMBOL
        new_row, new_col = search_position(board, BURROW_SYMBOL)

    board[new_row][new_col] = SNAKE_SYMBOL
    board[snake_position[0]][snake_position[1]] = TRAIL_SYMBOL
    snake_position = search_position(board, SNAKE_SYMBOL)

else:
    print('You won! You fed the snake.')

print_result(food_quantity, board)
