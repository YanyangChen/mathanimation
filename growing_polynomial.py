import matplotlib.pyplot as plt 
import matplotlib.animation as animation 
import numpy as np 
plt.style.use('dark_background')
# https://pythonmatplotlibtips.blogspot.com/2018/01/combine-3d-two-2d-animations-in-one-figure-artistdanimation.html
fig = plt.figure() 
ax = plt.axes(xlim=(-8, 10), ylim=(0, 68)) 
line, = ax.plot([], [], lw=2) 

# initialization function 
def init(): 
	# creating an empty plot/frame 
	line.set_data([], []) 
	return line, 

# lists to store x and y axis points 
xdata, ydata = [], [] 

# animation function 
def animate(i): 
	# t is a parameter 
	t = 0.1*i 
	
	# x, y values to be plotted 
	x = t-8 
	y = x**2
	
	# appending new points to x, y axes points list 
	xdata.append(x) 
	ydata.append(y) 
	line.set_data(xdata, ydata) 
	return line, 
	
# setting a title for the plot 
plt.title('Creating a growing coil with matplotlib!') 
# hiding the axis details 
plt.axis('off') 

# call the animator	 
anim = animation.FuncAnimation(fig, animate, init_func=init, 
							frames=160, interval=20, blit=False) 

# save the animation as mp4 video file 
# anim.save('coil.gif',writer='imagemagick') 
plt.show()