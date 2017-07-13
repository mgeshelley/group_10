# Unit tests

import numpy as np
import sys

def unit_test_hamiltonian_pairing(numerical_hamiltonian, g):
    """
    This function tests that the hamiltonian matrix is set up correctly by checking
    if it is equal to the analytical hamiltonian matrix for the pairing problem.
    If the matrix is not set up correctly an error message is printed out and the 
    program is stopped. 

    Input 

    numerical_hamiltonian:  ndarray,
                            the hamiltonian matrix to be tested
    g:                      float, 
                            the pairing constant

    Returns (nothing)

    """

    N = 6

    analytical_hamiltonian = -g*np.ones([N,N])
    np.fill_diagonal(analytical_hamiltonian, 2.-2.*g)
    np.fill_diagonal(np.rot90(analytical_hamiltonian), 0)

    for n in range(N):
        analytical_hamiltonian[n,n] += 2*n

    for m in range(5,2,-1):
        analytical_hamiltonian[m,m] = analytical_hamiltonian[m-1,m-1]

    unit_test = np.array_equal(numerical_hamiltonian, analytical_hamiltonian)

    if not unit_test:
        print "\nERROR IN UNIT TEST: The numerical and analytical hamiltonian matrix are not equal!"
        print 'The numerical hamiltonian matrix:'
        print numerical_hamiltonian
        print 'The analytical hamiltonian matrix:'
        print analytical_hamiltonian
        sys.exit()
        
    if unit_test:
        print "\nSUCCESS: The hamiltonian matrix was set up corectly (for the pairing problem).\n"



# To test the unit test
"""
test_ham = np.array([[  2.,   0.,   0.,   0.,   0.,   0.],
        [  0.,   4.   ,0.,   0.,   0.,   0.],
        [  0.,   0.   ,6. ,  0.,   0.,   0.],
        [  0.,   0.  , 0.  , 6.,   0.,   0.],
        [  0.,   0. ,  0.   ,0.,   8.,   0.],
        [  0.,   0.,   0.   ,0.,   0.,  10.]])

unit_test_hamiltonian_pairing(test_ham,0)

"""

