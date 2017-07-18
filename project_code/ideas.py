# testing ideas

import numpy as np
import sys

def find_energy(state, states_matrix, energies):
    N = np.shape(states_matrix)[0]
    states_listed = np.zeros([N,4])
    counter = 0
    for i in range(N):
        states_listed[i] = states_matrix[i,:]
        idea = state-states_listed[i] #if the states are equal this should be [0,0,0,0]
        if np.array_equiv(idea, [0,0,0,0]):
            e_state = energies[i]
            counter +=1
        if counter >= 2:
            sys.exit("Too many energies found! There must be states that are equal (not allowed).")
    return e_state, states_listed


states_matrix = np.genfromtxt('table_files/sd_mscheme.int', skip_header=3, usecols=(0,1,2,3), dtype='str')
energies = np.genfromtxt('table_files/sd_mscheme.int', usecols=(4), skip_header=3)

#N = np.genfromtxt('table_files/sd_mscheme.int', skip_header=2, usecols=(0), max_rows=1, dtype='int') #=len(states_matrix)


### TESTING
state = [ 1.,   2.,   1.,   2.]

energy_state, states_listed = find_energy(state, states_matrix, energies)

print 'test state: ', state
print 'energy found for test state:', energy_state

print '\nlist of states: '
print states_listed[:5]
print '\nenergies: '
print energies[:5]





