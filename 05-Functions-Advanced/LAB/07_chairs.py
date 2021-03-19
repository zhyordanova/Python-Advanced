from itertools import combinations

names = input().split(', ')
n = int(input())

print(*[f"{', '.join(el)}" for el in list(combinations(names, n))], sep="\n")