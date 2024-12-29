integers = input().split()

stack = []

while integers:
    next_integers = integers.pop()
    stack.append(next_integers)

print(' '.join(stack))git