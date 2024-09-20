lst = list(map(int, input().split()))

shops = [i for i in range(len(lst)) if lst[i] == 2]
shops.append(shops[-1])
shops = iter(shops)
l = r = next(shops)
ans = 0

for i, val in enumerate(lst):
    if val == 1:
       ans = max(ans, min(abs(i - l), abs(i - r)))
    elif val == 2:
        l, r = r, next(shops)

print(ans)
