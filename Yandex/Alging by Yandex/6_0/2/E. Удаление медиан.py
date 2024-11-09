n = int(input())

lst = sorted(map(int, input().split()))

mid = (n - 1) // 2
ans = []
while len(ans) != n:
    ans.append(lst[mid])
    if (n - len(ans)) % 2 == 1:
        mid += len(ans)
    else:
        mid -= len(ans)

print(*ans)
