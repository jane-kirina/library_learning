import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('../matplotlib_plotting/car-sales.csv')
plt.figure(figsize=(10, 5))

sns.rugplot(x='Price', data=df, height=0.5)

# DEPRECATED distplot, use displot or histplot
# seaborn.displot is a figure-level plot, which does not work with figsize=(12,8)
sns.set(style='whitegrid')
sns.displot(data=df, x='Price', aspect=2, bins=20, color='green', edgecolor='black', linewidth=2)
plt.show()

sns.set(style='darkgrid')
fig, ax = plt.subplots(figsize=(9, 5))
sns.histplot(data=df, x='Price')
plt.show()

sns.kdeplot(data=df, x='Doors')
plt.show()

np.random.seed(100)
sample = np.random.randint(0, 100, 200)
sample = pd.DataFrame(sample, columns=['data'])
sns.rugplot(data=sample, x='data', height=0.4)
plt.show()
