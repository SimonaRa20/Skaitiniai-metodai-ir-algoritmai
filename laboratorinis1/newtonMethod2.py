import math
import skenavimoAlgoritmas2 as skenavimas
from scipy.optimize import fsolve
import scipy

from scipy.misc import derivative

def NewtonsMethod(g, x1, x2):
    count = 0
    x = (x1 + x2) / 2
    while (abs(g(x))) > 1e-6:
        gx = g(x)
        gdx = derivative(g, x, dx=1e-6)
        x = x -(gx / gdx)
        count += 1
    return x, count


# def discrete_method_approx(g, x, h=.001):
#     return (g(x + h) - g(x)) / h
#
# def NewtonsMethod(g, x, tolerance=.001):
#     count = 0
#     while abs(g(x)) > tolerance:
#         df = discrete_method_approx(g,x)
#         x = x - g(x) / df
#         count += 1
#     return x, count

g = lambda x: (math.log(x) / (math.sin(2 * x) + 1.5)) - x / 7

intervalai = skenavimas.interval;
print('3 - Niutono (liestiniu) metodo rezultatai:')
print('-' * 165)
print("|  {0:^44}  |  {1:^20}  |  {2:^30}  |  {3:^25}  |  {4:^20}  |".format('Intervalas', 'Gautoji saknis', 'Funkcijos reiksme saknyje', 'Tikslumas', 'Iteraciju skaicius'))
print('-' * 165)
for interval in intervalai:
    x0, count = NewtonsMethod(g, interval[0], interval[1])
    y = skenavimas.gx(x0)
    intervalStart = interval[0]
    intervalEnd = interval[1]
    root = scipy.optimize.brentq(g, intervalStart, intervalEnd)
    print("|  [{0:^20}, {1:^20}]  |  {2:^20}  |  {3:^30}  |  {4:^25}  |  {5:^20}  |".format(intervalStart, intervalEnd, x0, y, root - x0, count))
print('-' * 165)