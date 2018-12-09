"""
Solution Code for Day 7 Part 1
# aka the topological sort
"""

from collections import defaultdict
data_fp = "data.txt"
step_requirements = defaultdict(list)
task_order = []
with open(data_fp, "r") as df:
	lines = df.readlines()
	for line in lines:
		_, requirement, _, _, _, _, _, step, _, _ = line.split()
		step_requirements[step].append(requirement)

	for line in lines:
		_, requirement, _, _, _, _, _, step, _, _ = line.split()
		if requirement not in step_requirements:
			task_order.append(requirement)

	# line up the first steps and append as necessary starting now
	task_order = (list(set(task_order)))
	task_order.sort()

order_of_steps = []

# Go through each step and open up new opportunities, resolving conflicts
# alphabetically
while task_order:
	step = task_order.pop(0)
	order_of_steps.append(step)

	# Say we've done the step so remove requirement on remaining steps
	for el in step_requirements.keys():
		if step in step_requirements[el]:
			step_requirements[el].remove(step)
	
	# Add new steps to the task order that can now be done
	# cause they no longer have requirements.
	for el in list(step_requirements.keys()):
		if not step_requirements[el]:
			task_order.append(el)
			del step_requirements[el]

	print (task_order)
	if task_order:
		task_order = (list(set(task_order)))
		task_order.sort()


print("".join(order_of_steps))

