# Solution Code for Day 1 part 2
from collections import Counter

data_file = "data.txt"
final_frequency = 0
frequencies_visited = []
duplicate_found = False
iterations_run = 0
while duplicate_found == False:
	print("Current iterations_run: %s" % (iterations_run))
	print ("Current Length of Frequencies: %s" % (len(frequencies_visited)))
	with open(data_file, "r") as df:
		for line in df:
			num = line.strip()
			if num[0] == "+":
				final_frequency += int(num[1:])
			if num[0] == "-":
				final_frequency -= int(num[1:])

			# check for the first duplicate in growing list
			if final_frequency in frequencies_visited:
				print (final_frequency)
				duplicate_found = True
			else:
				frequencies_visited.append(final_frequency)
	iterations_run += 1