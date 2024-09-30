import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4, 4])
plt.show()

x = [1, 2, 3, 4]
y = [11, 22, 33, 44]
plt.plot(x, y)
plt.show()

'''Styles of plotting // plt.plot()'''
## 1st method
fig = plt.figure()  # create a figure
ax = fig.add_subplot()  # adds some axes
plt.show()

## 2nd method
fig = plt.figure()  # create a figure
ax = fig.add_axes([1, 1, 1, 1])  # adds sample data
ax.plot(x, y)  # add some data
plt.show()

## 3rd method (recommended)
fig, ax = plt.subplots()  # subplot - more than one plot come out at the same time
ax.plot(x, [50, 100, 200, 250])  # add some data
plt.show()
## everytime when we call smth like fig, ax = plt.subplots() -> it's going to reset the figure
