n, k, d = map(int, input().split())

t = n * 10
flag = 0

for i in range(10):
    if (t + i) % k == 0:
        t += i
        break
else:
    flag = 1

print(-1 if flag else ''.join([str(t)] + ['0' for i in range(d - 1)]))
