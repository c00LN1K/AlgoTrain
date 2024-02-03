digits = {
    1: 'I',
    5: 'V',
    10: 'X',
    50: 'L',
    100: 'C',
    500: 'D',
    1000: 'M',
    4: 'IV',
    9: 'IX',
    40: 'XL',
    90: 'XC',
    400: 'CD',
    900: 'CM'
}

n = input()

ans = []

for i in range(len(n)):
    exp = 10 ** (len(n) - 1 - i)
    digit = int(n[i])
    if digits.get(digit * exp):
        ans.append(digits[digit * exp])
    else:
        c = digit - 5
        if c > 0:
            ans.append(digits[5 * exp])
            ans.append(digits[exp] * c)
        else:
            ans.append(digits[exp] * digit)
print(''.join(ans))
