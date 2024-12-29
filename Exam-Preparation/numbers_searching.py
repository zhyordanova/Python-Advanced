def get_missing_value(numbers):
    start_range = min(numbers)
    end_range = max(numbers)
    missing_value = [num for num in range(start_range, end_range +1) if num not in numbers]
    return missing_value[0]


def get_duplicate_value(numbers):
    duplicates = set([num for num in numbers if numbers.count(num) > 1])
    return list(sorted(duplicates))


def numbers_searching(*args):
    numbers = list(args)
    missing_value = get_missing_value(numbers)
    duplicates = get_duplicate_value(numbers)
    return [missing_value, duplicates]



print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))