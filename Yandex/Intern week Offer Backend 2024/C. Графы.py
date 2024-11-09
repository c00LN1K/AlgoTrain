import math

n = int(input())
n1 = n - 1
comb = (n1 - 1) ** n1
print(comb // 2 * n % (10 ** 9 + 7))
