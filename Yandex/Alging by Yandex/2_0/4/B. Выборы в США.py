from collections import defaultdict

d = defaultdict(int)
with open('input.txt', 'r') as file:
    for line in file.readlines():
        candidate, num = line.split()
        d[candidate] += int(num)
for candidate, num in sorted(d.items()):
    print(candidate, num)
