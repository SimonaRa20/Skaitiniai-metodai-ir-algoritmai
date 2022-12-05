import numpy as np
import matplotlib.pyplot as plt

def chebyshev_polynomial(x,n):
    T=[1,x]
    for i in range(n-2):
        T.append(2*x*T[i+1]-T[i])
    return T 

def calculate_coeficients(X,Y):
    T=np.matrix([chebyshev_polynomial(x,len(X))for x in X])
    print(np.shape(T))
    T_inv=np.linalg.inv(T)
    print(np.shape(T))
    return T_inv@Y

def eval(X,n,a):
    T=np.matrix([chebyshev_polynomial(x,n)for x in X])
    yval=T@a
    print(np.shape(T))
    return yval.A1

f=lambda x:(np.log(x) / (np.sin(2 * x) + 1.5)) + (x / 5)

yCO2emission=np.array([516.82, 507.64, 506.03, 511.21, 504.28, 507.75, 509.04, 499.20, 492.48, 486.46, 
                       468.66, 472.62, 456.72, 460.30, 461.27, 427.77, 433.22, 433.60, 436.18, 422.74,])

interval=(1,20)
n=20
X=np.linspace(*interval,20)
a=calculate_coeficients(X,yCO2emission).T
smooth=np.linspace(*interval,100)
yval=eval(smooth,n,a)
print(np.shape(yval))
plt.plot(smooth,yval)
plt.scatter(X,yCO2emission,c='firebrick')
plt.title("Prancūzijos šiltnamio dujų emisijos grafikas (daugianario)")
plt.xlabel('x')
plt.ylabel('y')
plt.show()