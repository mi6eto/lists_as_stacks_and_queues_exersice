clothes = input().split()

s = []

for c in clothes:
    s.append(int(c))

capacity = int(input())
racks = 0
sum = 0

while s:
    current_cloth = s.pop()
    sum += current_cloth
    if len(s) == 0:
        racks += 1
        if sum > capacity:
            sum = current_cloth
            racks += 1
        break

    if capacity > sum:
        continue
    if capacity == sum:
        racks += 1
        sum = 0
        continue
    if sum > capacity:
        sum = current_cloth
        racks += 1
        continue

print(racks)
