import numpy as np
import pandas as pd
from numpy.random import randn as r

np.random.seed(101)

df = pd.DataFrame(r(5, 4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])
print(df)
print(df['W'])

# print(df.W) # not recommended

# d['qwer'] # error

df['qwer'] = df['W'] + df['Y']

print(df)

df.drop('qwer', axis=1, inplace=True)
df.drop('E', axis=0)

print(df)
# loc refers to index
# iloc refers to position
print(df.loc['A'])

print(df.loc['B', 'Y'])

print(df.loc[['A', 'B'], ['W', 'Y']])

bool_df = df > 0

data_bool_W = df['W'] > 0

print(data_bool_W)

print(df[df['Z'] < 0])

result_df = df[df['W'] > 0]

result_df_x = result_df['X']
print(result_df_x)

result_full = df[df['W'] > 0][['Y', 'X']]
print(result_full)

# result_with_error = df[(df['W'] > 0) and (df['Y'] > 1)]  ## Series is ambiguous
result_without_error = df[(df['W'] > 0) | (df['Y'] > 1)]

print(df.reset_index())
print(df.reset_index(inplace=True))

newind = 'CA NY WY OR CO'.split()
df['States'] = newind
print(df)
df.set_index('States', inplace=True)
print(df)

# Index Levels
outside = 'G1 G1 G1 G2 G2 G2'.split()
inside = [1, 2, 3, 1, 2, 3]
hier_index = list(zip(outside, inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)
print(outside)
print(inside)
print(hier_index)

df = pd.DataFrame(r(6, 2), hier_index, ['A', 'B'])
print(df)
print(df.loc['G1'])

df.index.names = ['Groups', 'Num']
print(df)

group2_num2_B = df.loc['G2'].loc[2]['B']
print(group2_num2_B)

group1_num3_A = df.loc['G1'].loc[3]['A']
print(group1_num3_A)

print(df.xs(1, level='Num'))
