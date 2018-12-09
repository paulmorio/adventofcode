"""
Solution for Day 8 part 2
"""
from anytree import Node, RenderTree

data_fp = "data.txt"
with open(data_fp, "r") as df:
	data = list(map(int, df.readlines().pop().split()))
	i = 0

def read_int():
	global i
	global data
	i += 1
	return data[i-1]

def read_tree():
	num_children, num_meta = read_int(), read_int()
	children = []
	meta_data = []
	for _ in range(num_children):
		children.append(read_tree())
	for _ in range(num_meta):
		meta_data.append(read_int())
	return((children, meta_data))

def sum_meta_data(children, meta_data):
	ans = 0
	for m in meta_data:
		ans+=m
	for c,m in children:
		ans+=sum_meta_data(c, m)
	return ans

def value(a):
	children, meta_data = a
	if not children:
		return (sum(meta_data))
	else:
		ans = 0
		for m in meta_data:
			if 1 <= m <= len(children):
				ans+=value(children[m-1])
		return ans

a = read_tree()
children,dmeta_data = a
print(sum_meta_data(children, dmeta_data))
print(value(a))
