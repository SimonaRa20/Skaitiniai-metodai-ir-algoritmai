import matplotlib.pyplot as plt
import numpy as np
import math


def g(x):
    y = (math.log(x) / (math.sin(2 * x) + 1.5)) - x / 7
    return y

gx = np.vectorize(g)
start = 1
end = 10
x = np.arange(start, end, 0.01)
# plt.plot(x, gx(x))
# plt.grid()
# plt.show()
