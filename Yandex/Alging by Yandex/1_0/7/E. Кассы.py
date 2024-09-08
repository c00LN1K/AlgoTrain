def solve():
    n = int(input())

    times = []
    ans = 0
    st = 24 * 60
    curr = set()

    for i in range(n):
        st_h, st_m, end_h, end_m = map(int, input().split())
        if st_m == end_m and end_h == st_h:
            n -= 1
            continue
        times.append((st_h * 60 + st_m, 0, i))
        times.append((end_h * 60 + end_m, 1, i))

    if n == 0:
        return st

    times.sort()
    for time, type, i in times:
        if type == 0:
            curr.add(i)
            if len(curr) == n:
                st = time

        elif type == 1 and i in curr:
            curr.remove(i)

    for time, type, i in times:
        if type == 0:
            curr.add(i)
            if len(curr) == n:
                st = time

        elif type == 1 and i in curr:
            if len(curr) == n:
                ans += time + 24 * 60 - st if st > time else time - st
            curr.remove(i)

    return ans

if __name__ == '__main__':
    print(solve())


