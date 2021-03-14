import numpy as np
from scipy.stats import bernoulli

sample_size=100000

prob_A=0.3
prob_B=0.6

#Simulations using Bernoulli r.v.
sample_A= bernoulli.rvs(size= sample_size, p = prob_A)
sample_B= bernoulli.rvs(size= sample_size, p = prob_B)


#calculating P(A and B):
count=0
for i in range(sample_size):
    if sample_A[i] == 1 and sample_B[i] == 1:
        count +=1
        
#finding probability of A and B
prob_AB= count/sample_size        
print("P(A and B) = ", prob_AB)

print("which is approximately equal to 0.18(theoritical value)")
#calculating P(A and not B):
count=0
for i in range(sample_size):
    if sample_A[i] == 1 and sample_B[i] == 0:
        count +=1
        
#finding probability of A and not B
prob_AnB= count/sample_size        
print("P(A and not B) = ", prob_AnB)

print("which is approximately equal to 0.12(theoritical value)")
#calculating P(A or B):
count=0
for i in range(sample_size):
    if sample_A[i] == 1 or sample_B[i] == 1:
        count +=1
        
#finding probability of A or B
prob_AorB= count/sample_size        
print("P(A or B) = ", prob_AorB)

print("which is approximately equal to 0.72(theoritical value)")

#calculating P(neither A nor B):
count=0
for i in range(sample_size):
    if sample_A[i] == 0 and sample_B[i] == 0:
        count +=1
        
#finding probability of neither A nor B
prob_AnorB= count/sample_size        
print("P(neither A nor B) = ", prob_AnorB)

print("which is approximately equal to 0.28(theoritical value)")
