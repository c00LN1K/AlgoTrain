n = int(input())
lst = []

for i in range(n):
    l, t = map(int, input().split())
    lst.append((l, 1))
    lst.append((t + l, 0))

lst.sort()
count = 0
ans = 0

for pos, type in lst:
    if type == 1:
        count += 1
        ans = max(ans, count)
    else:
        count -= 1
print(ans)