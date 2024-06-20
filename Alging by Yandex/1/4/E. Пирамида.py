from sys import stdin
from collections import defaultdict

d = defaultdict(dict)
for line in stdin:
    user, product, number = line.split()
    d[user][product] = d[user].setdefault(product, 0) + int(number)

for user, products in sorted(d.items()):
    print(f'{user}:')
    for product, number in sorted(products.items()):
        print(product, number)
