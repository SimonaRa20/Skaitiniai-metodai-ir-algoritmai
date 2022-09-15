import math

import matplotlib.pyplot as plt
import numpy as np

def f(_x):
    y = 1.35 * _x ** 4 + 0.93 * _x ** 3 - 26.46 * _x ** 2 - 16.20 * _x + 76.19
    return y

R = 1 + (76.19 / 1.35)
# x = np.arange(-R, R) # grubus intervalas

kteig = 4 - 2
Bteig = 26.46
Rteig = 1 + math.sqrt(Bteig / 1.35)

kneig = 4 - 3
Bneig = 26.46
Rneig = 1 + Bneig / 1.35
# x = np.arange(-Rneig, Rteig) # tikslesnis intervalas

x = np.arange(-4, -2.25, 0.001)
# y = f(x)
# plt.plot(x, y)
# plt.grid()
# plt.show()
