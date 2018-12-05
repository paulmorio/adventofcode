"""
Solution for day 5 part 1
"""


data_fp = "data.txt"
import math
with open(data_fp, "r") as df:
	polymer = df.readlines()
	polymer = polymer[0].strip()

change_was_made = True
polymer = list(polymer) # to allow popping
while change_was_made:
	change_was_made = False
	indices = []
	print("Length of polymer remaining: %s" % (len(polymer)))
	i = 0
	while i in range(len(polymer)-1):
		if polymer[i].islower() and polymer[i+1].isupper():			
			if polymer[i] == polymer[i+1].lower():
				indices.append(i)
				indices.append(i+1)
				i += 2
				change_was_made = True
			else:
				i += 1
		elif polymer[i].isupper() and polymer[i+1].islower():
			# print("Oi")
			if polymer[i] == polymer[i+1].upper():
				indices.append(i)
				indices.append(i+1)
				i += 2
				change_was_made = True
			else:
				i += 1
		else:
			# print("nig")
			i += 1

	for j in sorted(indices, reverse=True):
		polymer.pop(j)

print("Answer")
print("".join(polymer))
print(len(polymer))


