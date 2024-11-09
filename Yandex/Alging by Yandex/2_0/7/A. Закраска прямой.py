n = int(input())
lst = []

for i in range(n):
    l, r = map(int, input().split())
    lst.append((l, 0))
    lst.append((r, 1))

lst.sort()
count = 0
ans = 0
left = 0

for pos, type in lst:
    if type == 0:
        if count == 0:
            left = pos
        count += 1
    else:
        count -= 1
        if count == 0:
            ans += pos - left

print(ans)