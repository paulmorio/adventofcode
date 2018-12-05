"""
Solution for day 5 part 1
"""


data_fp = "data.txt"
import math
with open(data_fp, "r") as df:
	polymer_og = df.readlines()
	polymer_og = polymer_og[0].strip()

# copy
alphabet = "abcdefghijklmnopqrstuvwxyz"

polymer_lens = []
for letter in list(alphabet):
	print("Removing: %s" %(letter))
	polymer = list(polymer_og)
	polymer[:] = [x for x in polymer if x != letter]
	polymer[:] = [x for x in polymer if x != letter.upper()]

	change_was_made = True
	while change_was_made:
		change_was_made = False
		indices = []
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

	polymer_lens.append(len(polymer))

print("Minimal Polymer Length is: %s" % (min(polymer_lens)))



