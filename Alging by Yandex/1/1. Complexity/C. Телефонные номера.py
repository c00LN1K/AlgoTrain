def reformat_number(number: str):
    number = number.replace('-', '').replace(')', '').replace('(', '')
    if len(number) == 7:
        return '495' + number
    return number[-10:]


check_number = reformat_number(input())

for i in range(3):
    print('YES' if check_number == reformat_number(input()) else 'NO')
