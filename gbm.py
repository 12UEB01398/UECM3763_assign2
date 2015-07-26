import pylab as p
import numpy as np

# Setup parameters
mu = 0.1;
sigma = 0.26; 
S0 = 39;
n_path = 1000; 
n = n_partitions = 1000;

# Create Brownian paths
t = p.linspace(0,3,n+1);
dB = p.randn(n_path, n+1) / p.sqrt(n);
dB[:,0] = 0;
B = dB.cumsum(axis=1);

# Calculate stock prices
nu = mu - sigma*sigma/2.0;
S = p.zeros_like(B); 
S[:,0] = S0;
S[:,1:] = S0*p.exp(nu*t[1:]+sigma*B[:,1:]);

# Plot 5 realizations of GBM
S5 = S[0:5];
p.plot(t,S5.transpose());
p.xlabel('Time, $t$');
p.ylabel('Stock price, $RM$');
p.title('5 realizations of GBM with mu $ = 0.1 $ , sigma $ = 0.26 $');
p.show();

# Calculate expected value of S(3)
S3 = p.array(S[:,-1]);
E_S3 = np.mean (S3);
print('Expectation value of S(3) =', E_S3);

# Calculate variance of S(3)
Var_S3 = np.var(S3);
print('Variance of S(3) =', Var_S3);

# Calculate P[S(3)>39]
x = S3 > 39;
Pr = sum(x) / len(x);
print('P[S(3) > 39] = ', Pr)

# Calculate E[S(3)|S(3)>39]
y = S3 * x
E_S3_39 = sum(y) / sum(x)
print('E[S(3) | S(3) > 39] =', E_S3_39)