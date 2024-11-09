m = int(input())
lst = []
i = 0
while True:
    l, r = map(int, input().split())
    if l == r == 0:
        break
    if r < 0 or l > m:
        continue
    lst.append((l, r))

lst.sort()
curr_right = 0
curr_best = 0, 0
ans = []
for l, r in lst:
    if l > curr_right:
        ans.append(curr_best)
        curr_right = curr_best[1]
    if l <= curr_right:
        if r > curr_best[1]:
            curr_best = l, r
            if curr_best[1] >= m:
                break


if curr_right != curr_best[1]:
    ans.append(curr_best)
    curr_right = curr_best[1]

if curr_right < m:
    print('No solution')
else:
    print(len(ans))
    for el in ans:
        print(*el)
