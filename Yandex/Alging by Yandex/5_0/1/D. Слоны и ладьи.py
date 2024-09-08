l = []
f = []

for i in range(8):
    t = input()
    for j in range(8):
        if t[j] != '*':
            f.append((t[j], i, j))
    l.append(t[:8])

for fig, x, y in f:
    for i in range(x, -1, -1):
        pass
