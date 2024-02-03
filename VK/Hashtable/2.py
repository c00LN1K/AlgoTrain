def check_anagramm(s1, s2):
    if len(s1) != len(s2) or set(s1) != set(s2):
        return 'false'

    letters1 = {}
    letters2 = {}

    for letter1, letter2 in zip(s1, s2):
        letters1[letter1] = letters1.setdefault(letter1, 0) + 1
        letters2[letter2] = letters2.setdefault(letter2, 0) + 1

    for key in letters1:
        if letters1[key] != letters2[key]:
            return 'false'
    return 'true'


s1, s2 = input().split()
print(check_anagramm(s1, s2))
