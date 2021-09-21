"""
Different data distributions
"""
# In[] Libs
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# In[] Gaussian

# number of discretizations
N = 1001

data = np.linspace(-10, 10, N)
gaussian_dist = stats.norm.pdf(data) # calculate the probability density

plt.plot(data, gaussian_dist)
plt.title("Analytic Gaussian (normal) distribution")
plt.show()

# In[]