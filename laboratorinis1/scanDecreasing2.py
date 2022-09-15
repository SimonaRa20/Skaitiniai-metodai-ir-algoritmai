import numpy as np
import transcendentine as funkcija
import skenavimoAlgoritmas2 as intervalas
import scipy
import math

def scanDecreasing(x1, x2):
    count = 0
    zingsnis = (x2 - x1) / 100
    count += 2
    while np.abs(funkcija.g(x1)) > 0.001 and x1 + zingsnis <= x2:
        if np.sign(funkcija.g(x1)) != np.sign(funkcija.g(x1 + zingsnis)):
            zingsnis /= 2
            count+=1
            continue
        x1 += zingsnis
        count+=1
    return x1, count


g = lambda x: (math.log(x) / (math.sin(2 * x) + 1.5)) - x / 7
intervalai = intervalas.interval;

# print('5 - Skenavimo su mazejanciu zingsniu metodo rezultatai:')
# print('-' * 165)
# print("|  {0:^44}  |  {1:^20}  |  {2:^30}  |  {3:^25}  |  {4:^20}  |".format('Intervalas', 'Gautoji saknis', 'Funkcijos reiksme saknyje', 'Tikslumas', 'Iteraciju skaicius'))
# print('-' * 165)
# for interval in intervalai:
#     x0, count = scanDecreasing(interval[0], interval[1])
#     intervalStart = interval[0]
#     intervalEnd = interval[1]
#     y = funkcija.g(x0)
#     root = scipy.optimize.brentq(g, intervalStart, intervalEnd)
#     print("|  [{0:^20}, {1:^20}]  |  {2:^20}  |  {3:^30}  |  {4:^25}  |  {5:^20}  |".format(intervalStart, intervalEnd, x0, y, root - x0, count))
# print('-' * 165)
