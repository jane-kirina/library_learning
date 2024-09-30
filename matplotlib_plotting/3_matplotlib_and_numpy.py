import matplotlib.pyplot as plt
import numpy as np

## create data
x = np.linspace(0, 10, 100)

'''1 - Line plot x^2'''
fig, ax = plt.subplots(figsize=(6, 6))
ax.plot(x, x ** 2)
ax.set(title='1. Line plot')

'''2 Scatter plot exponential'''
fig, ax = plt.subplots()
ax.scatter(x, np.exp(x))  # scatter -> lots of dots on the plot
ax.set(title='2. Scatter plot -> exponential')

'''3 Scatter plot sin'''
fig, ax = plt.subplots()
ax.scatter(x, np.sin(x))
ax.set(title='3. Scatter plot -> trigonometric sine')

'''4 Plot from dictionary - bar'''
dic = {"1-data": 20,
       "2-data": 4,
       "3-data": 14
       }
fig, ax = plt.subplots()
ax.bar(dic.keys(), dic.values())
ax.set(title='4. Bar plot -> dictionary')

'''5 Plot from dictionary - histogram 1'''
fig, ax = plt.subplots()
ax.barh(list(dic.keys()), list(dic.values()))
ax.set(title='5. Histogram 1 -> dictionary')

'''6 Plot from dictionary - histogram 2'''
x = np.random.randn(1000)
fig, ax = plt.subplots()
ax.hist(x)  # hist - short for histogram
ax.set(title='6. Histogram 2 -> dictionary')

'''7 1st subplots'''
fig, ((ax0, ax1), (ax2, ax3)) = plt.subplots(nrows=2, ncols=2, figsize=(10, 8))

## plot every axis
ax0.set(title='7.1 Subplots')
ax1.set(title='7.2 Subplots')
ax2.set(title='7.3 Subplots')
ax3.set(title='7.4 Subplots')

ax0.plot(x, x / 2)
ax1.scatter(np.random.random(10), np.random.random(10))
ax2.bar(dic.keys(), dic.values())
ax3.hist(x)

'''8 2st subplots'''
fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(10, 7))

## plot every index
ax[0, 0].set(title='8.1 Subplots')
ax[0, 1].set(title='8.2 Subplots')
ax[1, 0].set(title='8.3 Subplots')
ax[1, 1].set(title='8.4 Subplots')

ax[0, 0].plot(x, x / 2)
ax[0, 1].scatter(np.random.random(10), np.random.random(10))
ax[1, 0].bar(dic.keys(), dic.values())
ax[1, 1].hist(x)

plt.show()
