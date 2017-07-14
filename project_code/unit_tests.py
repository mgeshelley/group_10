# Unit tests (so far for the pairing problem)

import numpy as np
import sys

def unit_test_hamiltonian_pairing(N_particles, g, numerical_hamiltonian):
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
        print "\nERROR IN UNIT TEST: The numerical and analytical hamiltonian matrix are not equal!\n"
        print 'The numerical hamiltonian matrix (shape):'
        print np.shape(numerical_hamiltonian)
        print numerical_hamiltonian
        print '\n'
        print 'The analytical hamiltonian matrix (shape):'
        print np.shape(numerical_hamiltonian)
        print analytical_hamiltonian
        print '\n'
        sys.exit()
        
    if unit_test:
        print "\nUNIT TEST SUCCESS: The hamiltonian matrix was set up correctly (for the pairing problem).\n"


##############################################################
# To test the unit test:
##############################################################

"""
N_particles = 4
g = 0

folder_name = 'table_files/'
SD_filename = folder_name+"3s_slater_det.sd"
tbme_filename = folder_name+"pairing_g%s.int" %(g)


test_ham = Hamiltonian_one_body(N_particles, 8, SD_filename, tbme_filename)

unit_test_hamiltonian_pairing(N_particles, g, test_ham)

"""
