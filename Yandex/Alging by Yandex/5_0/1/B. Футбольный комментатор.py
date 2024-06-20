first_match = [int(i) for i in input().split(':')]
second_match = [int(i) for i in input().split(':')]
team_number = int(input())

dif = first_match[1] + second_match[1] - first_match[0] - second_match[0]


if dif < 0:
    print(0)
else:
    if ((team_number == 1 and first_match[1] - second_match[0] >= dif) or
            (team_number == 2 and second_match[1] >= first_match[0])):
        dif += 1
    print(dif)
