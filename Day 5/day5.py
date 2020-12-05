import math

with open('input.txt') as f:
    lines = f.readlines()
def replaceSub(ls, substr):
    new_ls = []
    for item in ls:
        item = item.strip(substr)
        new_ls.append(item)
    return new_ls
lines = replaceSub(lines, '\n')

rows = []
for line in lines:
    rows.append(line[:7])

columns = []
for line in lines:
    columns.append(line[-3:])

row_numbers = []
for row in rows:
    start = 0
    stop = 127
    for direction in row:
        if direction == 'F':
            stop = math.floor((start + stop)/2)
        elif direction == 'B':
            start = math.ceil((start + stop)/2)
    row_numbers.append(start)

column_numbers = []
for column in columns:
    start = 0
    stop = 7
    for direction in column:
        if direction == 'R':
            start = math.ceil((start + stop)/2)
        elif direction == 'L':
            stop = math.floor((start + stop)/2)
    column_numbers.append(start)

seatIDs = []
for i in range(len(lines)):
    seatID = row_numbers[i] * 8 + column_numbers[i]
    seatIDs.append(seatID)

print("The max ID is {}".format(max(seatIDs)))
print("The min ID is {}".format(min(seatIDs)))

print("The missing boarding pass is {}".format(set(range(min(seatIDs), max(seatIDs))) - set(seatIDs)))