# Solution Code for Day 2 part 2
from collections import Counter
from itertools import permutations

def match(s1, s2):
    pos = -1

    for i, (c1, c2) in enumerate(zip(s1, s2)):
        if c1 != c2:
            if pos != -1:
                return -1
            else:
                pos = i

    return pos

def match_bool(s1, s2):
    ok = False

    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            if ok:
                return False
            else:
                ok = True

    return ok

data_file = "data.txt"


id_list = []
with open(data_file, "r") as df:
	# read the files and make counter objects for all the box ids
	lines = df.readlines()
	for line in lines:
		box_id = list(line.strip())
		id_list.append(box_id)

solutions = []
for a, b in permutations(id_list, 2):
	if match_bool(a,b):
		solutions.append((a,b))

for a, b in solutions:
	place = match(a, b)
	print(a, b)
	print(a.pop(place))
	print("".join(a))
	print("NEXT\n \n")