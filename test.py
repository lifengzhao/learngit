import os,sys
from math import sqrt

def dist(x0, x1):
    res = 0.
    for i in range(3):
        dx = x1[i]-x0[i]
        res += dx*dx
    return sqrt(res)
