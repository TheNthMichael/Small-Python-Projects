import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import math

class MatrixTo(object):
    def __init__(self, start=np.array([ [1, 0], [0, 1] ]), end = np.array([[1, 0], [1, 1]])):
        self.start = start
        self.end = end
        self.sign = (end - start) * 0.1
        self.points = []
        self.add_points()
        
    def add_points(self):
        for x in range(-10, 10):
            for y in range(-10, 10):
                self.points.append([x,y])


    def plot_step(self, i):
        if((self.start == self.end).all()):
            print('equal')
        else:
            self.start = self.start + self.sign

        ax1.clear()

        

        for point in self.points:
            a = point[0] * self.start[0][0] + point[1] * self.start[0][1]
            b = point[0] * self.start[1][0] + point[1] * self.start[1][1]
            ax1.plot(a, b, marker='o', markersize=3, color="red")

        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.title('Live graph with matplotlib')	
            



# data which the line will  
# contain (x, y) 
fig = plt.figure()
#creating a subplot 
ax1 = fig.add_subplot(1,1,1)

using = MatrixTo()
	
    
ani = FuncAnimation(fig, using.plot_step, interval=1000/30) 
plt.show()