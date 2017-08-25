# Creates the one-body and the two body hamiltonian matrix for the pairing problem
from compare import *
import numpy as np
import sys

def Hamiltonian_one_body(N_particles, nr_sp_states, matrix, SD_filename):
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

    Output

    hamiltonian_1body:    ndarray,
                    Hamiltonian matrix with the one-body interaction terms
    """

    nr_sp_states = int(nr_sp_states)
    N_particles = int(N_particles)

    # The file with Slater Determinants (s_d) is loaded [index, sp states]
    s_d = np.loadtxt(SD_filename, comments = "!", skiprows=0, dtype = 'int')
    s_d = np.atleast_2d(s_d)
    #print s_d
    # number of Slater determinants
    nr_sd = s_d.shape[0]
    #print nr_sd
    '''
    if N_particles == nr_sp_states:
        nr_sd = 1
        s_d[0,1:] = list(s_d)
    '''

    # Read the single-particle energies from the last column of .sp file
    sp_energies = list(matrix[:,-1])
    #print sp_energies
    
    # Make a matrix with the single-particle energies on the diagonal <p|h_1body|q>
    
    ''' THIS PART IS NO LONGER NECESSARY WITH sd-model space
    H_diag = np.zeros((nr_sp_states, nr_sp_states))
    for i in range(nr_sp_states):
        H_diag[i,i] = sp_energies[i] #this is an integer division
    '''

    # initialize to zero the Hamiltonian <beta_SD|H|alpha_SD>
    hamiltonian_1body = np.zeros((nr_sd, nr_sd))
    #print nr_sd
    # loop over <beta_SD|
    for beta in range(0, nr_sd, 1):
        #print s_d.shape
        #print beta
        beta_list = list(s_d[beta,1:])
        #print beta_list
        # loop over |alpha_SD>
        for alpha in range(0, nr_sd, 1):

            alpha_list = list(s_d[alpha,1:])
            # index = -1 means not index found

            # Add single-particle energies to diagonal of Hamiltonian
            if alpha == beta:

                for i in range(0,N_particles):
                    #eps_i = 1
                    eps_i = sp_energies[alpha_list[i]-1] # to account for the energy of the sp_states with label i
                    #print i, alpha_list[i], eps_i
                    hamiltonian_1body[beta, alpha] = hamiltonian_1body[beta, alpha] + eps_i
    #print hamiltonian_1body
    return hamiltonian_1body


##########################################################################################################


def Hamiltonian_two_body(N_particles, nr_sp_states, SD_filename, tbme_filename):

    """
    This function builds the two-body part of the Hamiltonian <beta_SD|H|alpha_SD>

    To call it
    Hamiltonian_two_body(N_particles, nr_sp_states, SD_filename, tbme_filename)

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

    hamiltonian_2body:    ndarray,
                    Hamiltonian matrix with the one-body interaction terms
    """

    nr_sp_states = int(nr_sp_states)
    N_particles = int(N_particles)

    # The file with Slater Determinants (s_d) is loaded [index, sp states]
    #s_d = np.loadtxt(folder_name+"3s_slater_det.sd", comments = "!", skiprows=0) #only for testing
    s_d = np.loadtxt(SD_filename, comments = "!", skiprows=0, dtype = 'int')
    s_d = np.atleast_2d(s_d)
    # number of Slater determinants
    nr_sd = s_d.shape[0]

    #sys.exit()

    # Read the two-body matrix elements from the .int file
    #two_body_me = np.loadtxt(folder_name+"pairing_g1.int", comments = "!", skiprows=3) #only for testing
    two_body_me = np.loadtxt(tbme_filename, comments = "!", skiprows=3)


    # nr_2bme is the number of two body matrix elements
    nr_2bme = two_body_me.shape[0]
    
    #if np.genfromtxt(folder_name+"pairing_g1.int", comments = "!", skip_header=2, max_rows=1)[0] != nr_2bme:
    #   sys.exit("ERROR: Dimension of 2-body matrix not consistent!!!") #only for testing

    if np.genfromtxt(tbme_filename, comments = "!", skip_header=2, max_rows=1, dtype='int') != nr_2bme:
        sys.exit("ERROR: Dimension of 2-body matrix not consistent!!!")
    
    two_body_matrix = np.zeros((nr_sp_states+1,nr_sp_states+1,nr_sp_states+1,nr_sp_states+1))
    mass_corr = (18./(16.+N_particles))**0.3
    for k in range(0,nr_2bme):
        two_body_matrix[int(two_body_me[k,0]),int(two_body_me[k,1]), \
                        int(two_body_me[k,2]),int(two_body_me[k,3])] = two_body_me[k,4] * mass_corr
        two_body_matrix[int(two_body_me[k,0]),int(two_body_me[k,1]), \
                        int(two_body_me[k,3]),int(two_body_me[k,2])] = -two_body_me[k,4] * mass_corr
        two_body_matrix[int(two_body_me[k,1]),int(two_body_me[k,0]), \
                        int(two_body_me[k,2]),int(two_body_me[k,3])] = -two_body_me[k,4] * mass_corr
        two_body_matrix[int(two_body_me[k,1]),int(two_body_me[k,0]), \
                        int(two_body_me[k,3]),int(two_body_me[k,2])] = two_body_me[k,4] * mass_corr
        two_body_matrix[int(two_body_me[k,2]),int(two_body_me[k,3]), \
                        int(two_body_me[k,0]),int(two_body_me[k,1])] = two_body_me[k,4] * mass_corr
        two_body_matrix[int(two_body_me[k,2]),int(two_body_me[k,3]), \
                        int(two_body_me[k,1]),int(two_body_me[k,0])] = -two_body_me[k,4] * mass_corr
        two_body_matrix[int(two_body_me[k,3]),int(two_body_me[k,2]), \
                        int(two_body_me[k,0]),int(two_body_me[k,1])] = -two_body_me[k,4] * mass_corr
        two_body_matrix[int(two_body_me[k,3]),int(two_body_me[k,2]), \
                        int(two_body_me[k,1]),int(two_body_me[k,0])] = two_body_me[k,4] * mass_corr

   
    # initialize to zero the Hamiltonian <beta_SD|H|alpha_SD>
    hamiltonian_2body = np.zeros((nr_sd, nr_sd))


    # loop over <beta_SD|
    for beta in range(0, nr_sd, 1):

        beta_list = list(s_d[beta,1:])
        # loop over |alpha_SD>
        for alpha in range(0, nr_sd, 1):
            alpha_list = list(s_d[alpha,1:])


            diff_list,phase = beta_alpha_compare(beta_list, alpha_list)

            # AlphA and beta are same
            if len(diff_list) == 0:
                # Sum over i and j (all 2-body matrix elements)
                for i in range(0,N_particles):
                    for j in range(0,N_particles):
                        a = alpha_list[i]
                        b = alpha_list[j]
                        #print a,b, two_body_matrix[a,b,a,b]
                        # If 2-body me exists, add to Hamiltonian
                        if two_body_matrix[a,b,a,b] != 0.0:
                            # THE COEFFICIENT 1/2 HAS BEEN REMOVED BECAUSE THE SUM RUN ON i<=j
                            #mat_element = 0.5 * two_body_matrix[a,b,a,b]
                            mat_element = 0.5*two_body_matrix[a,b,a,b]
                            hamiltonian_2body[beta,alpha] = hamiltonian_2body[beta,alpha] + mat_element
                            #mat_element = 0.5*two_body_matrix[a,b,a,b]
                            #hamiltonian_2body[beta,alpha] = hamiltonian_2body[beta,alpha] + mat_element

            # Alpha and beta have one difference
            elif len(diff_list) == 2:
                '''
                alpha_list_aux = list(alpha_list)
                alpha_list_aux.remove(diff_list[1])
                for b in alpha_list_aux:
                    phase_aux = 0
                    a = diff_list[0]
                    if a > b:
                        a_aux = b
                        b_aux = a
                        phase_aux = phase_aux +1
                    else:
                        a_aux = a
                        b_aux = b

                    c = diff_list[1]
                    if c > b:
                        c_aux = b
                        d_aux = c
                        phase_aux = phase_aux +1
                    else:
                        c_aux = c
                        d_aux = b
                    #here it is the problem
                    print a_aux,b_aux,c_aux,d_aux, two_body_matrix[a_aux,b_aux,c_aux,d_aux]
                    # If 2-body me exists, add to Hamiltonian
                    if two_body_matrix[a_aux,b_aux,c_aux,d_aux] != 0.0:
                        mat_element = two_body_matrix[a_aux,b_aux,c_aux,d_aux]*phase*phase_aux
                        hamiltonian_2body[beta,alpha] = hamiltonian_2body[beta,alpha] + mat_element
                    '''
                    # If 2-body me exists, add to Hamiltonian
                alpha_list_aux = list(alpha_list)
                alpha_list_aux.remove(diff_list[1])
                for b in alpha_list_aux:
                    
                    a = diff_list[0]
                    c = diff_list[1]
                    #print a,b,c,b, alpha_list_aux
                    if two_body_matrix[a,b,c,b] != 0.0:

                        mat_element = two_body_matrix[a,b,c,b]*phase

    
                        hamiltonian_2body[beta,alpha] = hamiltonian_2body[beta,alpha] + mat_element
                        '''
                        if alpha == 0 and beta == 15:
                            print beta, alpha, diff_list, a,b,c,b, two_body_matrix[a,b,c,b],mat_element, hamiltonian_2body[beta,alpha]
                        if alpha == 15 and beta == 0:
                            print beta, alpha, diff_list, a,b,c,b,two_body_matrix[a,b,c,b], mat_element, hamiltonian_2body[beta,alpha]
                        
                        #print beta, alpha, hamiltonian_2body[beta,alpha]
                        mat_element = two_body_matrix[c,b,a,b]*phase
                        #print beta, alpha, mat_element
                        hamiltonian_2body[beta,alpha] = hamiltonian_2body[beta,alpha] + mat_element

                        if alpha == 2 and beta == 7:
                            print beta, alpha, diff_list,c,b,a,b, mat_element, hamiltonian_2body[beta,alpha]
                        if alpha == 7 and beta == 2:
                            print beta, alpha, diff_list,c,b,a,b, mat_element, hamiltonian_2body[beta,alpha]
                        '''



            # Alpha and beta have two differences
            elif len(diff_list) == 4:
                
                a = diff_list[0]
                b = diff_list[1]
                c = diff_list[2]
                d = diff_list[3]
                #print a,b,c,d, two_body_matrix[a,b,c,d]
                # If 2-body me exists, add to Hamiltonian
                if two_body_matrix[a,b,c,d] != 0.0:
                    mat_element = two_body_matrix[a,b,c,d]*phase
                    #print mat_element
                    hamiltonian_2body[beta,alpha] = hamiltonian_2body[beta,alpha] + mat_element
                    #print beta, alpha,  a,b,c,d,two_body_matrix[a,b,c,d], mat_element, hamiltonian_2body[beta,alpha]
                    #mat_element = two_body_matrix[c,d,a,b]*phase
                    #hamiltonian_2body[beta,alpha] = hamiltonian_2body[beta,alpha] + mat_element

        #sys.exit()
    #print hamiltonian_2body
    return hamiltonian_2body
##############################################################
