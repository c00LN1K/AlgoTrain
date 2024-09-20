from collections import defaultdict

n, b = map(int, input().split())
lst = list(map(int, input().split()))

d = {0: defaultdict(int), 1: defaultdict(int)}
ans = 0
index = 0

while lst[index] != b:
    index += 1

count = 0
for i in range(index, -1, -1):
    if lst[i] > b:
        count += 1
    elif lst[i] < b:
        count -= 1
    d[(index - i) % 2][count] += 1

count = 0
for i in range(index + 1, n):
    if lst[i] > b:
        count += 1
    elif lst[i] < b:
        count -= 1
    ans += d[(i - index) % 2].get(-count, 0)
    
ans += d[0][0]
print(ans)


