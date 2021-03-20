import numpy as np
from scipy.stats import uniform
from matplotlib import pyplot as plt
uniform_data = np.linspace(0,1,100000)
plot1 = plt.figure(1)
fx = uniform.pdf(uniform_data,0,1)
plt.plot(uniform_data,fx)
plt.title("Probability density function of U:")
plt.xlabel("$x$")
plt.ylabel("$f_U(x)$")
plt.show()
