#!/usr/bin/env python

import numpy as np


# Read in Z,N,A from 'rms13.dat'
isotopes = np.genfromtxt('rms13.dat',skip_header=2, usecols=(0,1,2))
"""
Columns are:
    0: Z
    1: N
    2: A
"""

# Read in binding energies from 'rms13.dat' into separate array
rms = np.genfromtxt('rms13.dat',skip_header=2, usecols=3)


for i in range(0,len(isotopes)):
    # Only check if isotope has > 1 neutron
    if isotopes[i,1] <= 1:
        continue

    z = isotopes[i,0]
    n = isotopes[i,1]
    a = isotopes[i,2]

    # Find location of isotope with n = n-1
    n_1_isotope = np.where((isotopes[:,1] == n-1) & (isotopes[:,0] == z))

    # Skip if there isn't a measured isotope with 1 fewer neutron
    if len(n_1_isotope[0]) == 0:
        continue

    # Calculate difference
    difference = rms[i] - rms[n_1_isotope]

    # Print difference between isotope with N and N-1
    print n, difference [0]
