"""
Solution for Day 6 Part 1
"""

from collections import defaultdict
from scipy.spatial.distance import cityblock
import numpy as np

data_fp = "data.txt"
coordinates = []
max_x = 500
max_y = 500
with open(data_fp, "r") as df:
	lines = df.readlines()
	for line in lines:
		x, y = line.split(",")
		x = int(x.strip())
		y = int(y.strip())
		coordinates.append([x,y])
		# find out area bounds
		if x >= max_x:
			max_x = x
		if y >= max_y:
			max_y = y

		# print (x,y)

print("Bounds of map are (%s, %s)" % (max_x, max_y))
print("There are %s area spots in this plot"%(max_x*max_y))
area_spots = max_x*max_y
counter = 1
# This is clearly a voronoi diagram esque question ie each point
# occupies a set of coordinates such that members of the set are
# closer to any other point (by manhattan distance in this case)
voronoi_sets = defaultdict(set)

# go through every point and assign it to the center points
for xit in range(max_x):
	for yit in range(max_y):
		if counter % 1000 == 0:
			print ("%s of %s" % (counter, area_spots))
		dists = []
		
		for coord in coordinates:
			dists.append(cityblock([xit,yit],coord))
		counter+=1

		if len(dists) != len(set(dists)):
			# there are duplicates so this point does not get attached to any group
			continue
		else:
			dists = np.array(dists)
			argmin_dists = dists.argmin()
			voronoi_sets[argmin_dists].add((xit, yit))

max_area = 0
for vset in voronoi_sets.keys():
	if len(voronoi_sets[vset]) > max_area:
		max_area = len(voronoi_sets[vset])
print("Maximum area is: %s"%(max_area))





