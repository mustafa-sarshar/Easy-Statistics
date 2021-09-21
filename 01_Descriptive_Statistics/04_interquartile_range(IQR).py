"""
Interquartile Range - IQR
"""
# In[] Libs
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# In[] Self generated data
N = 1000
data = np.random.randn(N)**2

plt.clf()
plt.scatter(list(range(len(data))), data)
plt.show()

# In[] Manully find the IQR
# Rank-transform and scaled to 1
data_ranked = stats.rankdata(data)/N

# find the values closest to 25% and 75% of the distribution
q1 = np.argmin((data_ranked-.25)**2) # find the index of the data close to 0.25 and square it to eliminate the negative signs
q3 = np.argmin((data_ranked-.75)**2) # find the index of the data close to 0.75 and square it to eliminate the negative signs

# get the two values in the data
iq_vals = data_ranked[[q1, q3]]

# IQR is the difference between them
iqr_manual = iq_vals[1] - iq_vals[0]

print(f"IQR: {iqr_manual}")

# In[] Use Python's built-in function
iqr_stats = stats.iqr(data)
print(f"IQR: {iqr_stats}")