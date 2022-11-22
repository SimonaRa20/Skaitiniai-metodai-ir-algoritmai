import numpy as np
import matplotlib.pyplot as plt

#----------Ermitodaugianariai-----------
def Hermite(X,j,x):
    N=np.size(X)
    L=Lagrange(X,j,x)
    DL=D_Lagrange(X,j,X[j])
    U=(1-2*DL*(x-X[j]))*np.square(L)
    V=(x-X[j])*np.square(L)
    return U,V

#---------Lagranzodaugianarioisvestinepagalx--------------
def D_Lagrange(X,j,x):
    N=np.size(X)
    DL=np.zeros(x.shape,dtype=np.double);#DLisraiskosskaitiklis
    for i in range(0,N):#ciklasperatmetamusnarius
        if(i==j):continue
        Lds=np.ones(x.shape,dtype=np.double)
        for k in range(0,N):
            if((k!=j)and(k!=i)):Lds=Lds*(x-X[k])
        DL=DL+Lds
        
    Ldv=np.ones(x.shape,dtype=np.double);#DLisraiskosvardiklis
    for k in range(0,N):
        if(k!=j):Ldv=Ldv*(X[j]-X[k])
    
    DL=DL/Ldv
    return DL
#--------Lagranzodaugianaris-------------
def Lagrange(X,j,x):
    N=np.size(X)
    L=np.ones(x.shape,dtype=np.double)
    for k in range(0,N):
        if(j!=k):L=L*((x-X[k])/(X[j]-X[k]))
    return L

def s(i):
    global x,yCO2emission
    n=len(x)
    if i==-1:
        return 2*s(0)-s(1)
    elif i==-2:
        return 2*s(-1)-s(0)
    elif i==n-1:
        return 2*s(n-2)-s(n-3)
    elif i==n:
        return 2*s(n-1)-s(n-2)
    else:
        return(yCO2emission[i+1]-yCO2emission[i])/(x[i+1]-x[i])
    
def w1(i):
    return np.abs(s(i+1)-s(i))

def w2(i):
    return np.abs(s(i-1)-s(i-2))

def d(i):
    W1=w1(i)
    W2=w2(i)
    
    return W1/(W1+W2)*s(i-1)+W2/(W1+W2)*s(i)

plt.grid()
yCO2emission=[516.82, 507.64, 506.03, 511.21, 504.28, 507.75, 509.04, 499.20, 492.48, 486.46, 
              468.66, 472.62, 456.72, 460.30, 461.27, 427.77, 433.22, 433.60, 436.18, 422.74,]
x=np.linspace(1,20,20)
print(x)
dy=[]

for i in range(20):
    dy.append(d(i))
    plt.scatter(x[i],yCO2emission[i],c='firebrick')
    
for i in range(1,20):
    xPlt=np.linspace(i,i+1,100)
    yPlt=np.zeros(100)
    for j in range(2):
        U,V=Hermite(x[i-1:i+1],j,xPlt)
        yPlt=yPlt+U*yCO2emission[i+j-1]+V*dy[i+j-1]
    plt.plot(xPlt,yPlt)

plt.show()