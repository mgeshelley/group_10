# testing ideas

import numpy as np
import sys


states_matrix = np.genfromtxt('table_files/sd_mscheme.int', skip_header=3, usecols=(0,1,2,3), dtype='str')
energies = np.genfromtxt('table_files/sd_mscheme.int', usecols=(4), skip_header=3)

N = np.genfromtxt('table_files/sd_mscheme.int', skip_header=2, usecols=(0), max_rows=1, dtype='int') #=len(states_matrix)

####

states_listed = np.zeros([N,4])


### TESTING
state = [ 1.,   2.,   1.,   2.]

counter = 0
for i in range(N):
    states_listed[i] = states_matrix[i,:]
    idea = state-states_listed[i] #if the states are equal this should be [0,0,0,0]
    if np.array_equiv(idea, [0,0,0,0]):
        e_state = energies[i]
        counter +=1
    if counter >= 2:
        sys.exit("Too many energies found! There must be states that are equal (not allowed).")


print 'test state: ', state
print 'energy found for test state:', e_state

print '\nlist of states: '
print states_listed[:5]
print '\nenergies: '
print energies[:5]
print '\nold matrix: '
print states_matrix[:5,:]



