n = int(input())

even_numbers_set = set()
odd_numbers_set = set()

for current_iteration_count in range(1, n + 1):
    name = input()
    current_sum = sum([ord(el) for el in name]) // current_iteration_count
    if current_sum % 2 == 0:
        even_numbers_set.add(current_sum)
    else:
        odd_numbers_set.add(current_sum)

even_sum = sum(even_numbers_set)
odd_sum = sum(odd_numbers_set)

if even_sum == odd_sum:
    modified_set = [str(el) for el in even_numbers_set.union(odd_numbers_set)]
    print(f"{', '.join(modified_set)}")
elif odd_sum > even_sum:
    modified_set = [str(el) for el in odd_numbers_set.difference(even_numbers_set)]
    print(f"{', '.join(modified_set)}")
else:
    modified_set = [str(el) for el in even_numbers_set.symmetric_difference(odd_numbers_set)]
    print(f"{', '.join(modified_set)}")
