import numpy as np
import scipy 
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

X = np.linspace(0,1,10001)
probability = [ ]
for i in range(10001): 
  probability.append(2*X[i]/10001)
count=0
for i in range(10001):
  Random_variable = np.random.choice(X, p = probability)
  if Random_variable<0.5:
        count +=1
print("simulated probability P(X<0.5) is : ",count/10001)
print("Theoritical probability P(X<0.5) is : 0.25")
