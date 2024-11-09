from collections import deque

lst1 = deque(map(int, input().split()))
lst2 = deque(map(int, input().split()))

i = 0
while len(lst1) and len(lst2) and i < 10 ** 6:
    i += 1
    val1 = lst1.popleft()
    val2 = lst2.popleft()
    if (val1 == 0 and val2 == 9) or (not (val1 == 9 and val2 == 0) and val1 > val2):
        lst1.append(val1)
        lst1.append(val2)
    else:
        lst2.append(val1)
        lst2.append(val2)

if len(lst1) and not len(lst2):
    print('first', i)
elif len(lst2) and not len(lst1):
    print('second', i)
else:
    print('botva')
