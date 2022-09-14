import numpy as np
import math
import daugianaris as funkcija
import skenavimoAlgoritmas as intervalas


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

start = 1 + (26.46 / 1.35)
end = 1 + math.sqrt(26.46 / 1.35)
interval = getInterval(-start, end)[0];

# x = interval[0]
# print(interval)
# x0 = scanDecreasing(interval[0], interval[1])

start = 1 + (26.46 / 1.35)
end = 1 + math.sqrt(26.46 / 1.35)
intervalai = intervalas.getInterval(-start, end);
print('-' * 105)
print("|  {0:^44}  |  {1:^25}  |  {2:^20}  |".format('Intervalas','Iteraciju skaicius','Gautoji saknis'))
print('-' * 105)
for interval in intervalai:
    x0, count = scanDecreasing(interval[0], interval[1])
    intervalStart = interval[0]
    intervalEnd = interval[1]
    print("|  [{0:^20}, {1:^20}]  |  {2:^25}  |  {3:^20}  |".format(intervalStart, intervalEnd, count, x0))
print('-' * 105)





# print('x: ', x)
# print('x0: ', x0)
# print("f(x0) = ", 1.35 * x ** 4 + 0.93 * x ** 3 - 26.46 * x ** 2 - 16.20 * x + 76.19)

