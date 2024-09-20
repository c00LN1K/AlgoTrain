n = int(input())
lst = list(map(int, input().split()))
last = 0
count = 0
ans = []
for el in lst:
    if el == -1:
        count += 1
        ans.append(1)
    elif el - last >= count + 1:
        ans.append(el - last - count)
        last, count = el, 0
    else:
        ans = []
        break

if ans:
    print('YES')
    print(*ans)
else:
    print('NO')