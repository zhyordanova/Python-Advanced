def filtered_even(iters):
    return list(filter(lambda x: x % 2 == 0, iters))


numbers = map(int, input(). split())
print(filtered_even(numbers))