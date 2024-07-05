
from math import log2
from scipy.stats import binom
from matplotlib import pyplot
import matplotlib.pyplot as plt
import numpy as np
# calculate the kl divergence
def kl_divergence(p, q):
    return sum(p[i] * log2(p[i]/q[i]) for i in range(len(p)))

# define distributions
p_values = [0,1,2,3,4,5,6,7,8,9,10]
observed_probabilities = [0.005,0.01,0.04,0.12,0.18,0.19,0.14,0.07,0.1,0.08,0.065] #real prob
KL=[]
P1 = []
# Fit a binomial distribution to the data
for i in range (1,12,1):         
    n = 10  # Number of trials in the binomial distribution
    p = i/10  # Initial guess for the probability of success
    P1.append(p)
    Q = [] # esimate prob
    dist = binom(n,p)
    for n in range(0, 11, 1):
        x = dist.pmf(n)
        Q.append(x)
    # calculate (P || Q)
    kl_pq = kl_divergence(observed_probabilities, Q)
    KL.append(kl_pq)
# Plot the empirical distribution and the binomial distribution
#pyplot.bar(p_values, observed_probabilities)
#pyplot.plot(p_values, q_binomial, 'ro-')
#pyplot.show()

print('KL(P || Q): ' ,KL)
best_p_index = KL.index(min(KL))
best_p = P1[best_p_index]
min_x = np.min(best_p)
min_y = best_p
plt.xlabel('p')
plt.ylabel('KL Divergence')
plt.plot(P1,KL)
plt.scatter(min_x,min_y,c='r',label='minimum')
plt.legend()
plt.show()
print(f"The parameter p corresponding to the lowest KL Divergence is: {best_p}")
