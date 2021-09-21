"""
Violin Plot
"""
# In[] Libs
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# In[] Data
N = 1000
thresh = 5 # threshold for cropping data

data = np.exp(np.random.randn(N))
data[data>thresh] = thresh + np.random.randn(sum(data>thresh))*.1

# show histogram
plt.hist(data,30)
plt.title('Histogram')
plt.show()

# show violin plot
plt.violinplot(data)
plt.title('Violin')
plt.show()


# In[] By using swarm plot
import seaborn as sns
sns.set_theme(style="whitegrid")
ax = sns.swarmplot(data=data, orient="v", color=".2")
ax = sns.boxplot(data=data, whis=np.inf)
ax = sns.violinplot(data=data, inner=None, color=".5")
