from itertools import count

k = int(input())

for _ in range(k):
    data = list(map(int, input().split()))
    n = data[0]
    line = []
    for i in range(n):
        line.append((data[i * 2 + 1] + 1, 0))
        line.append((data[i * 2 + 2], 1))
    line.sort()
    left = 0
    count = 0
    abc = 0
    for pos, type in line:
        if type == 0:
            if count == 0:
                left = pos
            count += 1
        elif type == 1:
            count -= 1
            if count == 0:
                abc += pos - left + 1
    print(abc)



