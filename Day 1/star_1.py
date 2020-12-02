from itertools import combinations
import numpy as np

# read in input -- expense report
lines = []
with open('input.txt') as f:
	lines = f.readlines()

# remove the tailing '\n'
def removeTail(ls, sub):
	new_ls = []
	for i in ls:
		i = i.strip(sub)
		new_ls.append(i)
	return new_ls

lines = removeTail(lines, '\n')

# convert string to numbers
num_lines = [int(i) for i in lines]

# find the correct combination that sum == 2020, and multiply them
for i in combinations(num_lines, r=2):
	if sum(i) == 2020:
		print(i)
		print(np.prod(i))