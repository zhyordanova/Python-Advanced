strings = input().split(", ")

print(*[f"{name} -> {len(name)}" for name in strings], sep=", ")