def findWinners(matches):
    players = {}
    players_without_loses = []
    players_with_lose = []

    for winner, losser in matches:
        players[losser] = players.setdefault(losser, 0) + 1
        players.setdefault(winner, 0)

    for player, number_loses in players.items():
        if number_loses == 0:
            players_without_loses += [player]
        elif number_loses == 1:
            players_with_lose.append(player)

    return [sorted(players_without_loses), sorted(players_with_lose)]


print(findWinners(([[2,3],[1,3],[5,4],[6,4]])))
