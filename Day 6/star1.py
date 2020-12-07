with open('input.txt') as f:
	stringL = f.read()


groupList = stringL.split('\n\n').copy()

def replaceSub(ls, substr):
    new_ls = []
    for item in ls:
        item = item.replace(substr, '')
        new_ls.append(item)
    return new_ls

groupList = replaceSub(groupList, '\n')


groupList_num = []
for group in groupList:
    groupList_num.append(len(set(group)))

print(sum(groupList_num))