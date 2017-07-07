#!/usr/bin/env python

import numpy as np
import sys
import matplotlib.pyplot as plt

# Read in Z,A,N from 'toiee.dat'
isotopes = np.genfromtxt('toiee.dat',skip_header=1, usecols=(1,2))
"""
Columns are:
    0: A
    1: Z
"""

# Read in spin and energy from 'toiee.dat' into separate 1-d array
j_pi_info = np.genfromtxt('toiee.dat',skip_header=1, usecols=(7), dtype='string')
energy = np.genfromtxt('toiee.dat',skip_header=1, usecols=(6))

# Empty lists to store the energy of the 
e_state_six = []
e_state_eight = []
mass_nr = []

for i in range(len(j_pi_info)):
    if j_pi_info[i] == '6+':

        nucleus = isotopes[i]
        A = isotopes[i,0]
        Z = isotopes[i,1]

        n = i
        step_out = 0
        while step_out == 0:

            if j_pi_info[n] == '8+':
                e_state_six.append(energy[i])
                e_state_eight.append(energy[n])
                mass_nr.append(isotopes[n,0])
                step_out = 1

            if isotopes[n,0] != A:
                #print 'hola'
                step_out = 1
            if isotopes[n,1] != Z:
                #print 'hola2'
                step_out = 1

            n += 1

e_ratio = np.array(e_state_eight)/np.array(e_state_six)

plt.plot(mass_nr, e_ratio, 'x')
plt.plot(mass_nr, (12./7.)*np.ones(len(mass_nr)))
plt.plot(mass_nr, np.ones(len(mass_nr)))
plt.xlabel('Mass nr A')
plt.ylabel('Spin ratio 8+/6+')
plt.legend(['Ratio', '1', '12/7'])
plt.title('Question 4, HW1')

plt.show()

