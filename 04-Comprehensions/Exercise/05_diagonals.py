def create_row():
    row = input().split(", ")
    return [int(col) for col in row]


n = int(input())

matrix = [create_row() for row in range(n)]

first_diagonal = [matrix[row][col] for row in range(n) for col in range(n) if row == col]
second_diagonal = [matrix[row][col] for row in range(n) for col in range(n) if n - 1 - row == col]

print(f"First diagonal: {', '.join(map(str, first_diagonal))}. Sum: {sum(first_diagonal)}")
print(f"Second diagonal: {', '.join(map(str, second_diagonal))}. Sum: {sum(second_diagonal)}")