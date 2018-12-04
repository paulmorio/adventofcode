"""
Solution for Day 4 Part 1
"""
from datetime import datetime
from collections import defaultdict, Counter

data_file_path = "data.txt"

# Open file, read data and clean
with open(data_file_path, "r") as df:
	lines = df.readlines()

	markings = []
	for line in lines:
		date, event = line.split("]")
		
		# Date and time cleaning
		date = date[1:].strip()
		dated, time = date.split()
		year, month, day = (map(int, dated.split("-")))
		datetime_object = datetime.strptime(date, '%Y-%m-%d %H:%M')
		
		# Event cleaning
		event = event.strip()

		# Add to markings list to sort
		markings.append((datetime_object,event))

	# sort by datetime
	markings.sort(key = lambda x: x[0])

	for i in markings[:30]:
		print (i)
# For each guard establish counts of when they sleep 
guard_sleepy_minutes = defaultdict(list)

current_guard = -1
time_start = 0
for dt, event in markings:
	# Guard change events
	if event[0] == "G":
		_, gid, _, _ = event.split()
		gid = int(gid[1:].strip())
		current_guard = gid
		print(current_guard)
		if dt.hour == 00:
			time_start = dt.minute
		else:
			time_start = 0

	# fall asleep event
	if event[0] == "f":
		time_start = dt.minute

	if event[0] == "w":
		for i in range(time_start, dt.minute):
			guard_sleepy_minutes[current_guard].append(i)

# guard that sleeps the most
current_max_sleeper = -1
most_slept = 0
for gid in guard_sleepy_minutes.keys():
	if len(guard_sleepy_minutes[gid]) > most_slept:
		current_max_sleeper = gid
		most_slept = len(guard_sleepy_minutes[gid])
print("Guard that sleeps the most: %s with %s minutes" % (current_max_sleeper, most_slept))

# Find the guard and minute slept most
minute_slept_most = -1
how_often_minute = -1
guard_sleeping_that_minute = -1
for gid in guard_sleepy_minutes.keys():
	minCounter = Counter(guard_sleepy_minutes[gid])
	if (minCounter.most_common()[0][1] > how_often_minute):
		guard_sleeping_that_minute = gid
		minute_slept_most = minCounter.most_common()[0][0]
		how_often_minute = minCounter.most_common()[0][1]

print("Minute Slept most: %s, %s times by guard %s, checksum: %s" % (minute_slept_most, how_often_minute, 
	guard_sleeping_that_minute, guard_sleeping_that_minute*minute_slept_most))


