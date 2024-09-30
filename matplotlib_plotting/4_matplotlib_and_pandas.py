import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

car_sales = pd.read_csv('car-sales.csv')

car_sales["Price"] = car_sales["Price"].str.replace('$', '').str.replace('.', '').str.replace(',', '')
# car_sales["Price"] = car_sales["Price"].str.replace('[\$\,\.]', '')
car_sales["Price"] = car_sales["Price"].str[:-2]

car_sales["Sale Date"] = pd.date_range('1/1/2020', periods=len(car_sales))

car_sales["Total Sales"] = car_sales["Price"].astype(int).cumsum()

# plot data
car_sales.plot(x='Sale Date', y='Total Sales')

car_sales["Price"] = car_sales["Price"].astype(int)
car_sales.plot(x='Odometer (KM)', y='Price', kind='scatter')

print(car_sales)

'''Graph'''
x = np.random.rand(10, 4)
df = pd.DataFrame(x, columns=['a', 'b', 'c', 'd'])
df.plot.bar() # or df.plot(kind='bar')

car_sales.plot(x='Make', y='Odometer (KM)', kind='bar')
car_sales['Odometer (KM)'].plot.hist(bins=20)

print(df)
plt.show()
