# Solution to Day 3 Part 1
from collections import defaultdict

data_fp = "data.txt"
fabric_size = 1000 # *fabric_size sq inches

with open(data_fp, "r") as df:
	lines = df.readlines()

fabric_claims = defaultdict(list) # list with (x,y) type keys
cut_claims = []
for claim in lines:
	# cleaning and putting in dictionary
	clid, _, left_corner_coord, size = claim.split()
	clid = int(clid[1:].strip())
	left_corner_coord = left_corner_coord[:-1].strip()
	start_x, start_y = list(map(int,left_corner_coord.split(",")))
	size_x, size_y = list(map(int, size.split("x")))
	cut_claims.append((clid, start_x, start_y, size_x, size_y))

# the areas in tuples which a claim will take
def claim_areas(claim_command):
	results = []
	x = claim_command[1] # start x
	y = claim_command[2] # start y
	for i in range(claim_command[3]):
		for j in range(claim_command[4]):
			results.append((x+i, y+j))

	return results

# put the stakes in each of the areas
for claim in cut_claims:
	clid = claim[0]
	for area in claim_areas(claim):
		fabric_claims[area].append(clid)

# find out which areas have multiple claims and how many of them exist
counter = 0
for area in fabric_claims.keys():
	if len(fabric_claims[area]) >= 2:
		counter+=1
print(counter)
for area in fabric_claims.keys():
	if area[0] > fabric_size-1 or area[1] > fabric_size-1:
		counter-=1
print(counter)

