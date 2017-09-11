# Creating table files

import numpy as np
import itertools


#############################################################################################

def create_SD_perm(N_particles, nr_sp_states, sp_matrix, SD_filename, restrictions=''): 

    """
    Writes all the possible slater determinants to a .sd file.
    Every row identifies a different slater determinant.
    First column: the index of the slater determinants.
    In the last four columns the labels of the occupied single particle states are listed.

    Input

    N_particles:    float,
                number of particles
    nr_sp_states:   float,  
                the total number of single-particle states  
    sp_matrix:      ndarray,
                matrix containing the single particle states and the quantum numbers.
                data organized in the following way, columns labeld as:
                index, n, l, 2j, 2mj
    SD_filename:    string,
            name of the file where to save the Slater Determinants
    restrictions:   string,
            'pair' indicates system with pairs of nucleons (only N_particles even)          

    Returns:
    the file SD_filename

    """

    nr_sp_states = int(nr_sp_states)
    sp_list = []
    for i in range(1, nr_sp_states+1):
        sp_list.append(i)
    sp_tuple = tuple(sp_list)
    #print sp_tuple
    index = 0
    SD_list = []
    act_list = []
    for x in itertools.combinations(sp_tuple, N_particles):
        m_tot = 0
        for k in range (N_particles):
            m_tot = m_tot + sp_matrix[x[k]-1,4]
        #PAIRING CASE
        # in pairing case only N_particles even is considered
        if restrictions == 'pair':
            if N_particles%2 == 0:
                pair_bool = 0
                # check that the single-particle states are in pairs
                for j in range (0,N_particles,2):
                    if np.array_equal(sp_matrix[x[j]-1,1:3], sp_matrix[x[j+1]-1,1:3]):
                        pair_bool = pair_bool 
                    else:
                        pair_bool = pair_bool +1
                # check that M=0 and pairs are coupled
                if m_tot == 0 and pair_bool == 0:
                    index +=1
                    SD_list.append(index)
                    SD_list.extend(list(x))
        #GENERAL CASE
        else:
            index +=1
            SD_list.append(index)
            SD_list.extend(list(x))
    
    nr_SD = index
    SD_array = np.array(SD_list)
    SD_states = SD_array.reshape(nr_SD,N_particles+1)


    out_sd = open(SD_filename,"w")
    #out_sd.write("! Tot Slater Determinants = %d \n" % (nr_SD))
    np.savetxt(SD_filename,SD_states,fmt='%2d')
    out_sd.close()

##################################################################################

def create_tbme_pairing(tbme_filename,nr_sp_states,g):
    """
    Produce tbme_filename file with tbme 

    Input   

    tbme_filename:      string,
                filename of the file to produce
    nr_sp_states:       float,
                nr of possible single-particle states
    g:          float,
                parameter of the pairing interaction


    Output 
    
    tbme_filename:      file that contains the tbme (two body matrix element) for the pairing interaction
                        1st line: tbme_dim
                        tbme_dim: number of non-zero matrix elements              
                        sp_1, sp_2, sp_3, sp_4, matrix element

    """


    # g is the value of the pairing parameter
    index = 0
    tbme_list = []
#    J = 0
#    T = 1

    p_1=1
    p_2=2
    p_3=3
    p_4=4


    nr_sp_states = int(nr_sp_states)

    for a in range(1, nr_sp_states+1,2):
        for b in range(a, nr_sp_states+1,2):
            index += 1
            tbme_list.extend([a,a+1,b,b+1,-g])
    dim_tbme = index
    tbme_array = np.array(tbme_list)
    tbme_matrix = tbme_array.reshape(dim_tbme,5)


    out_tbme = open(tbme_filename,"w")
    out_tbme.write("! %s matrix elements\n" % (tbme_filename))
    out_tbme.write("! list of states\n")
    out_tbme.write("%d  \n" % dim_tbme)
    for i in range(0,dim_tbme):
        out_tbme.write('%2d %2d %2d %2d %7.3f \n' % (tuple(tbme_matrix[i,0:4])+tuple([tbme_matrix[i,4]])))
    out_tbme.close()



