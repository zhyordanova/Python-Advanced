from itertools import permutations

text = list(input())
print(*[f"{''.join(el)}" for el in list(permutations(text))], sep='\n')