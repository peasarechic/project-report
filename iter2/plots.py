import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-6, 6, 10000)

y = abs((x**3-3*x+5)**(0.5))
z = -y

fig = plt.figure()

# setting the axes at the centre
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# plot the function
plt.plot(x,y, 'r')
plt.plot(x,z, 'r')
# show the plot
plt.show()
