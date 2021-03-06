#!/usr/bin/python
##example2_4
import numpy as np
from LUdecomp import *

def vandermode(v):
    n=len(v)
    a=np.zeros((n,n))
    for j in range(n):
        a[:,j]=v**(n-j-1)

    return a

v= np.array([1.0, 1.2, 1.4, 1.6, 1.8, 2.0])
b= np.array([0.0, 1.0, 0.0, 1.0, 0.0,1.0])

a= vandermode(v)
aOrig=a.copy()
bOrig=b.copy()

a = LUdecomp(a)

x = LUsolve(a,b)

det = np.prod(np.diagonal(a))

print('x=\n',x)
