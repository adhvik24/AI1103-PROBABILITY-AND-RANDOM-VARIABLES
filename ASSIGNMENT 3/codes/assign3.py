import random as rand
import numpy as np
from matplotlib import pyplot as plt

sim_len=100000
count=0
for i in range (sim_len):
  X_1=np.random.randint(1,7)
  X_2=np.random.randint(1,7)
  X_3=np.random.randint(1,7)
  if(X_1+X_2+X_3==5):
     count+=1
  sim_prob=count/sim_len
  the_prob=1/36
print("probability by simulation = ",sim_prob)
print("theoritical probability=",the_prob)
data1 = {'theoritical probability':the_prob, 'simulated probability':sim_prob}
prob_type = list(data1.keys())
prob = list(data1.values())
  
fig = plt.figure(figsize = (6, 4))
 
# creating the bar plot
plt.bar(prob_type,prob, color ='Yellow',width = 0.08)
plt.xlabel("type of probability")
plt.ylabel("probability")
plt.title("Probability of getting 5")
plt.show()
