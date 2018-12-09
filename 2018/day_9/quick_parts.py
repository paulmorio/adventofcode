data_fp = "data.txt"

with open(data_fp, "r") as df:
    line = df.readlines().pop()
    players, max_marble_point = line.split("; ")
    players_count = int(players.split()[0])
    max_marble_point = int(max_marble_point.split()[4])

from collections import deque, defaultdict

def play_game(max_players, last_marble):
    scores = defaultdict(int)
    circle = deque([0])

    for marble in range(1, last_marble + 1):
        if marble % 23 == 0:
            circle.rotate(7)
            scores[marble % max_players] += marble + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(marble)

    return max(scores.values()) if scores else 0

print(play_game(players_count,max_marble_point))
print(play_game(players_count,max_marble_point*100))