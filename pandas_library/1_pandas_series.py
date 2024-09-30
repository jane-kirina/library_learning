import numpy as np
import pandas as pd

label = ['a', 'b', 'c']
data = [10, 20, 30]
arr = np.array(data)
d = dict(map(lambda i, j: (i, j), label, data))

print(pd.Series(data=data))
print(pd.Series(data=data, index=label))
print(pd.Series(data, label))
print(pd.Series(arr, label))
print(pd.Series(d))
print(pd.Series(data=[sum, print, len]))

ser1 = pd.Series([1, 2, 3, 4], ['USA', 'Germany', 'USSR', 'Japan'])
print(ser1)

ser2 = pd.Series([1, 2, 5, 4], ['USA', 'Germany', 'Italy', 'Japan'])
print(ser2)

ser3 = pd.Series(data=label)
print(ser1 + ser2)
