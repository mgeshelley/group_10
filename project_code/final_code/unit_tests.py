# Unit tests (so far for the pairing problem)

# Importing the files containing the needed functions (that we wrote our selves)
from create_table_files import *
from read_files import *
from ham import *
from input_func import *

import os.path

import numpy as np
import sys


def unit_test_hamiltonian_pairing():
    """
    This function tests that the hamiltonian matrix is set up correctly by checking
    if it is equal to the analytical hamiltonian matrix for the pairing problem.
    If the matrix is not set up correctly an error message is printed out and the 
    program is stopped. 


    Returns (nothing)

    """
    N_Utest = 4

    # numerical hamiltonian

    sp_basis_filename_Utest = 'table_files/3s_mscheme.sp'
    SD_filename_Utest = 'table_files/3s_pairing.sd'
    tbme_filename_Utest = 'table_files/pairing_g1.int'
    restriction_Utest = 'pair'
    g_Utest = 1
    # read sp_basis from file .sp
    sp_matrix_Utest = read_sd_basis(sp_basis_filename_Utest)
    nr_sp_states_Utest = np.shape(sp_matrix_Utest)[0]

    create_SD_perm(N_Utest, nr_sp_states_Utest, sp_matrix_Utest, SD_filename_Utest, restriction_Utest)

    # Read in the SD from files:
    SlaterD_matrix_Utest = read_SD(N_Utest, SD_filename_Utest)
    nr_SD_Utest = SlaterD_matrix_Utest.shape[0]


    # Creating the file containing the pairing interaction:
    if os.path.isfile(tbme_filename_Utest) == False:
        create_tbme_pairing(tbme_filename_Utest,nr_sp_states_Utest,g_Utest)
    #print g

    numerical_hamiltonian = np.zeros((nr_SD_Utest, nr_SD_Utest))
    numerical_hamiltonian_1body = np.zeros((nr_SD_Utest, nr_SD_Utest))
    numerical_hamiltonian_2body = np.zeros((nr_SD_Utest, nr_SD_Utest))
    numerical_hamiltonian_1body = Hamiltonian_one_body(N_Utest, nr_sp_states_Utest, sp_matrix_Utest, SD_filename_Utest)
    numerical_hamiltonian_2body = Hamiltonian_two_body(N_Utest, nr_sp_states_Utest, SD_filename_Utest, tbme_filename_Utest, 'pairing')

    numerical_hamiltonian = numerical_hamiltonian_1body+numerical_hamiltonian_2body

    #analytical hamiltonian

    dim = 6

    analytical_hamiltonian = -g_Utest/2.*np.ones([dim,dim])
    np.fill_diagonal(analytical_hamiltonian, 2.-2.*g_Utest/2.)
    np.fill_diagonal(np.rot90(analytical_hamiltonian), 0)

    for n in range(dim):
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
        print "UNIT TEST COMPLETED: Hamiltonian matrix set up correctly.\n"

