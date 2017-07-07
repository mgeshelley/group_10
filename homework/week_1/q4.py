#!/usr/bin/env python

import numpy as np
import sys

# Read in Z,A,N from 'toiee.dat'
isotopes = np.genfromtxt('toiee.dat',skip_header=1, usecols=(1,2,5))
"""
Columns are:
    0: A
    1: Z
    2: N
"""
#print 'isotopes', isotopes[0:3]


# Read in spin from 'toiee.dat' into separate array
j_pi_info = np.genfromtxt('toiee.dat',skip_header=1, usecols=(7), dtype='string')
energy = np.genfromtxt('toiee.dat',skip_header=1, usecols=(6))

step_out = 0
for i in range(len(j_pi_info)):

    if j_pi_info[i] == '6+':

        nucleus = isotopes[i]
        A = isotopes[i,0]
        
        Z = isotopes[i,1]

        #for n in range(i,len(j_pi_info)):
        n = i
        while step_out == 0:

            if j_pi_info[n] == '8+':
                print nucleus
                sys.exit()
                step_out = 1

            if isotopes[n,0] != A:
                print 'hola'
                step_out = 1
            if isotopes[n,1] != Z:
                print 'hola2'
                step_out = 1

            n += 1

           






#print j_pi_info

"""

for i in range(0,len(isotopes)):
    # Only check if isotope has > 2 protons
    if isotopes[i,0] <= 2:
        continue

    z = isotopes[i,0]
    a = isotopes[i,1]
    n = isotopes[i,2]

    # Check if unbound to 2p-decay
    p2_isotope = np.where((isotopes[:,0] == z-2) & (isotopes[:,2] == n))

    # Skip if there isn't a measured isotope with 2 fewer protons
    if len(p2_isotope[0]) == 0:
        continue

    # If B.E. of isotope with 2 fewer protons is smaller, skip
    if bind_energies[p2_isotope] - bind_energies[i] < 0:
        continue

    ## Check if bound to 1p-decay
    p1_isotope = np.where((isotopes[:,0] == z-1) & (isotopes[:,2] == n))
    # If B.E. of isotope with 1 fewer protons is smaller, print
    if bind_energies[p1_isotope] - bind_energies[i] < 0:
        print z,n,a
"""