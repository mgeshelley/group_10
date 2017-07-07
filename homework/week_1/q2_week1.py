# program to solve A. Brown's homework q2 week1
# this program calculate the neutron dripline using the 
# liquid-drop model (LDM)
import math
# parameters given in Brown's notes
a1 = 15.49
a2 = 17.23
a3 = 0.697
a4 = 22.6 
# input data
Zmin = 36
Zmax = 44
#
print '--------------------------------'
print 'driplines from liquid-drop model'
print '  Z   N    A     BE/A '
# loop over Z
for Z in range(Zmin, Zmax+1,1):
    N = Z
    drip = 0
    while drip == 0:
        A = N+Z
        BE = a1*A-a2*A**(2./3)-a3*Z**2/A**(1./3)-a4/A*(N-Z)**2  # binding energy defined > 0 for bound nuclei
        if BE > 0: 
             N = N+1
             drip = 0
        else: # BE < 0 i.e. unbound nuclei
             A = A-1 # identify the last bound A
             N = N-1 # identify the last bound N
             BE = a1*A-a2*A**(2./3)-a3*Z**2/A**(1./3)-a4/A*(N-Z)**2 # calculate the binding energy of the last bound 
             print '%3d %4d %4d %7.3f' % (Z, A-Z, A, BE/A)
             drip = 1
    #end while 
#end for
print '--------------------------------'
#the results is benchmarked with https://upload.wikimedia.org/wikipedia/commons/3/3b/Bethe-Weizs%C3%A4cker.png for Z=25
