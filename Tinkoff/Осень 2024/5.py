st_h, st_m, st_s = map(int, input().split(':'))
n = int(input())
start_time = st_h * 3600 + st_m * 60 + st_s
teams = {}

for _ in range(n):
    team, time, server, status = input().split()
    teams.setdefault(team, {})
    teams[team].setdefault(server, [0, 0])
    if status in {'FORBIDEN', 'DENIED'}:
        teams[team][server][1] += 20
    elif status == 'ACCESSED':
        h, m, s = map(int, time.split(':'))
        time = h * 3600 + m * 60 + s
        if time < start_time:
            time += 24 * 60 * 60
        teams[team][server][1] += (time - start_time) // 60
        teams[team][server][0] = 1

res = []
for team, servers in teams.items():
    t = [0, 0]
    for server, status in servers.items():
        if status[0]:
            t[0] += 1
            t[1] += status[1]
    res.append((-t[0], t[1], team))

res = sorted(res)
last_place = 0
prev = [1, 1]
for i, (servers_nums, fine, name) in enumerate(res):
    if prev != [servers_nums, fine]:
        last_place = i + 1
    print(last_place, name, -servers_nums, fine)
    prev = [servers_nums, fine]



