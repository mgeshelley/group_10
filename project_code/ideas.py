# testing ideas


import numpy as np
import sys


states_matrix = np.genfromtxt('table_files/sd_mscheme.int', skip_header=2, usecols=(0,1,2,3), dtype='str')
energies = np.genfromtxt('table_files/sd_mscheme.int', usecols=(4), skip_header=2)

N = np.genfromtxt('table_files/sd_mscheme.int', skip_header=1, usecols=(0), max_rows=1, dtype='int') #=len(states_matrix)

####

states_listed = np.zeros([N,4])

for i in range(N):
    states_listed[i] = states_matrix[i,:]


### TESTING
state = [ 1.,   2.,   1.,   2.]


#print np.equal(states_listed, state)

for i in range(N):
    print np.array_equiv(states_listed[i],state)
    e_state = np.extract(np.array_equiv(states_listed[i],state), energies)


#e_state = np.where(np.array_equiv(states_listed,state), energies, 0)

print 'test state: ', state
print 'energy found for test state:', e_state

print '\nlist of states: '
print states_listed[:5]
print '\nenergies: '
print energies[:5]
print '\nold matrix: '
print states_matrix[:5,:]




#if 1245. in states_listed:
#    print 'hello'

#print states_listed.index('1245.')
#e_state = np.where(states_listed==state, energies, 0) # when condition true gives energies, else returns 0



