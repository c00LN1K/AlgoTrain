num = int(input())
for _ in range(num):
    s, k = input().split()
    k = int(k)

    n = len(s)
    v = list(s)

    for left in range(n):
        if k <= 0:
            break

        min_pos = left

        for right in range(left + 1, min(n, left + k + 1)):
            if v[right] < v[min_pos]:
                min_pos = right

        if min_pos != left:
            min_digit = v[min_pos]
            for j in range(min_pos, left, -1):
                v[j] = v[j - 1]
            v[left] = min_digit
            k -= (min_pos - left)

    start = next((i for i, c in enumerate(v) if c != '0'), n)
    if start == n:
        print("0")
    else:
        print(''.join(v[start:]))
