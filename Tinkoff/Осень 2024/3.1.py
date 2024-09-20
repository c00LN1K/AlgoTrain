from collections import defaultdict


def find_substrings(s: str, c: set, k: int):
    char_count = defaultdict(int)
    result = []
    start = 0
    unique_chars = 0

    for end in range(len(s)):
        if s[end] in c:
            char_count[s[end]] += 1
            if char_count[s[end]] == 1:
                unique_chars += 1

        while end - start + 1 > k:
            if s[start] in c:
                char_count[s[start]] -= 1
                if char_count[s[start]] == 0:
                    unique_chars -= 1
            start += 1

        if unique_chars == len(c):
            for i in range(start, end + 1):
                substring = s[i:end + 1]
                if not (set(substring).issubset(c) and all(char in substring for char in c)):
                    break
                result.append(substring)

    return result


s = input()
c = set(input())
k = int(input())
subs = find_substrings(s, c, k)
if not subs:
    print(-1)
else:
    ans = start_sub = subs[-1]
    for sub in set(subs):
        if sub.startswith(start_sub) and len(sub) > len(ans):
            ans = sub
    print(ans)


