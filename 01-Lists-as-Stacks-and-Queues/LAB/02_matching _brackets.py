expression = input()

stack = []

for i in range(len(expression)):
    ch = expression[i]
    if ch == "(":
        stack.append(i)
    elif ch == ")":
        j = stack.pop()
        print(expression[j:i + 1])