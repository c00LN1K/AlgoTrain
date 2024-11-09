n = int(input())
d = set()
for i in range(n):
    word = input()
    d.add(word[0])

for i in range(97, 122 + 1):
    letter = chr(i)
    if letter in d:
        print(letter, end='')
    else:
        print('.', end='')
    if (i - 97 + 1) % 6 == 0:
        print()
