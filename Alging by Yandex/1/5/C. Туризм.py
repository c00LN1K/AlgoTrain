n = int(input())
coords = sorted(tuple(map(int, input().split())) for i in range(n))
prefix_forward = [0] * (n + 1)
prefix_back = [0] * (n + 1)
for i in range(1, n):
    dif = coords[i][1] - coords[i - 1][1]
    prefix_forward[i + 1] = prefix_forward[i] + dif if dif > 0 else prefix_forward[i]
    prefix_back[i + 1] = prefix_back[i] - dif if dif < 0 else prefix_back[i]

m = int(input())
for i in range(m):
    l, r = map(int, input().split())
    print((prefix_forward[r] - prefix_forward[l]) if l < r else (prefix_back[l] - prefix_back[r]))
