import numpy as np
import pandas as pd

d = {'A': [1, 2, np.nan], 'B': [5, np.nan, np.nan], 'C': [1, 2, 3]}
df = pd.DataFrame(d)

print(df.dropna(axis=1))
print(df.dropna(thresh=2))
print(df.fillna(value='nothing'))
print(df['A'].fillna(value=df['A'].mean()))
