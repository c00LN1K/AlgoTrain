from collections import defaultdict

s = input() + '#'
letters = set(input())
k = int(input())
d = defaultdict(int)
l = 0
count = 0
passwords = []
for r, letter in enumerate(s):
    if letter in letters and count < k:
        d[letter] += 1
        count += 1
    elif letter not in letters:
        while len(letters) == len(d):
            passwords.append(s[l:r])
            d[s[l]] -= 1
            if d[s[l]] == 0:
                d.pop(s[l])
            l += 1
        l = r + 1
        count = 0

    if count >= k:
        while count >= k and len(letters) == len(d):
            passwords.append(s[l:r+1])
            d[s[l]] -= 1
            count -= 1
            if d[s[l]] == 0:
                d.pop(s[l])
            l += 1
    elif len(letters) == len(d):
        passwords.append(s[l:r+1])

print(passwords)
