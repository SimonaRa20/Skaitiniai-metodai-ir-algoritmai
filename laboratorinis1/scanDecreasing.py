import numpy as np
import math
import daugianaris as funkcija
import skenavimoAlgoritmas as intervalas

import scipy
def scanDecreasing(x1, x2):
    count = 0
    zingsnis = (x2 - x1) / 100
    count += 2
    while np.abs(funkcija.f(x1)) > 0.001 and x1 + zingsnis <= x2:
        if np.sign(funkcija.f(x1)) != np.sign(funkcija.f(x1 + zingsnis)):
            zingsnis /= 2
            count+=1
            continue
        x1 += zingsnis
        count+=1
    return x1, count

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


f = lambda x: 1.35 * x ** 4 + 0.93 * x ** 3 - 26.46 * x ** 2 - 16.20 * x + 76.19
start = funkcija.Rneig
end = funkcija.Rteig
intervalai = intervalas.getInterval(-start, end)

print('5 - Skenavimo su mazejanciu zingsniu metodo rezultatai:')
print('-' * 165)
print("|  {0:^44}  |  {1:^20}  |  {2:^30}  |  {3:^25}  |  {4:^20}  |".format('Intervalas', 'Gautoji saknis', 'Funkcijos reiksme saknyje', 'Tikslumas', 'Iteraciju skaicius'))
print('-' * 165)
for interval in intervalai:
    x0, count = scanDecreasing(interval[0], interval[1])
    intervalStart = interval[0]
    intervalEnd = interval[1]
    y = funkcija.f(x0)
    root = scipy.optimize.brentq(f, intervalStart, intervalEnd)
    print("|  [{0:^20}, {1:^20}]  |  {2:^20}  |  {3:^30}  |  {4:^25}  |  {5:^20}  |".format(intervalStart, intervalEnd, x0, y, root - x0, count))
print('-' * 165)
