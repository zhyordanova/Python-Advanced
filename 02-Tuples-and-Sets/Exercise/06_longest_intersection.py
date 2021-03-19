n = int(input())

intersections = []

for _ in range(n):
    data = input()
    first_seq_data, second_seq_data = data.split("-")
    star, stop = [int(el) for el in first_seq_data.split(',')]
    first_seq = range(star, stop + 1)
    star, stop = [int(el) for el in second_seq_data.split(',')]
    second_seq = range(star, stop + 1)
    intersection = set(first_seq).intersection(second_seq)
    intersections.append(intersection)


longest = sorted(intersections, key=lambda x: -len(x))[0]
print(f"Longest intersection is {list(longest)} with length {len(longest)}")
