from collections import Counter, defaultdict

with open('input.txt') as file:
    d = defaultdict(int)
    height = 0
    for line in file.readlines():
        for word in line.split():
            for letter, value in Counter(word).items():
                d[letter] += value
                height = max(height, d[letter])
    names = sorted(d.keys())
    for row in range(height, 0, -1):
        for name in names:
            if row - d[name] <= 0:
                print('#', end='')
            else:
                print(' ', end='')
        print()
    print(*names, sep='')
