from collections import deque

rows, cols = [int(el) for el in input().split()]

word = deque(input())

matrix = []

for row in range(rows):
    matrix.append([0 for el in range(cols)])

index_word = 0


for row_index in range(rows):
    for col_index in range(cols):
        current_char = word.popleft()
        # matrix[row_index][col_index] = word[index_word]
        matrix[row_index][col_index] = current_char
        word.append(current_char)


for row_index in range(rows):
    if row_index % 2 == 1:
        matrix[row_index].reverse()
    print(''.join(matrix[row_index]))