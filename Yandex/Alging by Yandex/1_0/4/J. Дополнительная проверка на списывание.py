from string import digits, ascii_letters

with (open('input.txt') as file):
    n, register, starts_digit = file.readline().split()
    symbols = set(digits + ascii_letters + '_')
    keywords = set()
    for _ in range(int(n)):
        keyword = file.readline().rstrip('\n')
        keywords.add(keyword.lower() if register == 'no' else keyword)
    d = {}
    ans = ''
    t = 0
    for row in map(lambda x: x.rstrip('\n'), file.readlines()):
        if register == 'no':
            row = row.lower()
        for sign in set(row) - set(symbols):
            row = row.replace(sign, ' ')
        for word in row.split():
            if ((starts_digit == 'no' and word[0] not in digits) or starts_digit == 'yes' and not word.isdigit()) \
                    and word not in keywords:
                d.setdefault(word, [0, t])[0] += 1
                t += 1
                if not ans or d[word][0] > d[ans][0] or d[word][0] == d[ans][0] and d[word][1] < d[ans][1]:
                    ans = word
    print(ans)
