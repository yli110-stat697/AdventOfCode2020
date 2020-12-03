import math

with open('input.txt') as f:
	lines = f.readlines()

def removeTail(ls, substr):
	new_ls = []
	for i in ls:
		i = i.strip(substr)
		new_ls.append(i)
	return new_ls

lines = removeTail(lines, '\n') #lines is now a list with each element being a string

factor = math.ceil(len(lines)/len(lines[0]) * 3) #this is the factor that should expand the matrix to the right
for i in range(len(lines)):
	lines[i] = lines[i]*factor


# right 3, down 1 slope
i = 0 #row index
j = 0 #column index
path = [] #list that collects the pathing of the slope
c = 0 #count of the trees on the path

while i < len(lines) - 1:
	i += 1
	j += 3
	path.append(lines[i][j])

	if lines[i][j] == '#':
		c = c + 1

print(c)
print(path.count('#'))


