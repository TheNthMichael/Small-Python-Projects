import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import math

def get_cubic_coeff(x_val, y_val):
    A = np.array([
        [x_val[0]**3, x_val[0]**2, x_val[0], 1],
        [x_val[1]**3, x_val[1]**2, x_val[1], 1],
        [x_val[2]**3, x_val[2]**2, x_val[2], 1],
        [x_val[3]**3, x_val[3]**2, x_val[3], 1]
    ])
    b = np.array(y_val)
    z = np.linalg.solve(A,b)
    return z


""" x_val = [1,2,3,4]
y_val = [1,-2,1,6]


z = get_cubic_coeff(x_val, y_val)
x = np.array(range(100))
x = x / 10
y = z[0] * (x**3) + z[1] * (x*x) + z[2] * x + z[3] """



# data which the line will  
# contain (x, y) 
fig = plt.figure()
#creating a subplot 
ax1 = fig.add_subplot(1,1,1)


def animate(i):
    dx = 100 * math.cos(i / 30)
    dy = 100 * math.sin(i / 30)
    x_val = [1-dx, 10+dx, 3, 4]
    y_val = [5-dx/2, 5+dx, 100, 70-dx]




    z = get_cubic_coeff(x_val, y_val)
    x = np.array(range(int(min(x_val) * 10) - 30, int(max(x_val) * 10) + 30))
    #x = np.array(range(-1000, 1000))
    x = x / 10
    y = z[0] * (x**3) + z[1] * (x*x) + z[2] * x + z[3]
   
    
    ax1.clear()
    ax1.plot(x, y)

    for d in range(len(x_val)):
        ax1.plot(x_val[d], y_val[d], marker='o', markersize=3, color="red")

    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Live graph with matplotlib')	
	
    
ani = FuncAnimation(fig, animate, interval=1000/60) 
plt.show()

#plt.plot(x,y)





#plt.show()
