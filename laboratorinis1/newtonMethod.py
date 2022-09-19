
import daugianaris as funkcija
import skenavimoAlgoritmas as intervalas
import scipy
from scipy.misc import derivative

def NewtonsMethod(f, x1, x2):
    count = 0
    x = (x1 + x2) / 2
    while (abs(f(x))) > 1e-10:
        fx = f(x)
        fdx = derivative(f, x, dx=1e-6)
        x = x - (fx / fdx)
        count += 1
    return x, count
# def discrete_method_approx(f, x, h=.001):
#     return (f(x + h) - f(x)) / h
#
# def NewtonsMethod(f, x, tolerance=.001):
#     count = 0
#     while abs(f(x)) > tolerance:
#         df = discrete_method_approx(f,x)
#         x = x - f(x) / df
#         count += 1
#     return x, count


f = lambda x: 1.35 * x ** 4 + 0.93 * x ** 3 - 26.46 * x ** 2 - 16.20 * x + 76.19
intervalai = intervalas.interval;
#
print('3 - Niutono (liestiniu) metodo rezultatai:')
print('-' * 165)
print("|  {0:^44}  |  {1:^20}  |  {2:^30}  |  {3:^25}  |  {4:^20}  |".format('Intervalas', 'Gautoji saknis', 'Funkcijos reiksme saknyje', 'Tikslumas', 'Iteraciju skaicius'))
print('-' * 165)
for interval in intervalai:
    intervalStart = interval[0]
    intervalEnd = interval[1]
    x0, count = NewtonsMethod(f, intervalStart, intervalEnd)
    y = funkcija.f(x0)
    root = scipy.optimize.brentq(f, intervalStart, intervalEnd)
    print("|  [{0:^20}, {1:^20}]  |  {2:^20}  |  {3:^30}  |  {4:^25}  |  {5:^20}  |".format(intervalStart, intervalEnd, x0, y, root - x0, count))
print('-' * 165)
