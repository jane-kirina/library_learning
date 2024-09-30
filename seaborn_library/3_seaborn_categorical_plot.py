import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

'''
The two main types of plots for this are: 
    countplot() -> Counts number of rows per category
    barplot() -> General form of displaying any chosen metric per category
'''

df = pd.read_csv('../matplotlib_plotting/car-sales.csv')

plt.figure(figsize=(10, 5), dpi=90)
# plt.ylim(2, 10)
sns.countplot(data=df, x='Colour', hue='Make')

plt.figure(figsize=(10, 5), dpi=90)
sns.barplot(data=df, x='Colour', hue='Make')
plt.show()

# df.plot(x='Odometer (KM)', y='Price', kind='scatter')

# tips = sns.load_dataset('tips')
# print(sns.displot(tips['total_bill']))
#
# sns.jointplot(x='total_bill', y='tip', data=tips)
