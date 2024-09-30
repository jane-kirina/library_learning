# 0 - import matplotlib
import matplotlib.pyplot as plt

# 1 - prep data
x = [1, 2, 3, 4]
y = [10, 20, 30, 40]
# 2 - setup plot
fig, ax = plt.subplots(figsize=(8, 8))
# 3 - plot data
ax.plot(x, y)
# 4 - customize plot
ax.set(title='Example of Workflow', xlabel='x-axis', ylabel='y-axis')
# 5 - save & show the figure
fig.savefig('matplotlib-workflow.png')
plt.show()
