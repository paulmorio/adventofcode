# Solution Code for Day 1
data_file = "data.txt"
final_frequency = 0
with open(data_file, "r") as df:
	for line in df:
		num = line.strip()
		if num[0] == "+":
			final_frequency += int(num[1:])
		if num[0] == "-":
			final_frequency -= int(num[1:])

print (final_frequency)