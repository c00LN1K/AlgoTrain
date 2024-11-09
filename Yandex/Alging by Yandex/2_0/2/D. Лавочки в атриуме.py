from bisect import bisect_left

l, k = map(int, input().split())
legs = list(map(int, input().split()))
mid = l // 2
index = bisect_left(legs, mid)
if l % 2 == 1 and legs[index] == mid:
    print(mid)
else:
    print(legs[index - 1], legs[index])
