import numpy as np
import matplotlib.pyplot as plt
#If using termux
import subprocess
import shlex
#end if

#Sample size
simlen = 1000000
#Possible outcomes
n = range(3,19)
# Generate X1 and X2 and X3
y = np.random.randint(1,7, size=(3, simlen))

#Generate X
X = np.sum(y, axis = 0) 
#Find the frequency of each outcome
unique, counts = np.unique(X, return_counts=True)
#Simulated probability
psim = counts/simlen
a=0
#Theoretical probability
n1 = [3,4,5,6,7,8]
n2 = [9,10,11,12,13,14]
n3 = [15,16,17,18]
panal1=[]
panal2=[]
panal3=[]
for i in range(6):
  panal1.append((n1[i])**2-(n1[i])*3 +2)
  panal2.append(n2[i]*42-166-2*n2[i]**2)
for i in range(4):
  panal3.append(380+n3[i]**2-n3[i]*39)
panal = np.concatenate((panal1,panal2,panal3),axis=None)/432
a=np.sum(panal)
print("The generated probability mass function adds to ",a)
#Plotting
plt.stem(n,psim, markerfmt='o', use_line_collection=True, label='Simulation')
plt.stem(n,panal, markerfmt='o',use_line_collection=True, label='Analysis')
plt.xlabel('$n$')
plt.ylabel('$p_{X}(n)$')
plt.legend()
plt.grid()# minor
print("Therefore simulations are close to analysis")
