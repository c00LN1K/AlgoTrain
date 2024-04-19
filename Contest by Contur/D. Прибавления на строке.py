dict_from_int_to_char = {0: 'a', 1: 'A', 2: 'b', 3: 'B', 4: 'c', 5: 'C', 6: 'd', 7: 'D', 8: 'e', 9: 'E', 10: 'f',
                         11: 'F', 12: 'g', 13: 'G',
                         14: 'h', 15: 'H', 16: 'i', 17: 'I', 18: 'j', 19: 'J', 20: 'k', 21: 'K', 22: 'l', 23: 'L',
                         24: 'm', 25: 'M',
                         26: 'n', 27: 'N', 28: 'o', 29: 'O', 30: 'p', 31: 'P', 32: 'q', 33: 'Q', 34: 'r', 35: 'R',
                         36: 's', 37: 'S',
                         38: 't', 39: 'T', 40: 'u', 41: 'U', 42: 'v', 43: 'V', 44: 'w', 45: 'W', 46: 'x', 47: 'X',
                         48: 'y', 49: 'Y',
                         50: 'z', 51: 'Z'}

dict_from_char_to_int = {'a': 0, 'A': 1, 'b': 2, 'B': 3, 'c': 4, 'C': 5, 'd': 6, 'D': 7, 'e': 8, 'E': 9, 'f': 10,
                         'F': 11, 'g': 12,
                         'G': 13, 'h': 14, 'H': 15, 'i': 16, 'I': 17, 'j': 18, 'J': 19, 'k': 20, 'K': 21, 'l': 22,
                         'L': 23, 'm': 24,
                         'M': 25, 'n': 26, 'N': 27, 'o': 28, 'O': 29, 'p': 30, 'P': 31, 'q': 32, 'Q': 33, 'r': 34,
                         'R': 35, 's': 36,
                         'S': 37, 't': 38, 'T': 39, 'u': 40, 'U': 41, 'v': 42, 'V': 43, 'w': 44, 'W': 45, 'x': 46,
                         'X': 47, 'y': 48,
                         'Y': 49, 'z': 50, 'Z': 51}

s = input()
q = int(input())
n = len(dict_from_int_to_char)
letters = [0] * len(s)

for _ in range(q):
    l, r, x = map(int, input().split())
    for i in range(l - 1, r):
        letters[i] += x

for i in range(len(s)):
    if letters[i]:
        print(dict_from_int_to_char[(letters[i] + dict_from_char_to_int[s[i]]) % n], end='')
    else:
        print(s[i], end='')
