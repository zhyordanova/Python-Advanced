from collections import deque


def add_elements(list_of_numbers, position, numbers):
    if position == 'beginning':
        list_of_numbers.extendleft(reversed(numbers))
    elif position == 'end':
        list_of_numbers.extend(numbers)
    return list_of_numbers


def remove_elements(list_of_numbers, position, numbers):
    if numbers:
        num_to_remove = numbers[0]
        for i in range(num_to_remove):
            if position == 'beginning':
                list_of_numbers.popleft()
            elif position == 'end':
                list_of_numbers.pop()
    else:
        if position == 'beginning':
            list_of_numbers.popleft()
        elif position == 'end':
            list_of_numbers.pop()
    return list_of_numbers


def list_manipulator(list_of_numbers, operation, position, *args):
    list_of_numbers = deque(list_of_numbers)
    numbers = list(args)


    if operation == 'add':
        list_of_numbers = add_elements(list_of_numbers, position, numbers)
    elif operation == "remove":
        list_of_numbers = remove_elements(list_of_numbers, position, numbers)

    list_of_numbers = [el for el in list_of_numbers]
    return list_of_numbers


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
