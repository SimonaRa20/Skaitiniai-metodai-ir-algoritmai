import matplotlib.pyplot as plt
import numpy as np
import daugianaris as funkcija

def getInterval(start, end):
    step = (end - start) / 100
    x = start
    intervals = []

    while x < end:
        x_next = x + step
        if (funkcija.f(x) > 0 > funkcija.f(x_next)) or (funkcija.f(x_next) > 0 > funkcija.f(x)):
            intervals.append([x, x_next])
        x = x_next

    return intervals

startIndex = -funkcija.Rneig
endIndex = funkcija.Rteig
interval = getInterval(startIndex, endIndex);
print(interval)

x = np.arange(interval[0][0], interval[0][1], 0.001)
y = funkcija.f(x)
# plt.plot(x, y)
# plt.grid()
# plt.show()
