from collections import defaultdict

n = int(input())
d = defaultdict(set)
for _ in range(n):
    word = input()
    for i, letter in enumerate(word):
        if letter.isupper():
            d[word.lower()].add(i)
ans = 0
hw = input()
for word in hw.split():
    was_upper = -1
    for i, letter in enumerate(word):
        if letter.isupper():
            if was_upper == -1:
                was_upper = i
            else:
                was_upper = -1
                break
    if was_upper == -1 or was_upper not in d.get(word.lower(), {was_upper}):
        ans += 1

print(ans)
