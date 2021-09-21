"""
QQ plot - Normality test for data distribution
"""
# In[] Libs
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import statsmodels.api as sm

# In[]
N = 10001
data_normal_dist = np.random.randn(N) # empricial normal distribution
data_non_normal_dist = np.exp(np.random.randn(N)*.8) # log-norm distribution

x = np.linspace(-8, 8, N) # theoretical normal distribution given N

# In[] Plot the histograms on top of each other
yy, xx = np.histogram(data_normal_dist,40)
yy = yy/max(yy)
xx = (xx[:-1]+xx[1:])/2

data_normal_dist_theo = stats.norm.pdf(x)
data_normal_dist_theo = data_normal_dist_theo/max(data_normal_dist_theo)

plt.plot(xx,yy,label="Empirical")
plt.plot(x,data_normal_dist_theo,label="Theoretical")
plt.legend()
plt.show()

# In[] plot the QQ plot of each separately
fig = sm.qqplot(data_normal_dist, stats.t, fit=True, line="45")
plt.title("Probability Plot")
plt.xlabel("Theoretical quantities")
plt.ylabel("Ordered Values")
plt.show()

# In[] plot the QQ plot of each separately
fig = sm.qqplot(data_non_normal_dist, stats.t, fit=True, line="45")
plt.title("Probability Plot")
plt.xlabel("Theoretical quantities")
plt.ylabel("Ordered Values")
plt.show()

# In[] Finish