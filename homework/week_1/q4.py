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

# Empty lists to store the energy and mass number of the states that has both a 6+ and a 8+ state
e_state_six = []
e_state_eight = []
mass_nr = []
z_number = []

# Here we search for the states that includes both 6+ and 8+ states and stores the values of those states
for i in range(len(j_pi_info)):
    if j_pi_info[i] == '6+':

        nucleus = isotopes[i]
        A = isotopes[i,0]
        Z = isotopes[i,1]

        #for n in range()
        n = i
        step_out = 0
        while step_out == 0:


            if j_pi_info[n] == '8+':
                e_state_six.append(energy[i])
                e_state_eight.append(energy[n])
                mass_nr.append(isotopes[n,0])
                z_number.append(isotopes[n,1])
                step_out = 1

            if isotopes[n,0] != A:
                step_out = 1
            if isotopes[n,1] != Z:
                step_out = 1
            n += 1

# The ratio of the energy of the states 8+/6+
e_ratio = np.array(e_state_eight)/np.array(e_state_six)

N = mass_nr - np.array(z_number)

# Plotting the ratio against the proton nr + the lines at y=[12/2, 1]

#plt.plot(mass_nr, e_ratio, 'x')
plt.plot(z_number, e_ratio, 'x')
plt.plot(z_number, (12./7.)*np.ones(len(z_number)))
plt.plot(z_number, np.ones(len(z_number)))

# These statements makes a pretty plot:
plt.xlabel('Neutron nr')
plt.ylabel('Energy ratio of spins 8+/6+')
plt.legend(['Ratio', '12/7', '1'])
plt.title('Question 4, HW1')

# This statement shows the plot, but you can also save the figure directly with savefig('filename'):
plt.show()

