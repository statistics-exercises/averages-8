import matplotlib.pyplot as plt
import numpy as np

def binomial(k,p) :
  # Your code to generate the binomial random variable goes here
  
pval, kval = 0.2, 8
ssum, ssum2, indices, p_estimator, k_estimator = 0, 0, np.zeros(200), np.zeros(200), np.zeros(200)
for i in range(200) : 
  # Add code to setup the numpy arrays called indices, p_estimator and k_estimator to generate the desired
  # plot here.
  
  
  
# This will plot the graph for the data.  You should not need to adjust this.
plt.plot( indices, p_estimator, 'ro' )
plt.plot( [0,200], [pval,pval], 'k--' )
plt.plot( indices, k_estimator, 'bo' )
plt.plot( [0,200], [kval,kval], 'g--' )
plt.xlabel("Number of random variables")
plt.ylabel("Estimator")
plt.savefig("binomial_estimator.png")
