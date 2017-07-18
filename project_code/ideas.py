# testing ideas

import numpy as np
import sys

def find_energy(state, states_matrix, energies):
    N = np.shape(states_matrix)[0]
    states_listed = np.zeros([N,4])

    e_state = "No state found!" #as initial value, could be set to None
    counter = 0
    for i in range(N):
        idea = states_matrix[i,:] - state #if the states are equal this should be [0,0,0,0]
        if np.array_equiv(idea, [0,0,0,0]):
            e_state = energies[i]
            counter +=1
        elif counter >= 2:
            sys.exit("Too many energies found! There must be states that are equal (not allowed).")
            
    return e_state


# Reading in from file, this can also be done inside the function
states_matrix = np.genfromtxt('table_files/sd_mscheme.int', skip_header=3, usecols=(0,1,2,3))
energies = np.genfromtxt('table_files/sd_mscheme.int', usecols=(4), skip_header=3)


### TESTING
state = [ 1., 2., 4., 5.]
energy_state = find_energy(state, states_matrix, energies)

print 'Test state: ', state
print 'Energy found for test state:', energy_state

print '\nList of states: '
print states_matrix[:5,:]
print '\nEnergies: '
print energies[:5]





