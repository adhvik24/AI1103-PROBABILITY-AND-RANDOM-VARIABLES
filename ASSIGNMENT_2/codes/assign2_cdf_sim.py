import numpy as np
from scipy.stats import uniform
from matplotlib import pyplot as plt

#if using termux
import subprocess
import shlex
#end if  
def ecdf(a):
    x, counts = np.unique(a, return_counts=True)
    cusum = np.cumsum(counts)
    return x, cusum / cusum[-1]

U = uniform.rvs(size=100)
V= U**0.5
x, y = ecdf(V)
x = np.insert(x, 0, x[0])
y = np.insert(y, 0, 0.)
plt.plot(x, y,'o',label='Simulation')
plt.grid(True)
x=np.linspace(0,1)
plt.plot(x,x**2,label='Analysis')
plt.title("CDF of random variable $X$")
plt.xlabel("$x$")
plt.ylabel("$F_X(x)$")
plt.legend(loc='best')


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
print("Simulated probability is nearly same as theoritical probability.")
