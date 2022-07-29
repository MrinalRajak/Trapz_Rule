

#Trapezoidal Rule(Discrete data points)

import numpy as np
from scipy.integrate import trapz


xs=np.array([1.2,1.3,1.4,1.5,1.6])
ys=np.array([2.0333,2.0692,2.1143,2.1667,2.2250])
n=len(xs)
h=(xs[1]-xs[0])
i=(h/2)*(ys[0]+ys[-1]+2*np.sum(ys[1:-1:1]))
print ("Trapezoidal Rule integrated Result: ",i)
print ("Scipy based Trapezoidal integrated Result: ",trapz(ys,dx=h))
