"""
Calculate the T-test for the mean of ONE group of scores.
This is a two-sided test for the null hypothesis that the expected value (mean) 
    	of a sample of independent observations a is equal to the given population 
        mean, popmean.
Resource: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_1samp.html
"""

# In[] Libs
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# In[] Genrate data
sample_size = 20
population_mean = .5
data = np.random.randn(sample_size) + population_mean

plt.clf()
plt.plot(data, "ko", markersize=10)
plt.xlabel('Data index')
plt.ylabel('Data value')
plt.show()

# In[] Manual T-Test
h0_val = 0 # the null hypothesis, testing the mean of the population against the null hypothesis

# Compute the t-value
t_numerator = np.mean(data) - h0_val
t_denominator = np.std(data, ddof=1) / np.sqrt(sample_size)
t_value = t_numerator / t_denominator

df = sample_size - 1 # degrees of freedom for one-sample t-test
p_value = 1 - stats.t.cdf(abs(t_value), df)

# Show the H0 parameter distribution and observed t-value
x_timeline = np.linspace(-4, 4, 1001)
t_distribution = stats.t.pdf(x_timeline, df) * np.mean(np.diff(x_timeline))

plt.clf()
plt.plot(x_timeline, t_distribution, linewidth=2, label="H0 distribution")
plt.plot([t_value, t_value], [0, max(t_distribution)], "r--", label="Observed t-value")
plt.xlabel("t-value")
plt.ylabel("pdf(t)")
plt.title(f"t({df}) = {t_value:0.4f}, p={p_value:0.34f}")
plt.legend()
plt.show()

# In[] T-Test from stats package
statistic, p_value = stats.ttest_1samp(a=data, popmean=h0_val)
print(f"t-Statistic= {statistic:0.4f}, p={p_value/2:0.34f}")
