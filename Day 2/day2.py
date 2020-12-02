import pandas as pd 

df = pd.read_csv('input.txt', sep = ' ', header = None, names = ('freq', 'letter', 'password'))

# data cleansing
df['letter'] = df['letter'].str.replace(':', '')
df['min'] = df['freq'].astype('str').str.split('-').str.get(0)
df['max'] = df['freq'].astype('str').str.split('-').str.get(1)
df['min'] = df['min'].astype(str).astype(int)
df['max'] = df['max'].astype(str).astype(int)
df['password'] = df['password'].astype(str)
df['letter'] = df['letter'].astype(str)

# the variable num represents the number of letter occurrence in password
df['num'] = df.apply(lambda x: x['password'].count(x['letter']), axis=1)

# star 1
print(df[(df['min'] <= df['num'] ) & (df['num'] <= df['max'])].shape[0])

# min_letter and max_letter represents the letter at specified positions in the rule
df['min_letter'] = df.apply(lambda x: x['password'][x['min'] - 1], axis=1)
df['max_letter'] = df.apply(lambda x: x['password'][x['max'] - 1], axis=1)

# star 2
print(df[(df['min_letter'] == df['letter']) ^ (df['max_letter'] == df['letter']) ].shape[0])