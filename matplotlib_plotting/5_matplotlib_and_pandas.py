import matplotlib.pyplot as plt
import pandas as pd

pd.set_option('display.max_columns', 15)
heart_disease = pd.read_csv('heart-disease.csv')

heart_disease['age'].plot.hist(bins=50)  # plot for raw

heart_disease.plot.hist(subplots=True, figsize=(10, 30))  # plot for all data

# plt.show()

''' pyplot vs matplotlib OO method?
 * When plotting something quickly, okay to use the pyplot method
 * When plotting something more advanced, use the 00 method
'''

'''Plot method'''
over_50 = heart_disease[heart_disease['age'] > 50]
print(over_50.head())
over_50.plot(kind='scatter', x='age', y='chol', c='target')

'''matplotlib OO method with plot method'''
fig, ax = plt.subplots(figsize=(10, 6))
over_50.plot(kind='scatter', x='age', y='chol', c='target', ax=ax)
# ax.set_xlim([45, 100]) # set limits

'''matplotlib OO method from scratch'''
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the data
scatter = ax.scatter(x=over_50['age'], y=over_50['chol'], c=over_50['target'])

# Customize the plot
ax.set(title='Heart Disease and Cholesterol Levels', xlabel='Age', ylabel='Cholesterol')

# Add a legend
ax.legend(*scatter.legend_elements(), title='Target')

# Add horizontal line
ax.axhline(over_50['chol'].mean(), linestyle='--')

'''matplotlib OO method from scratch - Subplot of chol, age, thalach'''
fig, (ax0, ax1) = plt.subplots(nrows=2, ncols=1, figsize=(10, 10), sharex=True)

# Add data, meanline, legend and customize ax0
scatter = ax0.scatter(x=over_50['age'], y=over_50['chol'], c=over_50['target'])
ax0.set(title='Heart Disease and Cholesterol Levels', ylabel='Cholesterol')
ax0.legend(*scatter.legend_elements(), title='Target')
ax0.axhline(over_50['chol'].mean(), linestyle='--')

# Add data, a meanline, a legend and customize ax1
scatter = ax1.scatter(x=over_50['age'], y=over_50['thalach'], c=over_50['target'], cmap='summer')
ax1.set(title='Heart Disease and Max Heart Levels', xlabel='Age', ylabel='Max Heart Levels')
ax1.legend(*scatter.legend_elements(), title='Target')
ax1.axhline(over_50['thalach'].mean(), linestyle='--')

#Add a title to the figure
fig.suptitle('Heart Disease Analysis', fontsize=15, fontweight='bold')

plt.show()

