import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
plt.style.use('seaborn-pastel')

# we simply create a figure window with a single axis in the figure. 
# Then we create our empty line object which is essentially the one to be modified in the animation. 
# The line object will be populated with data later.

fig = plt.figure()
ax = plt.axes(xlim=(0, 8), ylim=(-3, 3))
line, = ax.plot([], [], lw=3)

# we create the init function that will make the animation happen. 
# The init function initializes the data and also sets the axis limits.
def init():
    line.set_data([], [])
    return line,

# define the animation function which takes in the frame number(i) as the parameter and creates a sine wave(or any other animation) which a shift depending upon the value of i. 
# This function here returns a tuple of the plot objects which have been modified which tells the animation framework what parts of the plot should be animated.
def animate(i):
    x = np.linspace(0, 8, 1000)
    y = np.sin(4 * np.pi * (x - 0.01 * i))
    line.set_data(x, y)
    return line,

anim = FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=50, blit=False)


plt.show()