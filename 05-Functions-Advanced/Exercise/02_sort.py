def sorted_nums(iters):
    return sorted(iters)


numbers = map(lambda x: int(x), input().split())
print(sorted_nums(numbers))