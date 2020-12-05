import re

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

valid_passports = []
for person in passportsDict:
    if (len(person.keys())== 8) | (('cid' not in person.keys()) & (len(person.keys())==7)):
        valid_passports.append(person)

ecl_list = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] #define the ecl list

# modify valid_passports to have the correct form
for person in valid_passports:
    person['byr'] = int(person['byr'])
    person['iyr'] = int(person['iyr'])
    person['eyr'] = int(person['eyr'])
    person['hgt'] = [person['hgt'][-2:], int(re.findall(r'\d*\d', person['hgt'])[0])]
    person['hcl'] = [person['hcl'][0], person['hcl'][1:]]

# start to count the valid values
valid_value_count = 0
valid_value_passports = []

for person in valid_passports:
    if 1920 <= person['byr'] <= 2002:
        if 2010 <= person['iyr'] <= 2020:
            if 2020 <= person['eyr'] <= 2030:
                if ((person['hgt'][0] == 'cm')& (150 <= person['hgt'][1] <= 193)) or ((person['hgt'][0] == 'in') & (59 <= person['hgt'][1] <= 76)):
                        if (person['hcl'][0] == '#') & bool(re.match(r'[a-z0-9][a-z0-9][a-z0-9][a-z0-9][a-z0-9][a-z0-9]', person['hcl'][1])):
                            if person['ecl'] in ecl_list:
                                if (len(person['pid'])==9)  & bool(re.match(r'\d\d\d\d\d\d\d\d\d', person['pid'])):
                                    valid_value_count = valid_value_count + 1
                                    valid_value_passports.append(person)

assert (valid_value_count == len(valid_value_passports)), "results don't match"
print(valid_value_count)