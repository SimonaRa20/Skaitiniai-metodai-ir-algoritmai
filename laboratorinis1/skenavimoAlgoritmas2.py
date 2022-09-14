import matplotlib.pyplot as plt
import numpy as np
import math
import transcendentine as funkcija


def getInterval(start, end):
    step = (end - start) / 100
    x = start
    intervals = []

    while x < end:
        x_next = x + step
        if (funkcija.g(x) > 0 > funkcija.g(x_next)) or (funkcija.g(x_next) > 0 > funkcija.g(x)):
            intervals.append([x, x_next])
        x = x_next

    return intervals

interval = getInterval(1, 10);
print(interval)

gx = np.vectorize(funkcija.g)
x = np.arange(interval[0][0], interval[0][1], 0.01)
plt.plot(x, gx(x))
plt.grid()
plt.show()

