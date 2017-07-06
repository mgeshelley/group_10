#!/usr/bin/env python

import numpy as np


# Read in Z,A,N from 'aud16.dat'
isotopes = np.genfromtxt('aud16.dat',skip_header=2, usecols=(0,1,5))
"""
Columns are:
    0: Z
    1: A
    2: N
"""

# Read in binding energies from 'aud16.dat' into separate array
bind_energies = np.genfromtxt('aud16.dat',skip_header=2, usecols=2)


for i in range(0,len(isotopes)):
    # Only check if isotope has > 2 protons
    if isotopes[i,0] <= 2:
        continue

    z = isotopes[i,0]
    a = isotopes[i,1]
    n = isotopes[i,2]


    # Skip if there isn't a measured isotope with 2 fewer protons
    if len(p2_isotope[0]) == 0:
        continue

    # Check if unbound to 2p-decay
    p2_isotope = np.where((isotopes[:,0] == z-2) & (isotopes[:,2] == n))
    # If B.E. of isotope with 2 fewer protons is smaller, skip
    if bind_energies[p2_isotope] - bind_energies[i] < 0:
        continue

    ## Check if bound to 1p-decay
    p1_isotope = np.where((isotopes[:,0] == z-1) & (isotopes[:,2] == n))
    # If B.E. of isotope with 1 fewer protons is smaller, print
    if bind_energies[p1_isotope] - bind_energies[i] < 0:
        print z,n,a
