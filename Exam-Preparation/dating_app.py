from collections import deque


def match_couple(males, females):
    matches = 0
    while males and females:
        current_male = males[-1]
        current_female = females[0]
        if current_male <= 0:
            males.pop()
            continue
        elif current_female <= 0:
            females.popleft()
            continue
        elif current_male % 25 == 0:
            males.pop()
            continue
        elif current_female % 25 == 0:
            females.popleft()
            continue
        elif current_male == current_female:
            males.pop()
            females.popleft()
            matches += 1
        else:
            females.popleft()
            males[-1] -= 2
    return females, males, matches


def print_result(females, males, matches):
    print(f'Matches: {matches}')
    if len(males) == 0:
        print('Males left: none')
    else:
        print(f'Males left: {", ".join([str(el) for el in males[::-1]])}')
    if len(females) == 0:
        print('Females left: none')
    else:
        print(f'Females left: {", ".join([str(el) for el in females])}')


males = [int(s) for s in input().split()]
females = deque([int(s) for s in input().split()])
females, males, matches = match_couple(males, females)
print_result(females, males, matches)
