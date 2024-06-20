n, k = map(int, input().split())
lst = list(map(int, input().split()))

if k >= (n - 1):
    print("NO" if len(lst) == len(set(lst)) else "YES")
else:
    right = k + 1
    t = set(lst[:right])
    if right != len(t):
        print('YES')
    else:
        while right < len(lst):
            t.discard(lst[right - k - 1])
            if lst[right] in t:
                print("YES")
                break
            t.add(lst[right])
            right += 1
        else:
            print("NO")
