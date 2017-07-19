# testing ideas

import numpy as np
import sys
import matplotlib.pyplot as plt


a = np.array([[1,2], [2,3]])
a = np.array([1,2])
print a[0,1:]

"""
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
            #sys.exit("Too many energies found! There must be states that are equal (not allowed).")
            break # no need to keep on looping when the state is found! (as long as we are sure there is no error and multiple states exist)
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

"""




"""
state_1 = [1, 2, 3, 4, 5]

state_2 = [2, 3, 4, 5, 6]


diff = [x for x in state_2 if x not in state_1]
print diff 

same = [x for x in state_1 if x in state_2]
print same 


"""




#noe = list(set(state_1) & set(state_2))
#print noe
#print state_1.remove(noe)




#print np.equal(state_1,state_2)



#noe = state_1[0] ^ state_2[0]
#print noe

#inex_diff = np.nonzero(noe)[0]


"""
print "state_2 - state_2"
print noe

print "\nIndices that differ:"
print inex_diff

print "\nElements from state_1 that differ"
print state_1[inex_diff]

print "\nElements from state_2 that differ"
print state_2[inex_diff]

"""












