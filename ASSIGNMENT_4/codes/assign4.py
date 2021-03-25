import random as rand
import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import bernoulli
simlen=1000000
count=0
req=0
X=bernoulli.rvs(size=simlen,p=0.9)
Y=bernoulli.rvs(size=simlen,p=0.5)
for i in range(simlen):
  if Y[i]==0:
    count+=1
  if Y[i]==0 and X[i]==0:
    req+=1
print("simulated probability : ",req/count)
sim_prob=req/count
the_prob=0.1
data1 = {'theoritical probability':the_prob, 'simulated probability':sim_prob}
prob_type = list(data1.keys())
prob = list(data1.values())
  
fig = plt.figure(figsize = (6, 4))
 
# creating the bar plot
plt.bar(prob_type,prob, color ='Yellow',width = 0.1)
plt.xlabel("type of probability")
plt.ylabel("probability")
plt.show()
