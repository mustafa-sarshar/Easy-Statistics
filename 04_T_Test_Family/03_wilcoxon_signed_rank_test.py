"""
Calculate the Wilcoxon signed-rank test.

The Wilcoxon signed-rank test tests the null hypothesis that two related paired 
    samples come from the same distribution. 
In particular, it tests whether the distribution of the differences x - y
    is symmetric about zero.
It is a non-parametric version of the paired T-test.
Resources:
    https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.wilcoxon.html
    https://datatab.net/tutorial/wilcoxon-test
"""

# In[] Libs
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

# In[] Generate the data
sample_size_n = 20

sample_1_lam = 1
sample_2_lam = 1.5

data_pre = np.random.poisson(sample_1_lam, sample_size_n)
data_post = np.random.poisson(sample_2_lam, sample_size_n)

# In[] Compute the Wilcoxon signed-rank test for pre and post data and depict how the values are changed
statistic, p_value = stats.wilcoxon(data_pre, data_post)
df = sample_size_n - 1

plt.clf()
colors = "br"
for i in range(sample_size_n):
    plt.plot([data_pre[i], data_post[i]], [i, i], colors[int(data_pre[i]<data_post[i])])
plt.plot(data_pre, np.arange(sample_size_n), "bs", markerfacecolor="b", label="data pre", alpha=.5)
plt.plot(data_post, np.arange(sample_size_n), "ro", markerfacecolor="r", label="data post", alpha=.5)
plt.ylabel("Data index")
plt.xlabel("Data value")
plt.title(f"p({df}) = {abs(statistic):0.4f}, p = {p_value:0.4f}")
plt.legend()
plt.show()

# In[] Finish
