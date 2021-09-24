"""
Shanon Entropy
"""
# In[] Libs
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# In[] Data
data_gait_right_ankle = pd.read_csv("..\\datasets\\Gait_right_ankle.csv", skiprows=12)
data_gait_left_ankle = pd.read_csv("..\\datasets\\Gait_left_ankle.csv", skiprows=12)
_feature = "Gyr_X"
x = data_gait_right_ankle[_feature]+np.finfo(float).eps
scaler = MinMaxScaler(feature_range=(0, 1))
x = scaler.fit_transform(x.values.reshape(-1, 1)).flatten()

# In[] Plot the data
plt.clf()
plt.plot(x)
plt.show()

# In[] Plot the histogram and test the distribution type
plt.clf()
plt.hist(x, bins=50, density=True)
plt.show()

# In[] Bin the data and convert to probability
n_bins = 50
n_per_bin, bins = np.histogram(x, n_bins)
x_probs = n_per_bin / sum(n_per_bin)

# In[] Discretize/Bin the data
bins = list(np.arange(int(min(x))-1, int(max(x))+1, .05))
data_digitized = np.digitize(x, bins=bins)

plt.clf()
plt.plot(data_digitized)
plt.show()

# In[] Bin the data and convert to probability
n_bins = 50
n_per_bin, bins = np.histogram(data_digitized, n_bins)
data_digitized_probs = n_per_bin / sum(n_per_bin)

# In[] Plot the histogram and test the distribution type
plt.clf()
plt.hist(data_digitized, bins=50, density=True)
plt.show()

# In[] Compute Entropy
_tmp_data = x_probs
entropy_1 = -sum(_tmp_data*np.log2(_tmp_data+np.finfo(float).eps))

_tmp_data = data_digitized_probs
entropy_2 = -sum(_tmp_data*np.log2(_tmp_data+np.finfo(float).eps))
