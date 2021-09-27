"""
Mann-Whitney U rank test on two independent samples.

The Mann-Whitney U test is a nonparametric test of the null hypothesis that the 
    distribution underlying sample x is the same as the distribution underlying sample y. 
It is often used as a test of of difference in location between distributions.
Resources:
    https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.mannwhitneyu.html
    https://datatab.net/tutorial/mann-whitney-u-test
"""


# In[] Libs
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

# In[] Generate the data
population_1_n = 30
population_2_n = 40
population_1_lam = 1
population_2_lam = 1.5

population_1 = np.random.poisson(population_1_lam, population_1_n)
population_2 = np.random.poisson(population_2_lam, population_2_n)

# In[] Compute the Wilcoxon signed-rank test for pre and post data and depict how the values are changed
statistic, p_value = stats.mannwhitneyu(population_1, population_2, alternative="two-sided", use_continuity=True)
df = population_1_n + population_2_n - 2

plt.clf()
plt.hist(population_1, bins="fd", color=[1, 0, 0, .5], label="Population 1")
plt.hist(population_2, bins="fd", color=[0, 0, 1, .5], label="Population 2")
plt.xlabel("Data value")
plt.ylabel("Count")
plt.title(f"p({df}) = {abs(statistic):0.4f}, p = {p_value:0.4f}")
plt.legend()
plt.show()

# In[] Finish
