import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

'''Customizing car sales'''
print(plt.style.available)
plt.style.use('seaborn-v0_8-whitegrid')

# Get ready data
car_sales = pd.read_csv('car-sales.csv')
car_sales["Price"] = car_sales["Price"].str.replace('$', '').str.replace('.', '').str.replace(',', '')
car_sales["Price"] = car_sales["Price"].str[:-2]
car_sales["Sale Date"] = pd.date_range('1/1/2020', periods=len(car_sales))
car_sales["Total Sales"] = car_sales["Price"].astype(int).cumsum()
car_sales["Price"] = car_sales["Price"].astype(int)

# Plot
car_sales.plot(x='Odometer (KM)', y='Price', kind='scatter')

print(car_sales)

'''Customizing dump data'''
x = np.random.randn(10, 4)
df = pd.DataFrame(x, columns=['a', 'b', 'c', 'd'])

plt.style.use('ggplot')
ax = df.plot(kind='bar', cmap='spring')
ax.set(title='Some data Bar Graph', xlabel='Row number', ylabel='Random number')
ax.legend().set_visible(True)
plt.show()
