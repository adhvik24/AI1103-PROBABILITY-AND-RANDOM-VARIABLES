from scipy.stats import bernoulli
import matplotlib.pyplot as plt
simlen=100000
X_1= bernoulli .rvs(0.1, size = simlen) 
X_2= bernoulli .rvs(0.1, size = simlen) 
X_3= bernoulli .rvs(0.1, size = simlen) 
X_4= bernoulli .rvs(0.1, size = simlen) 
count=0
for i in range(simlen):
  if(X_1[i]==1 or X_2[i]==1 or X_3[i]==1 or X_4[i]==1):
    count+=1
print("simulated probability : ",count/simlen)
print("Theoretical probability : ",1-(0.9)**4)
print("Both simulated and theoritical probability are nearly same.")
sim_prob=count/simlen
the_prob=1-(0.9)**4
data1 = {'theoritical probability':the_prob, 'simulated probability':sim_prob}
prob_type = list(data1.keys())
prob = list(data1.values())
  
fig = plt.figure(figsize = (6, 4))
 
# creating the bar plot
plt.bar(prob_type,prob, color ='Yellow',width = 0.1)
plt.xlabel("type of probability")
plt.ylabel("probability")
plt.show()
