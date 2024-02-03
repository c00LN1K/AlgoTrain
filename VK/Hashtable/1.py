s = input()
d = {}

for letter in s:
    d[letter] = d.setdefault(letter, 0) + 1

print(max(d.values()))
