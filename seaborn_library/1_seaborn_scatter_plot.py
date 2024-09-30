import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('../matplotlib_plotting/car-sales.csv')
plt.figure(figsize=(10, 5))

# Params:
# hue -> Column,
# palette -> colormap,
# size -> of the points,
# alpha -> transparency(from 0 to 1),
# style -> change style of dots
sns.scatterplot(x='Price', y='Make', data=df, hue='Colour', style='Colour', alpha=0.5, s=100,
                palette='inferno')  # hue -> Column, palette -> colormap, size -> of the points, alpha -> transparency(from 0 to 1), style -> change style of dots
plt.show()

# size of the points based on column
sns.scatterplot(x='Price', y='Make', data=df, size='Colour')
plt.show()
