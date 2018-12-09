"""
Solution Code for Day 7 Part 2
"""

from collections import defaultdict

num_workers = 4
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
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
workers = defaultdict(lambda: defaultdict(int))
timer = 0
# Go through each step and open up new opportunities, resolving conflicts
# alphabetically

while task_order:
	for i in range(num_workers):
		if workers[i][1] <= 0 and workers[i][0] not in order_of_steps:
			step = task_order.pop(0)
			workers[i][0] = step
			workers[i][1] += 60 + (alphabet.index(step) + 1)
			order_of_steps.append(workers[i][0])

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

			if task_order:
				task_order = (list(set(task_order)))
				task_order.sort()

		elif workers[i][1] <= 0 and workers[i][0] in order_of_steps:
			step = task_order.pop(0)
			workers[i][0] = step
			workers[i][1] += 60 + (alphabet.index(step) + 1)
			order_of_steps.append(workers[i][0])

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

			if task_order:
				task_order = (list(set(task_order)))
				task_order.sort()



		elif workers[i][1] > 0:
			workers[i][1] -= 1

	timer += 1

# add remaning time
timer += max([workers[x][1] for x in workers.keys()])
print(timer)