import math
from collections import defaultdict


def primfacs(n):
   i = 2
   primfac = defaultdict(int)
   while i * i <= n:
       while n % i == 0:
           primfac[i] += 1
           n = n / i
       i = i + 1
   if n > 1:
       primfac[n] += 1
   return primfac

l, r = map(int, input().split())
ans = 0
for degree in range(max(2, math.ceil(l ** 0.5)), math.floor(r ** 0.5) + 1):
    num = degree
    primers = primfacs(num)
    num_dividers = 1
    for val in primers.values():
        num_dividers *= (val * 2 + 1)
    for i in range(2, math.floor(num_dividers ** 0.5) + 1):
        if num_dividers % i == 0:
            break
    else:
        ans += 1
print(ans)
