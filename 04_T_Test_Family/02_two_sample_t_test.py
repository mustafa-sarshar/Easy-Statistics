"""
Calculate the T-test for the means of two independent samples of scores.
This is a two-sided test for the null hypothesis that 2 independent samples have 
    identical average (expected) values.
This test assumes that the populations have identical variances by default.
Resource: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html
"""

# In[] Libs
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

# In[] Generate the data
population_1_n = 30
population_2_n = 40
population_1_mu = 1
population_2_mu = 1.2

population_1 = population_1_mu + np.random.randn(population_1_n)
population_2 = population_2_mu + np.random.randn(population_2_n)

# In[] Compute the two-sample t-test for independent equal variances and plot the histogram
statistic, p_value = stats.ttest_ind(population_1, population_2, equal_var=True)
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
