import matplotlib.pyplot as plt
import numpy as np
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

def g_derivative(x):
    return (1 / x * (sin(2 * x) + 3 / 2)) - (2 * np.log(x) * cos(2*x) / (sin(2 * x) + 3/2)**2) - 1 / 7

def absolute_terminate(function, x_mid, epsilon=1e-6):
    return abs(function(x_mid)) < epsilon
def ChordMethod(x_n, x_n1, iteration=1):
    if (x_n > x_n1):
        raise Exception("Incorrect function usage")

    # if (x_n == x_n1):
    #     return (x_mid, 'Iteracijų kiekis ' + str(iteration))

    k = abs(funkcija.f(x_n) / funkcija.f(x_n1))
    x_mid = (x_n + k * x_n1) / (1 + k)

    if (funkcija.f(x_mid) == 0 or absolute_terminate(funkcija.f, x_mid)):
        return x_mid, iteration

    if (sign(funkcija.f(x_mid)) == sign(funkcija.f(x_n))):
        return ChordMethod(x_mid, x_n1, iteration + 1)

    return ChordMethod(x_n, x_mid, iteration + 1)

start = 1 + (26.46 / 1.35)
end = 1 + math.sqrt(26.46 / 1.35)
intervals = intervalas.getInterval(-start, end);
roots = []

for interval in intervals:
    roots.append(ChordMethod(interval[0], interval[1]))

print(roots[0][0])

# start = 1 + (26.46 / 1.35)
# end = 1 + math.sqrt(26.46 / 1.35)
# intervalai = intervalas.getInterval(-start, end);
# print('-' * 105)
# print("|  {0:^44}  |  {1:^25}  |  {2:^20}  |".format('Intervalas','Iteraciju skaicius','Gautoji saknis'))
# print('-' * 105)
# for interval in intervalai:
#     x0, count = ChordMethod(interval[0], interval[1])
#     intervalStart = interval[0]
#     intervalEnd = interval[1]
#     print("|  [{0:^20}, {1:^20}]  |  {2:^25}  |  {3:^20}  |".format(intervalStart, intervalEnd, count, x0))
# print('-' * 105)



# interval = intervalas.getInterval(-start, end)[0];
#
# x = interval[0]
# print(x)
# x0 = ChordMethod(interval[0], interval[1])
#
# print('x: ', x)
# print('x0: ', x0)
# print("f(x0) = ", funkcija.f(x0))

