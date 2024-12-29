from collections import deque

customers = deque([int(el) for el in input().split(', ')])
taxis = [int(el) for el in input().split(', ')]

total_time = 0

while customers and taxis:
    current_customer = customers.popleft()
    current_taxis = taxis.pop()

    if current_customer <= current_taxis:
        total_time += current_customer
    else:
        customers.appendleft(current_customer)

if not customers:
    print('All customers were driven to their destinations')
    print(f'Total time: {total_time} minutes')
else:
    print('Not all customers were driven to their destinations')
    print(f'Customers left: {", ".join(str(el) for el in customers)}')





