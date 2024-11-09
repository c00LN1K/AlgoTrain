def get_time(time):
    h, m, s = map(int, time.split(':'))
    return s + m * 60 + h * 60 * 60


def round(num):
    if num * 10 % 10 < 5:
        return int(num)
    return int(num) + 1


A = get_time(input())
B = get_time(input())
C = get_time(input())
if C < A:
    C += 60 * 60 * 24
curr_time = (B + round((C - A) / 2)) % (60 * 60 * 24)

hours = curr_time // 3600
curr_time -= hours * 3600
minutes = curr_time // 60
curr_time -= minutes * 60
print(f'{hours:02}:{minutes:02}:{curr_time:02}')
