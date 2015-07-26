import pylab as p
import numpy as np

# Setup parameters
n_path = 1000;
n = n_partitions = 1000;
t = 1.0;
alpha = 1.0;
theta = 0.064;
sigma = 0.27;
R0 = 3.0;

# Create Brownian paths
dt = t/n;
t = p.linspace (0,t,n+1)[:-1];
dB = p.randn(n_path, n+1) * p.sqrt(dt);
dB[:,0] = 0;
B = dB.cumsum(axis=1);

#  Simulate R(t)
R = p.zeros_like(B);
R[:,0] = R0;
for col in range(n):
    R[:,col+1] = R[:,col] + (theta - R[:,col])*dt + sigma*R[:,col]*dB[:,col+1];

# Plot 5 realizations of mean reversal process    
R5 = R[0:5,:-1];
p.plot(t,R5.transpose());
p.xlabel('Time, $t$');
p.ylabel('R(t)');
p.title('5 realizations of mean reversal process');
p.show();

# Calculate expected value of R(1)
R1 = p.array(R[:,-1]);
E_R1 = np.mean(R1)
print('Expectation value of R(1) = ', E_R1);

# Calculate P[R(1)>2]
x = R1>2
Pr = sum(x)/len(x)
print('P[R(1)>2] = ', Pr)