import numpy as np


A=np.matrix([[4, 12, 1, 7],
             [2, 6, 17, 2],
             [2, 1, 5, 1],
             [5, 11, 7, 0]]).astype(np.float_)
b=(np.matrix([171,75,30,50])).transpose().astype(np.float_)
n=(np.shape(A))[0]
nb=(np.shape(b))[1]

A1=np.hstack((A,b))

# tiesioginis etapas(atspindziai):
for i in range (0,n-1):
    z=A1[i:n,i]
    zp=np.zeros(np.shape(z)); zp[0]=np.linalg.norm(z)
    omega=z-zp; omega=omega/np.linalg.norm(omega)
    Q=np.identity(n-i)-2*omega*omega.transpose()
    A1[i:n,:]=Q.dot(A1[i:n,:])
    # atgalinis etapas:
x=np.zeros(shape=(n,nb))
for i in range (n-1,-1,-1):    # range pradeda n-1 ir baigia 0 (trecias parametras yra zingsnis)
    x[i,:]=(A1[i,n:n+nb]-A1[i,i+1:n]*x[i+1:n,:])/A1[i,i]


print("x1\t\t\t\t\t\tx2\t\t\t\t\t\tx3\t\tx4")
for i in range(4):

    # Lower
    for j in range(1):
        print(x[i][j], end="\t")
    print("", end="\t")

