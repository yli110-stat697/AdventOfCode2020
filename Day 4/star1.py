with open("input.txt") as f:
	passports = f.read()

passportsList = passports.split('\n\n')

def replaceSub(ls, substr):
    new_ls = []
    for item in ls:
        item = item.replace(substr, ' ')
        new_ls.append(item)
    return new_ls

passportsList = replaceSub(passportsList, '\n')

def ConvertListToDict(ls):
    it = iter(ls)
    res_dct = dict(zip(it, it))
    return res_dct

passportsDict = []
for item in passportsList:
    item = item.replace(':', ' ').split(' ')
    item = ConvertListToDict(item)
    passportsDict.append(item)

valid_count = 0
for person in passportsDict:
    if (len(person.keys())== 8) | (('cid' not in person.keys()) & (len(person.keys())==7)):
        valid_count = valid_count + 1

print("The valid count of passports is {}".format(valid_count))