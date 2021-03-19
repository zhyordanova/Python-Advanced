characters = input().split(", ")

result = {ch: ord(ch) for ch in characters}
print(result)