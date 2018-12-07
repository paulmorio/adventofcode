# Solution Code for Day 6 part 1
# Judiciously stolen and changed adapted to python 3 based on answer on reddit
# This is not truly my solution

from collections import Counter

# Could be written into a single list comprehension line as commented below
data_fp = "data.txt"
data = []
max_x = 0
max_y = 0
with open(data_fp, "r") as df:
	lines = df.readlines()
	for line in lines:
		x, y = line.split(", ")
		x = int(x.strip())
		y = int(y.strip())
		data.append([x,y])
		# find out area bounds
		if x >= max_x:
			max_x = x
		if y >= max_y:
			max_y = y


# data = [map(int, i.split(', ')) for i in open('data.txt').readlines()]

grid = {}
for i in range(max_x):
	for j in range(max_y):
		m = min(abs(i-k) + abs(j-l) for k, l in data)
		for n, (k,l) in enumerate(data):
			if abs(i-k) + abs(j-l) == m:
				if grid.get((i,j), -1) != -1:
					grid[i, j] = -1
					break
				grid[i, j] = n

s = set([-1])
s = s.union(set(grid[x, max_y-1] for x in range(max_x)))
s = s.union(set(grid[x, 0] for x in range(max_x)))
s = s.union(set(grid[max_x-1, y] for y in range(max_y)))
s = s.union(set(grid[0, y] for y in range(max_y)))

# Part 1 answer
print (next(i[1] for i in Counter(grid.values()).most_common() if i[0] not in s))

# Part 2 answer
print (sum(sum(abs(i-k)+abs(j-l) for k, l in data) < 10000 for i in range(max_x) for j in range(max_y)))