strings = input().split()

print(*[word for word in strings if len(word) % 2 == 0],sep="\n")