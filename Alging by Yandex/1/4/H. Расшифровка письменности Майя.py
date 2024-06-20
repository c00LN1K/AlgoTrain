from collections import Counter


def solve():
    if g > s:
        return 0
    c = Counter(word)
    count = len(c)
    ans = 0
    for right in range(g - 1):
        if sequence[right] in c:
            c[sequence[right]] -= 1
            if not c[sequence[right]]:
                count -= 1

    for right in range(g - 1, s):
        if sequence[right] in c:
            c[sequence[right]] -= 1
            if not c[sequence[right]]:
                count -= 1
        if count == 0:
            ans += 1
        left = right - g + 1
        if sequence[left] in c:
            if c[sequence[left]] == 0:
                count += 1
            c[sequence[left]] += 1

    return ans


if __name__ == '__main__':
    g, s = map(int, input().split())
    word = input()
    sequence = input()
    print(solve())
