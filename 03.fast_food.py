from collections import deque

food = int(input())

q = deque()
command = input().split()

for el in command:
    q.append(int(el))

print(max(q))

while command:

    current_food = q.popleft()
    if food < current_food:
        print(f'Orders left: {current_food}', *q)
        break
    if len(q) == 0:
        print(f'Orders complete')
        break
    food -= current_food
