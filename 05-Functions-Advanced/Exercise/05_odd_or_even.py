def odd_sum(nums):
    return sum(filter(lambda x: x % 2 == 1, nums))


def even_sum(nums):
    return sum(filter(lambda x: x % 2 == 0, nums))


command = input()
numbers = list(map(int, input().split()))


if command == "Odd":
    print(odd_sum(numbers) * len(numbers))
elif command == "Even":
    print(even_sum(numbers) * len(numbers))

