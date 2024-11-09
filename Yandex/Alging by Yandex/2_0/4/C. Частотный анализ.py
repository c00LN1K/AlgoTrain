from collections import defaultdict

d = defaultdict(int)
with open('input.txt', 'r') as file:
    for line in file.readlines():
        for word in line.split():
            d[word] += 1

print(*sorted(d, key=lambda x: (-d[x], x)), sep='\n')