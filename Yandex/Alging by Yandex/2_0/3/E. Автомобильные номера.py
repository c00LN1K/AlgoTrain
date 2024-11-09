from collections import defaultdict

vars = []
for _ in range(int(input())):
    vars.append(set(input()))

ans = []
d = defaultdict(list)
for _ in range(int(input())):
    number = input()
    symbols = set(number)
    t = 0
    for var in vars:
        if var.issubset(symbols):
            t += 1
    d[t].append(number)
print(*d[max(d)], sep='\n')