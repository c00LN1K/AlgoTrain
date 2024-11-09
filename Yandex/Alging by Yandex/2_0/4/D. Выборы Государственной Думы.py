from collections import defaultdict

s = 0
parties = defaultdict(int)
with open('input.txt', 'r') as file:
    for line in file.readlines():
        party, number = line.rsplit(maxsplit=1)
        parties[party] += int(number)
        s += int(number)
s = s / 450
d = defaultdict(int)
places = 450
d1 = defaultdict(int)
for party, number in parties.items():
    d[party] = parties[party] // s
    d1[party] = parties[party] / s % 1
    places -= d[party]

i = 0
extra = sorted(d1, key=lambda x: d1[x], reverse=True)
while places - i:
    d[extra[i]] += 1
    i += 1

for party, num in d.items():
    print(party, int(num))