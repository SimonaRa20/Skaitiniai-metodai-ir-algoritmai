import math
import skenavimoAlgoritmas2 as skenavimas
from scipy.optimize import fsolve
import scipy

def discrete_method_approx(f, x, h=.001):
    return (f(x + h) - f(x)) / h

def NewtonsMethod(f, x, tolerance=.001):
    count = 0
    while abs(f(x)) > tolerance:
        df = discrete_method_approx(f,x)
        x = x - f(x) / df
        count += 1
    return x, count


f = lambda x: (math.log(x) / (math.sin(2 * x) + 1.5)) - x / 7
start = 1
end = 10

intervalai = skenavimas.getInterval(start, end);
print('-' * 165)
print("|  {0:^44}  |  {1:^20}  |  {2:^30}  |  {3:^25}  |  {4:^20}  |".format('Intervalas', 'Gautoji saknis', 'Funkcijos reiksme saknyje', 'Tikslumas', 'Iteraciju skaicius'))
print('-' * 165)

i = 0
for interval in intervalai:
    x0, count = NewtonsMethod(f, interval[0])
    g = skenavimas.gx(x0)
    intervalStart = interval[0]
    intervalEnd = interval[1]
    root = scipy.optimize.brentq(f, intervalStart, intervalEnd)
    print("|  [{0:^20}, {1:^20}]  |  {2:^20}  |  {3:^30}  |  {4:^25}  |  {5:^20}  |".format(intervalStart, intervalEnd, x0, g, root - x0, count))
print('-' * 165)