import math

n = int(input())
t_shirts = list(map(int, input().split()))
m = int(input())
pants = list(map(int, input().split()))

if t_shirts[0] >= pants[-1]:
    print(t_shirts[0], pants[-1])
elif pants[0] >= t_shirts[-1]:
    print(t_shirts[-1], pants[0])
else:
    i, j = 0, 0
    ans = [-math.inf, math.inf]
    while i < n and j < m:
        if t_shirts[i] == pants[j]:
            ans = [t_shirts[i], pants[j]]
            break
        elif t_shirts[i] > pants[j]:
            if (t_shirts[i] - pants[j]) < abs(ans[1] - ans[0]):
                ans = [t_shirts[i], pants[j]]
            j += 1
        else:
            if (pants[j] - t_shirts[i]) < abs(ans[1] - ans[0]):
                ans = [t_shirts[i], pants[j]]
            i += 1
    print(*ans)
