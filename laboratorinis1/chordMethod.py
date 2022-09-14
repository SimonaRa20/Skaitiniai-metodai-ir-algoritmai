import matplotlib.pyplot as plt
import numpy as np
import math
import skenavimoAlgoritmas as intervalas
import daugianaris as funkcija
from scipy import misc

def ChordMethod(start, end):
    count = 0
    x1 = start
    x2 = end
    count += 2
    y1 = funkcija.f(x1)
    count += 8
    y2 = funkcija.f(x2)
    count += 8

    # susidarysiu lygtį iš dviejų taškų y = kx + b
    k = (y2 - y1) / (x2 - x1)
    b = y1 - k * x1
    count += 5

    # susidaryta lygti prisilyginu 0 ir ieskau saknies
    x = ((-1) * b) / k
    count += 2

    return x, count

start = 1 + (26.46 / 1.35)
end = 1 + math.sqrt(26.46 / 1.35)
intervalai = intervalas.getInterval(-start, end);
print('-' * 105)
print("|  {0:^44}  |  {1:^25}  |  {2:^20}  |".format('Intervalas','Iteraciju skaicius','Gautoji saknis'))
print('-' * 105)
for interval in intervalai:
    x0, count = ChordMethod(interval[0], interval[1])
    intervalStart = interval[0]
    intervalEnd = interval[1]
    print("|  [{0:^20}, {1:^20}]  |  {2:^25}  |  {3:^20}  |".format(intervalStart, intervalEnd, count, x0))
print('-' * 105)



# interval = intervalas.getInterval(-start, end)[0];
#
# x = interval[0]
# print(x)
# x0 = ChordMethod(interval[0], interval[1])
#
# print('x: ', x)
# print('x0: ', x0)
# print("f(x0) = ", funkcija.f(x0))

