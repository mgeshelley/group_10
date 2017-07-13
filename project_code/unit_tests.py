# Unit tests (so far for the pairing problem)

import numpy as np
import sys



def Hamiltonian_one_body(N_particles, nr_sp_states, SD_filename, tbme_filename):
    """
    This function builds the one-body part of the Hamiltonian <beta_SD|H|alpha_SD>

    To call it
    Hamiltonian_one_body(N_particles, nr_sp_states, SD_filename, tbme_filename) 

    Input   

    N_particles:    float,
                    number of particles
    nr_sp_states:   float,  
                    the total number of single-particle states 
    SD_filename:    string,
                    filename of the file with the Slater Determinants
    tbme_filename:  string,
                    filename of the file with the interaction .int

    Output 
    
    hamiltonian:    ndarray,
                    Hamiltonian matrix with the one-body interaction terms
    """

    # The file with Slater Determinants (s_d) is loaded [index, sp states]
    s_d = np.loadtxt(SD_filename, comments = "!", skiprows=0)
    # number of Slater determinants
    nr_sd = s_d.shape[0]

    # Read the single-particle energies from the first line of .int file 
    sp_energies = np.genfromtxt(tbme_filename, comments = "!", skip_header=2, max_rows=1)[1:5]  

    # Make a matrix with the single-particle energies on the diagonal <p|h_1body|q>
    H_diag = np.zeros((nr_sp_states, nr_sp_states))
    for i in range(nr_sp_states):
        H_diag[i,i] = sp_energies[i/2] #this is an integer division 

    # initialize to zero the Hamiltonian <beta_SD|H|alpha_SD>
    hamiltonian = np.zeros((nr_sd, nr_sd))

    # loop over <beta_SD|
    for beta in range(0, nr_sd, 1):

        beta_list = s_d[beta,1:]
        # loop over |alpha_SD>
        for alpha in range(0, nr_sd, 1):
            
            # sum_p,q <p|h_1body|q> a_p^+ a_q
            for p in range(1,nr_sp_states+1):
                for q in range(1,nr_sp_states+1):

                    alpha_list = s_d[alpha,1:]
                    # index = -1 means not index found

                    # this part substitutes a_p^+ with a_i^+ if q == i, producing |alpha'_SD> 
                    # if it does not exist i that is equal to q, the code executes continue
                    index = -1
                    index_bol = True
                    i = 0 # variable to count the position in alpha_list 
                
                    while index_bol and i < N_particles:
                
                        if q == int(alpha_list[i]):
                            index = i
                            index_bol = False
                        else:
                            i += 1
                
                    if index < 0:
                        continue

                    alpha_list = np.insert(alpha_list,index,p)
                    alpha_list = np.delete(alpha_list,index+1)
                    alpha_list = np.sort(alpha_list)

                    # if <beta|alpha'> = 1 the matrix element H_diag(p,q) is added to the Hamiltonian matrix
                    if np.array_equal(beta_list,alpha_list):
                        hamiltonian[beta, alpha] = hamiltonian[beta, alpha] + H_diag[p-1,q-1]
    # print the Hamiltonian matrix
    # print hamiltonian
    return hamiltonian





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
        print "\nERROR IN UNIT TEST: The numerical and analytical hamiltonian matrix are not equal!"
        print 'The numerical hamiltonian matrix (shape):'
        print np.shape(numerical_hamiltonian)
        print numerical_hamiltonian
        print 'The analytical hamiltonian matrix (shape):'
        print np.shape(numerical_hamiltonian)
        print analytical_hamiltonian
        sys.exit()
        
    if unit_test:
        print "\nSUCCESS: The hamiltonian matrix was set up correctly (for the pairing problem).\n"

##############################################################
# To test the unit test:
##############################################################

N_particles = 4
g = 0

folder_name = 'table_files/'
SD_filename = folder_name+"3s_slater_det.sd"
tbme_filename = folder_name+"pairing_g%s.int" %(g)


test_ham = Hamiltonian_one_body(N_particles, 8, SD_filename, tbme_filename)

unit_test_hamiltonian_pairing(N_particles, g, test_ham)




"""
test_ham = np.array([[  2.,   0.,   0.,   0.,   0.,   0.],
        [  0.,   4.   ,0.,   0.,   0.,   0.],
        [  0.,   0.   ,6. ,  0.,   0.,   0.],
        [  0.,   0.  , 0.  , 6.,   0.,   0.],
        [  0.,   0. ,  0.   ,0.,   8.,   0.],
        [  0.,   0.,   0.   ,0.,   0.,  10.]])
"""


