from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

np.warnings.filterwarnings('ignore')

# Shows z1 function graph
def show_z1_graph():
    fig = plt.figure()
    fig.canvas.set_window_title('Z1')
    ax = fig.gca(projection='3d')
    surf = ax.plot_surface(XX, YY, Z1, cmap=cm.coolwarm,
                           alpha=0.5)
    surfZ = ax.plot_surface(XX, YY, np.zeros(np.shape(Z1)), antialiased=False, alpha=0.2)
    cp = ax.contour(X, Y, Z1, levels=0, colors='red')
    plt.show()


# Shows z2 function graph
def show_z2_graph():
    fig = plt.figure()
    fig.canvas.set_window_title('Z2')
    ax = fig.gca(projection='3d')
    surf = ax.plot_surface(XX, YY, Z2, cmap=cm.summer,
                           antialiased=False, alpha=0.5)
    surf_z = ax.plot_surface(XX, YY, np.zeros(np.shape(Z1)), antialiased=False, alpha=0.2)
    cp = ax.contour(X, Y, Z2, levels=0, colors='green')
    plt.show()


# Solves system graphically
def show_f_roots():
    fig = plt.figure()
    fig.canvas.set_window_title('Result')
    ax = fig.gca()
    ax.grid(color='#C0C0C0', linestyle='-', linewidth=0.5)
    cp = ax.contour(X, Y, Z1, levels=0, colors='red')
    cp = ax.contour(X, Y, Z2, levels=0, colors='green')
    plt.show()


# Solves system using newton's method
def newton(x):
    ff = f(x)
    dff = df(x)
    for i in range(max_iterations):
        dff = df(x)
        delta_x, a, b, c = np.linalg.lstsq(-dff, ff)

        x1 = x.reshape(2, 1) + alpha * delta_x
        ff1 = f([x1[0, 0], x1[1, 0]])

        precision = np.linalg.norm(delta_x) / (np.linalg.norm(x) + np.linalg.norm(delta_x))
        print(f"Iteration: {i} Precision: {precision}")

        if precision < eps:
            print(f"Solution: {x}")
            return x
        elif i == max_iterations:
            print(f"Set precision not reached. Last x = {x}")
            return

        x = np.array([x1[0, 0], x1[1, 0]])
        ff = ff1



def f(x):
    return np.asmatrix([
        [8*np.cos(x[0]) + (x[1])**2],
        [50*np.e**(-((x[0]**2)/4) + x[1]**2) +x[0] + x[1] - 5.5]
    ])


def df(x):
    return np.asmatrix([
        [-8*np.sin(x[0]), 2 * x[1]],
        [1-25*x[0]*np.e**(x[1]**2 - (x[0]**2 / 4)), 100*x[0]*np.e**(x[0]**2 - (x[1]**2 / 4)) + 1]
    ])

# Used for showing graphs
X = np.arange(-3, 3, 0.25)
Y = np.arange(-3, 3, 0.25)
XX, YY = np.meshgrid(X, Y)

Z1 = 8*np.cos(XX) + YY**2
Z2 = 50* np.e**(-((XX**2)/4) + YY) +XX + YY - 5.5

show_z1_graph()
show_z2_graph()

show_f_roots()

alpha = 1
max_iterations = 200
eps = 1e-10
initial_x = np.array([1, 1])  # Initial guess

# Solves system and checks with f function
result = newton(initial_x)
print(f(result))
