from collections import defaultdict


def is_descendant(curr, descendant):
    if curr == descendant:
        return True
    for child in d[curr]:
        res = is_descendant(child, descendant)
        if res:
            return res


with open('input.txt') as file:
    ans = []
    n = int(file.readline())
    d = defaultdict(list)
    for _ in range(n - 1):
        child, parent = file.readline().split()
        d[parent].append(child)
    for line in file.readlines():
        line = line.strip('\n')
        if not line:
            continue
        first, second = line.split()
        if first == second:
            ans.append(0)
        elif is_descendant(first, descendant=second):
            ans.append(1)
        elif is_descendant(second, descendant=first):
            ans.append(2)
        else:
            ans.append(0)
    print(*ans)