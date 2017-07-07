# commented
import math
# from math import sqrt, exp, log, sin
# from math import *
# import math as m
# m is now the name of the math module
#from math import sin as s, cos as c, log as ln
#import numpy as np

a1 = 15.49
a2 = 17.23
a3 = 0.697
a4 = 22.6

Zmin = 36
Zmax = 44

Z = Zmin
print 'driplines from liquid-drop model'
print '    Z     N     A     BE/A '
while Z <= Zmax:
    N = Z
    drip = 0
    while drip == 0:
        A = N+Z
        BE = a1*A-a2*A**(1./3)-a3*Z**2*A**(-1./3)-a4*(N-Z)**2/A # binding energy defined > 0 for bound nuclei
        if BE > 0: 
             N = N+1
             drip = 0
        else: # BE < 0 i.e. unbound nuclei
             C = A-1 # identify the previous A
             N = N-1 # identify the previous N
             BE = a1*A-a2*A**(1./3)-a3*Z**2*A**(-1./3)-a4*(N-Z)**2/A 
             print '%5d %5d %5d %.3f' % (Z, A-Z, A, BE/A)
             Z = Z+1
             drip = 1
    #end while 
#end while

