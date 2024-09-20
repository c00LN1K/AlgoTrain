n = int(input())
line = []
for i in range(n):
    st, end = map(int, input().split())
    if end - st < 5:
        continue
    line.append((st, 0, i))
    line.append((end, 1, i))

line.sort()
variants = []
visitors = set()
stack = []

for pos, type, i in line:
    if type == 0:
        stack.append((pos, i))
    elif type == 1:
        new_stack = []
        t = set()
        for p, ii in stack:
            if pos - p >= 5:
                t.add(ii)
            if ii != i:
                new_stack.append((p, ii))
        variants.append((pos, t))
        stack = new_stack

ans = [0, 0, set()]
for i, (end, s) in enumerate(variants):
    t = [end, end, s]
    for j in range(i + 1, len(variants)):
        if variants[j][0] - end >= 5 and len(s | variants[j][1]) > len(t[2]):
            t = [end, variants[j][0], s | variants[j][1]]
    if len(ans[2]) < len(t[2]):
        ans = t

print(len(ans[2]), ans[0] - 5, ans[1] - 5 if ans[0] != ans[1] else ans[1] + 1)
