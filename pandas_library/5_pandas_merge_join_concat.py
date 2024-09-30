import pandas as pd

df1 = pd.DataFrame(
    {
        'A': ['A0', 'A1', 'A2', 'A3'],
        'B': ['B0', 'B1', 'B2', 'B3'],
        'C': ['C0', 'C1', 'C2', 'C3'],
        'D': ['D0', 'D1', 'D2', 'D3'],
    },
    index=[0, 1, 2, 3],
)

df2 = pd.DataFrame(
    {
        'A': ['A4', 'A5', 'A6', 'A7'],
        'B': ['B4', 'B5', 'B6', 'B7'],
        'C': ['C4', 'C5', 'C6', 'C7'],
        'D': ['D4', 'D5', 'D6', 'D7'],
    },
    index=[4, 5, 6, 7],
)

df3 = pd.DataFrame(
    {
        'A': ['A8', 'A9', 'A10', 'A11'],
        'B': ['B8', 'B9', 'B10', 'B11'],
        'C': ['C8', 'C9', 'C10', 'C11'],
        'D': ['D8', 'D9', 'D10', 'D11'],
    },
    index=[8, 9, 10, 11],
)

# concat glues together DataFrames. Dimensions should match along the axis you are concatenating on
print('Concat:')
result1 = pd.concat([df1, df2, df3])
print(result1)

print('Concat, axis=1:')
result2 = pd.concat([df1, df2, df3], axis=1)
print(result2)

left = pd.DataFrame(
    {
        'key1': ['K0', 'K1', 'K2', 'K3'],
        'A': ['A0', 'A1', 'A2', 'A3'],
        'B': ['B0', 'B1', 'B2', 'B3'],
    }
)

right = pd.DataFrame(
    {
        'key2': ['K0', 'K1', 'K2', 'K3'],
        'C': ['C0', 'C1', 'C2', 'C3'],
        'D': ['D0', 'D1', 'D2', 'D3'],
    }
)

print('Merge, on = (key1, key2):')
result_merge1 = pd.merge(left, right, on=['key1', 'key2'])
print(result_merge1)

print('Merge, how=outer, on = (key1, key2):')
result_merge2 = pd.merge(left, right, how='outer', on=['key1', 'key2'])
print(result_merge2)

print('Merge, how=right, on = (key1, key2):')
result_merge3 = pd.merge(left, right, how='right', on=['key1', 'key2'])
print(result_merge3)

print('Merge, how=right, on = (key1, key2):')
result_merge4 = pd.merge(left, right, how='left', on=['key1', 'key2'])
print(result_merge4)

left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                    index=pd.Index(['K0', 'K1', 'K2']))

right = pd.DataFrame({'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']},
                     index=pd.Index(['K0', 'K1', 'K2']))

print('Join:')
result_join1 = left.join(right)
print(result_join1)

print('Join, outer:')
result_join2 = left.join(right, how='outer')
print(result_join2)
