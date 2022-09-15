import scipy
import skenavimoAlgoritmas2 as intervalas
import transcendentine as funkcija
import math
from math import sin, cos
import numpy as np

def sign(number):
    if (number > 0):
        return 1

    if (number < 0):
        return -1

    return 0
def g_derivative(x):
    return (1 / x * (sin(2 * x) + 3 / 2)) - (2 * np.log(x) * cos(2*x) / (sin(2 * x) + 3/2)**2) - 1 / 7
def absolute_terminate(function, x_mid, epsilon=1e-6):
    return abs(function(x_mid)) < epsilon
def ChordMethod(x_n, x_n1, iteration=1):
    if (x_n > x_n1):
        raise Exception("Incorrect function usage")

    k = abs(funkcija.g(x_n) / funkcija.g(x_n1))
    x_mid = (x_n + k * x_n1) / (1 + k)

    if (funkcija.g(x_mid) == 0 or absolute_terminate(funkcija.g, x_mid)):
        return x_mid, iteration

    if (sign(funkcija.g(x_mid)) == sign(funkcija.g(x_n))):
        return ChordMethod(x_mid, x_n1, iteration + 1)

    return ChordMethod(x_n, x_mid, iteration + 1)

intervals = intervalas.interval;
roots = []

for interval in intervals:
    roots.append(ChordMethod(interval[0], interval[1]))

g = lambda x: (math.log(x) / (math.sin(2 * x) + 1.5)) - x / 7
i = 0
print('1 - Stygu metodo rezultatai:')
print('-' * 165)
print("|  {0:^44}  |  {1:^20}  |  {2:^30}  |  {3:^25}  |  {4:^20}  |".format('Intervalas', 'Gautoji saknis', 'Funkcijos reiksme saknyje', 'Tikslumas', 'Iteraciju skaicius'))
print('-' * 165)
for interval in intervals:
    x0 = roots[i][0]
    count = roots[i][1]
    intervalStart = interval[0]
    intervalEnd = interval[1]
    y = funkcija.g(x0)
    root = scipy.optimize.brentq(g, intervalStart, intervalEnd)
    print("|  [{0:^20}, {1:^20}]  |  {2:^20}  |  {3:^30}  |  {4:^25}  |  {5:^20}  |".format(intervalStart, intervalEnd, x0, y, root - x0, count))
    i += 1
print('-' * 165)