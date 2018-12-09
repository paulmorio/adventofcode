"""
Solution Code for Day 9 Part 1
For a much better and faster solutions using a dequeue look at quickparts.py
"""
from collections import defaultdict
data_fp = "data.txt"

with open(data_fp, "r") as df:
	line = df.readlines().pop()
	players, max_marble_point = line.split("; ")
	players_count = int(players.split()[0])
	max_marble_point = int(max_marble_point.split()[4])

player_points = defaultdict(list)
marble_circle = [0]
index_current = 1
current_marble = 1
current_player = 1

# AAAAANNDD I'm an idiot this is a deque (double ended queue that I could have used)
def wrap_around_insert(value):
	# between 1 and 2 spaces away
	global marble_circle
	global index_current
	if index_current + 1 > len(marble_circle):
		index_current = 1
		marble_circle.insert(index_current, value)
		index_current += 1
	else:
		index_current += 1
		marble_circle.insert(index_current, value)
		index_current += 1

while current_marble <= max_marble_point*100: # <---- the only change
	if current_marble % 10000 == 0:
		print ("%s of %s" % (current_marble, max_marble_point*100))
	if current_player > players_count:
		current_player = 1
	if current_marble % 23 == 0:
		player_points[current_player].append(current_marble)
		index_current = (index_current-7) % len(marble_circle)
		player_points[current_player].append(marble_circle.pop((index_current-1)%len(marble_circle)))

		# turn ending stuff
		current_marble+=1
		current_player+=1

	else:
		wrap_around_insert(current_marble)

		# turn ending stuff
		current_marble+=1
		current_player+=1

# Answer
a = defaultdict(int)
for p in player_points.keys():
	a[p] = sum(player_points[p])

print(max([sum(player_points[x]) for x in player_points.keys()]))