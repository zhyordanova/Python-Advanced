lists = [outer_list.split() for outer_list in input().split('|')]

outer_list = [el for list in reversed(lists) for el in list]

print(' '.join(outer_list))