import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 2, 100)
y = np.linspace(0, 2, 100)
# axes = plt.gca()
# axes.set_xlim([0, 100])
# axes.set_ylim([0, 100])
plt.plot(x, x, label='linear')
plt.plot(x, x**2, label='quadratic')
plt.plot(x, x**3, label='cubic')
plt.plot(x, x**3 + 2*x**2 + 3*x, label='cubic2')

plt.xlabel('x label')
plt.ylabel('y label')

plt.title("Simple Plot")

plt.legend()

plt.show()