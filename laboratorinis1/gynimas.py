# gynimo užduotis
import matplotlib.pyplot as plt
import numpy as np
from random import random


def funkcija(x,alfa):
    if x < alfa:
        return 1
    if x == alfa:
        return 0
    else:
        return -1

alfa = random()

x = np.arange(-2, 2, 0.001)
y = []
for xx in x:
    y.append(funkcija(xx,alfa))

plt.plot(x, y)
plt.grid()
plt.show()

