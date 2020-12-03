import math
import numpy as np

with open("input.txt") as f:
    lines = f.readlines()

def removeTail(ls, sub):
    new_ls = []
    for i in ls:
        i = i.strip(sub)
        new_ls.append(i)
    return new_ls

lines = removeTail(lines, '\n')

factor = math.ceil(len(lines)/len(lines[0]) * 7) # max right step is 7

for i in range(len(lines)):
    lines[i] = lines[i] * factor

def CountPathTrees(right, down):
	i=0
	j=0
	path = []
	c=0

	while i < len(lines) - 1:
		i += down
		j += right
		path.append(lines[i][j])

		if lines[i][j] == '#':
			c = c + 1
	assert c == path.count('#'), "Count and the path count don't match"
	return c

treeNum = []
for i in range(1,8,2): # right 1, 3, 5, 7
	treeNum.append(CountPathTrees(i, 1))
treeNum.append(CountPathTrees(1,2))

print(np.prod(treeNum))