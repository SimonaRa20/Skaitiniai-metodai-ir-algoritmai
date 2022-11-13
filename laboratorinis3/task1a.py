import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return (np.log(x) / (np.sin(2 * x) + 1.5)) + (x / 5)

# Number of points
n = 30

# Interpolation function range
range_start = 2
range_end = 10
step_size = (range_end - range_start) / n

# X and Y values calculation
x_range = np.arange(range_start, range_end, step_size)
x_range = np.append(x_range, range_end)
y_range = [f(x) for x in x_range]

# Shows f(x) graph
plt.plot(np.arange(range_start, range_end, 0.01), [f(x) for x in np.arange(range_start, range_end, 0.01)], 'b',
         label='f(x)')
plt.scatter(x_range, y_range, color='b', label='Interpolation points')

plt.title("f(x)")
plt.xlabel('x')
plt.ylabel('y = f(x)')

plt.ylim(top=3.5, bottom=-3.5)
plt.grid(True)
plt.legend()
plt.show()