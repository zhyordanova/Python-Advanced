values = map(float, input().split())

values_counts = {}
for value in values:
    if value not in values_counts:
        values_counts[value] = 0
    values_counts[value] += 1

[print(f"{key} - {value} times") for key, value in values_counts.items()]
