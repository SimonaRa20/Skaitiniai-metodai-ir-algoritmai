import numpy as np
from scipy.optimize import fsolve
import scanDecreasing as scan
import matplotlib.pyplot as plt
import sys

def getMass(m):
    return 80 * np.exp(-(0.1 * 4)/m) + m * 9.8 / 0.1 * (np.exp(-(0.1 * 4)/m) - 1) - 21

def scanDecreasing(x1, x2):
    zingsnis = (x2 - x1) / 100
    print(zingsnis)
    while np.abs(getMass(x1)) > 0.001 and x1 + zingsnis <= x2:
        if np.sign(getMass(x1)) != np.sign(getMass(x1 + zingsnis)):
            zingsnis /= 2
            continue
        x1 += zingsnis
        print(zingsnis)
    return x1

ax = plt.subplot()
start = 0.5
end = 1.5
x = np.arange(start, end, 0.01)
afterFunctionX = scanDecreasing(start,end)
print(afterFunctionX)
ax.grid()
ax.plot(x, getMass(x))
plt.show()