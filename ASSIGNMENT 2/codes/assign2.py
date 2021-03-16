import numpy as np  
import matplotlib.pyplot as plt  
  
# data to be plotted 
x = np.arange(0,2)  
y =2*x 
  
# plotting 
plt.ylabel("f(x)")  
plt.xlabel("x")  
plt.title("probability density function")
plt.plot(x, y, color ="blue")  
plt.show()
