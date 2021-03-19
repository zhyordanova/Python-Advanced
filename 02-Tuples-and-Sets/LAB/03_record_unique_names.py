def input_to_list(count):
    lines = []
    for _ in range(count):
        lines.append(input())
    return lines


def print_result(names):
    for name in names:
        print(name)


n = int(input())
names = input_to_list(n)

unique_names = set(names)

print_result(unique_names)
