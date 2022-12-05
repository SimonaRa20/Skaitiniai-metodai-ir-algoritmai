import matplotlib.pyplot as plt
import numpy as np

yCO2emission=np.array([516.82, 507.64, 506.03, 511.21, 504.28, 507.75, 509.04, 499.20, 492.48, 486.46, 
              468.66, 472.62, 456.72, 460.30, 461.27, 427.77, 433.22, 433.60, 436.18, 422.74,])
x=np.linspace(1,20,20)
plt.plot(x,yCO2emission,'ro')
n=len(x)
m=5 # keisti norint gauti aproksimuojančias skirtingas daugianario kreives
BaseMatrix=np.zeros((n,m))
for i in range(n):
    for j in range(m):
        BaseMatrix[i,j]=x[i]**j
        
koef=np.linalg.solve(BaseMatrix.T@BaseMatrix,BaseMatrix.T@yCO2emission)

xxx=np.arange(min(x)-1,max(x)+1,0.1)
yyy=np.zeros_like(xxx)
func=''
for i in range(m):
    yyy+=koef[i]*xxx**i
    func+=str(np.round(koef[i],2))+'x^'+str(i)+'+'
print(func)
plt.plot(xxx,yyy,'b-',linewidth=3)
plt.title("Prancūzijos šiltnamio dujų emisijos grafikas (aproksimavimas)")
plt.xlabel('x')
plt.ylabel('y')
plt.show()