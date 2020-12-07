with open('input.txt') as f:
	stringL = f.read()


groupList = stringL.split('\n\n').copy()
groupPersonList = []
for group in groupList:
	person = group.split('\n')
	groupPersonList.append(person)

groupPersonList_num = []
for group in groupPersonList:
	i = 0
	commonSet = set(group[i])
	while i < len(group) - 1:
		commonSet = commonSet & set(group[i+1])
		i += 1
	groupPersonList_num.append(len(commonSet))

print(sum(groupPersonList_num))