n = int(input())
l = list(map(int, input().split()))
summ, maxx = sum(l), max(l)
ans = summ

if 2 * maxx - summ > 0:
    ans = min(summ, 2 * maxx - summ)
print(ans)
