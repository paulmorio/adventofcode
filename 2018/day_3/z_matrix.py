import numpy as np

z_matrix = []
for x in arange(0,1,0.05):
	z_row = [] # for that series of x values
	for y in arange(0,2,0.05):
		z_row.append(z_function(x,y))

	# then append that row to the z matrix so that its a list of rows (which is a matrix in matlab/numpy)
	z_matrix.append(z_row)