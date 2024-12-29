def min_numbers(iters):
    return min(iters)


def max_numbers(iters):
    return max(iters)


def sum_numbers(iters):
    return sum(iters)


numbers = list(map(int, input().split()))
print(f'The minimum number is {min_numbers(numbers)}')
print(f'The maximum number is {max_numbers(numbers)}')
print(f'The sum number is: {sum_numbers(numbers)}')


