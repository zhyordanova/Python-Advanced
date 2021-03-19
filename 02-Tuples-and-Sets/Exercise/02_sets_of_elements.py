n_length, m_length = list(map(int, input().split()))

n = set()
m = set()

for _ in range(n_length):
    number = int(input())
    n.add(number)

for _ in range(m_length):
    number = int(input())
    m.add(number)

intersection = n.intersection(m)

modified_intersection = (map(str, intersection))
print('\n'.join(modified_intersection))