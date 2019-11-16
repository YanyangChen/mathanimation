import matplotlib.pyplot as plt 
import matplotlib.animation as animation 
from scipy.integrate import odeint
import numpy as np 


fig = plt.figure() 
# ax = plt.axes(xlim=(0, 500), ylim=(-3, 4)) 
ax = plt.axes(xlim=(-4, 5), ylim=(-3, 4)) 
line, = ax.plot([], [], lw=2) 

mu = 0.2

def van_der_pol_oscillator_deriv(x, t):
    nx0 = x[1]
    nx1 = -mu * (x[0] ** 2.0 - 1.0) * x[1] - x[0]
    res = np.array([nx0, nx1])
    return res

ts = np.linspace(0.0, 50.0, 500)

# xs = odeint(van_der_pol_oscillator_deriv, [0.2, 0.2], ts)
# xs = odeint(van_der_pol_oscillator_deriv, [4.0, 4.0], ts)
# plt.plot(xs[:,0], xs[:,1])
xs = odeint(van_der_pol_oscillator_deriv, [-3.0, -3.0], ts)
# plt.plot(xs[:,0], xs[:,1])

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
	t = i 
	# xs = odeint(van_der_pol_oscillator_deriv, [-3.0, -3.0], t)
	# x, y values to be plotted 
	x = xs[t,0]
	y = xs[t,1]
	
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
							frames=500, interval=20, blit=True) 

# save the animation as mp4 video file 
#anim.save('coil.html',writer='ffmpeg') 
plt.show()