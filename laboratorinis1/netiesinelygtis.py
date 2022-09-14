import math

import matplotlib.pyplot as plt
import numpy as np
from math import *
from scipy.optimize import fsolve

def f(m):
    return float(80 * math.pow(math.e, (-0.1 * 4) / m)) + (((9.8 * m) / 0.1) * (math.pow(math.e, (-0.1 * 4) / m) - 1)) - 21

m = np.arange(-100,100,0.01)

##skenavimo su mazejanciu zingsniu algoritmas

iteration = 0
iter_max = 1000

found = False
alpha = 0.01
beta = alpha/2
x0 = 4.03
x1 = x0 + alpha
count = 0

print("Iteracija      Intervalas             F(x) reiksme")

while(iteration <=iter_max and x0< 4.04):
# Randam intervala kur saknis
  if(f(x0) >= 0 and f(x1) <= 0 or f(x0) <= 0 and f(x1) >= 0 ):
    found = True
    print("rasta saknis yra intervale ({0:7.9f} ; {1:7.9f})".format(x0,x1))
    step = alpha/10
    s0=x0
    s1=s0+step
    while(iteration < iter_max and abs(f(s0))>=1e-11 and s1<=x1):
      print("{0:3d}      |  {1:7.9f}  -  {2:7.9f} |  {3:.10e}".format(iteration,s0,s1,abs(f(s0))))
      #jeigu keicia zenkla
      if(f(s0) >= 0 and f(s1) <= 0 or f(s0) <= 0 and f(s1) >= 0 ):
        #pranesame, jog radome sakni intervale (s0 ; s1) ir maziname zingsni
        print("patikslinus, saknis yra intervale ({0:7.8f} ; {1:7.8f}) | {2:.10e}".format(s0,s1, abs(f(s0))))
        #s0 nesikeicia, o s1 patoliname nuo s0 per sumazinta zingsni
        step= step/10
        s1=s0+step
      #Jei ne, tikriname kita intervala
      else:
        s0+=step
        s1+=step
      #Skaiciuojam kaip dar viena iteracija
      iteration+=1

  iteration +=1
  x0=x1
  x1 +=alpha
  print("{0:3d}      |  {1:7.6f}  -  {2:7.6f} |  {3:.10e}".format(iteration,x0,x1,f(x0)))
plt.plot(m,f(m))
plt.grid()
plt.show()