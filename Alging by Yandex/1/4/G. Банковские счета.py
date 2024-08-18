from collections import defaultdict

d = defaultdict(int)

with open('input.txt') as file:
    for line in file.readlines():
        if line.startswith('DEPOSIT'):
            _, user, amount = line.split()
            d[user] += int(amount)
        elif line.startswith('WITHDRAW'):
            _, user, amount = line.split()
            d[user] -= int(amount)
        elif line.startswith('BALANCE'):
            _, user = line.split()
            print(d.get(user, 'ERROR'))
        elif line.startswith('TRANSFER'):
            _, user1, user2, amount = line.split()
            d[user1] -= int(amount)
            d[user2] += int(amount)
        elif line.startswith('INCOME'):
            _, p = line.split()
            for user, bal in d.items():
                if bal > 0:
                    d[user] = int(d[user] * (1 + int(p) / 100))
