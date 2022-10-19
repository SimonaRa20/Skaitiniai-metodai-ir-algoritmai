import numpy as np
import matplotlib.pyplot as plt

import math

def Pavirsius(X,Y,LFF):
    siz=np.shape(X)
    Z=np.zeros(shape=(siz[0],siz[1],2))
    for i in range (0,siz[0]):
        for j in range (0,siz[1]):  Z[i,j,:]=LFF([X[i][j],Y[i][j]]).transpose();
    return Z

# -------- Lygciu sistemos funkcija---------
def LF(x):  # grazina reiksmiu stulpeli
    s = np.matrix([[8* math.cos(x[0]) + x[1]**2], [50 * math.e**(-((x[0])**2/4) + x[1]**2) +x[0]+x[1] - 5.5]])
    return s

# ----------------------------------

fig1 = plt.figure(1, figsize=plt.figaspect(0.5));
ax1 = fig1.add_subplot(1, 2, 1, projection='3d');
ax1.set_xlabel('x');
ax1.set_ylabel('y');
ax1.set_ylabel('z')
ax2 = fig1.add_subplot(1, 2, 2, projection='3d');
ax2.set_xlabel('x');
ax2.set_ylabel('y');
ax2.set_ylabel('z')
# plt.draw();  #plt.pause(1);
xx = np.linspace(-3, 3, 50);
yy = np.linspace(-3, 3, 50);
X, Y = np.meshgrid(xx, yy);
Z = Pavirsius(X, Y, LF)

surf1 = ax1.plot_surface(X, Y, Z[:, :, 0], color='blue', alpha=0.4)
wire1 = ax1.plot_wireframe(X, Y, Z[:, :, 0], color='black', alpha=1, linewidth=0.3, antialiased=True)
surf2 = ax1.plot_surface(X, Y, Z[:, :, 1], color='purple', alpha=0.4)
wire2 = ax1.plot_wireframe(X, Y, Z[:, :, 1], color='black', alpha=1, linewidth=0.3, antialiased=True)
CS11 = ax1.contour(X, Y, Z[:, :, 0], [0], colors='b')
CS12 = ax1.contour(X, Y, Z[:, :, 1], [0], colors='g')
CS1 = ax2.contour(X, Y, Z[:, :, 0], [0], colors='b')
CS2 = ax2.contour(X, Y, Z[:, :, 1], [0], colors='g')

XX = np.linspace(-5, 5, 2);
YY = XX;
XX, YY = np.meshgrid(XX, YY);
ZZ = XX * 0
zeroplane = ax2.plot_surface(XX, YY, ZZ, color='gray', alpha=0.4, linewidth=0, antialiased=True)

plt.show()