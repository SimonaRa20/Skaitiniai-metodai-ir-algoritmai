import matplotlib.pyplot as plt
import numpy as np
import scipy
import math
import skenavimoAlgoritmas as intervalas
import daugianaris as funkcija
from scipy import misc

def sign(number):
    if (number > 0):
        return 1

    if (number < 0):
        return -1

    return 0
def f_derivative(x):
    return -27*x**3 / 5 - 279*x**2 / 100 + 1323*x / 25 + 81/5

def absolute_terminate(function, x_mid, epsilon=1e-6):
    return abs(function(x_mid)) < epsilon
def ChordMethod(x_n, x_n1, iteration=1):
    if (x_n > x_n1):
        raise Exception("Incorrect function usage")

    k = abs(funkcija.f(x_n) / funkcija.f(x_n1))
    x_mid = (x_n + k * x_n1) / (1 + k)

    if (funkcija.f(x_mid) == 0 or absolute_terminate(funkcija.f, x_mid)):
        return x_mid, iteration

    if (sign(funkcija.f(x_mid)) == sign(funkcija.f(x_n))):
        return ChordMethod(x_mid, x_n1, iteration + 1)

    return ChordMethod(x_n, x_mid, iteration + 1)

start = funkcija.Rneig
end = funkcija.Rteig
intervals = intervalas.getInterval(-start, end);
roots = []

for interval in intervals:
    roots.append(ChordMethod(interval[0], interval[1]))


f = lambda x: 1.35 * x ** 4 + 0.93 * x ** 3 - 26.46 * x ** 2 - 16.20 * x + 76.19
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
    y = funkcija.f(x0)
    root = scipy.optimize.brentq(f, intervalStart, intervalEnd)
    print("|  [{0:^20}, {1:^20}]  |  {2:^20}  |  {3:^30}  |  {4:^25}  |  {5:^20}  |".format(intervalStart, intervalEnd, x0, y, root - x0, count))
    i += 1
print('-' * 165)
