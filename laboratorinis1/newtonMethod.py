
import math
import skenavimoAlgoritmas as funkcija
import skenavimoAlgoritmas as intervalas


def discrete_method_approx(f, x, h=.001):
    return (f(x + h) - f(x)) / h


def NewtonsMethod(f, x, tolerance=.001):
    count = 0
    while abs(f(x)) > tolerance:
        df = discrete_method_approx(f,x)
        x = x - f(x) / df
        count += 1
    return x, count


f = lambda x: 1.35 * x ** 4 + 0.93 * x ** 3 - 26.46 * x ** 2 - 16.20 * x + 76.19
start = 1 + (26.46 / 1.35)
end = 1 + math.sqrt(26.46 / 1.35)
intervalai = intervalas.getInterval(-start, end);
print('-' * 105)
print("|  {0:^44}  |  {1:^25}  |  {2:^20}  |".format('Intervalas','Iteraciju skaicius','Gautoji saknis'))
print('-' * 105)
for interval in intervalai:
    x0, count = NewtonsMethod(f, interval[0])
    intervalStart = interval[0]
    intervalEnd = interval[1]
    print("|  [{0:^20}, {1:^20}]  |  {2:^25}  |  {3:^20}  |".format(intervalStart, intervalEnd, count, x0))
print('-' * 105)



# root = NewtonsMethod(f, interval[3][0])
# print(root)
# x0 = NewtonsMethod(3, 1.0e-6)

# print('x: ', -10)
# print('x0: ', x0)
# print("f(x0) = ", 1.35 * x0 ** 4 + 0.93 * x0 ** 3 - 26.46 * x0 ** 2 - 16.20 * x0 + 76.19)

