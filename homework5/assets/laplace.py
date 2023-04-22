import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import laplace

# Mean and scale parameter
mu = 0
scale = 1

# Generate random numbers from Laplace distribution with the parameters
x = np.arange(-5, 5, 0.1)
pdf = laplace.pdf(x, mu, scale)
cdf = laplace.cdf(x, mu, scale)

# Plotting probability density function and cumulative distributive function
fig, ax = plt.subplots(1, 2, figsize=(10, 5))
ax.plot(x, pdf, label='PDF')
ax.plot(x, cdf, label='CDF')
ax.set_title('Probability Density Function')
ax.set_title('Cumulative Distributive Function')
ax.legend()
ax.legend()
plt.show()
