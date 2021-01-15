queries = int(input())
s = []
count = queries
while count > 0:
    command = input().split()

    current_q = command[0]
    if current_q == '1':
        number = int(command[1])
        s.append(number)
    elif current_q == '2':
        if len(s) == 0:
            count -= 1
            continue
        else:
            s.pop()
    elif current_q == '3':
        print(max(s))
    elif current_q == '4':
        print(min(s))
    count -= 1

while s:
    if len(s) == 1:
        print(f'{s.pop()}')
    else:
        print(f'{s.pop()}, ', end='')
