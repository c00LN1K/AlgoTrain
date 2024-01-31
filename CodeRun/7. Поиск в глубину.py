def dfs(start):
    ways = d.get(start, [])
    for top in ways:
        if top not in was:
            was.append(top)
            dfs(top)


n, m = map(int, input().split())

d = {}
was = [1]

for i in range(m):
    a, b = map(int, input().split())
    if a != b:
        d.setdefault(a, []).append(b)
        d.setdefault(b, []).append(a)

dfs(1)
print(len(was))
print(*sorted(was))
