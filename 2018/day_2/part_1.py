# Solution Code for Day 2 part 1
from collections import Counter

data_file = "data.txt"
counter_list = []

with open(data_file, "r") as df:
	# read the files and make counter objects for all the box ids
	lines = df.readlines()
	for line in lines:
		box_id = line.strip()
		chars_counter = Counter(list(box_id))
		counter_list.append(chars_counter)
	
	# count the number of boxes with two identical letters, those with three identical letters,
	# and those with both
	two_chars = 0
	three_chars = 0
	for cc in counter_list:
		if 2 in cc.values():
			two_chars += 1
		if 3 in cc.values():
			three_chars += 1


print("The number of single two_chars: %s" % (two_chars))
print("The number of single three_chars: %s" % (three_chars))
print("Checksum two_chars*three_chars: %s" % (two_chars*three_chars))