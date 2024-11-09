n, m = map(int, input().split())
groups = []
auds = []
for i, group in enumerate(map(int, input().split())):
    groups.append((group, i))
groups.sort(reverse=True)
for i, aud in enumerate(map(int, input().split())):
    auds.append((aud, i))
auds.sort(reverse=True)

ans = [0] * len(groups)
r = 0
for l in range(len(groups)):
    if groups[l][0] < auds[r][0]:
        ans[groups[l][1]] = auds[r][1] + 1
        r += 1

print(r)
print(*ans)
