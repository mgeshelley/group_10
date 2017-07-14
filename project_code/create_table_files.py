# Creating table files

import numpy as np

def create_SD(N_particles, nr_sp_states, sp_matrix, SD_filename):
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
                    index, n, l, 2j, 2mj, 2t_z          

    Returns:
    the file '3s_slater_det.sd'
    
    """

    nr_sp_states = int(nr_sp_states)

    index = 0
    SD_list = []

    for a in range (1, nr_sp_states-2,1):
        for b in range (a+1, nr_sp_states-1, 1):
            for c in range (b+1, nr_sp_states, 1):
                for d in range (c+1, nr_sp_states+1, 1):
                    
                    m_tot = sp_matrix[a-1,4] + sp_matrix[b-1,4] + sp_matrix[c-1,4] + sp_matrix[d-1,4]
                    if np.array_equal(sp_matrix[a-1,1:3], sp_matrix[b-1,1:3]):
                        if np.array_equal(sp_matrix[c-1,1:3], sp_matrix[d-1,1:3]):
                            if m_tot == 0:
                                index += 1
                                SD_list.append(index)
                                SD_list.extend([a,b,c,d])

    nr_SD = index
    SD_array = np.array(SD_list)
    SD_states = SD_array.reshape(nr_SD,5)


    out_sd = open(SD_filename,"w")
    out_sd.write("! Tot Slater Determinants = %d \n" % (nr_SD))
    for i in range(0,nr_SD,1):
        out_sd.write('%2d %2d %2d %2d %2d \n' % (SD_states[i,0],SD_states[i,1],SD_states[i,2],SD_states[i,3],SD_states[i,4]))
    out_sd.close()

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
                        1st line: tbme_dim, E0, E1, E2, E3, constant, A_core, exponent
                        tbme_dim: number of non-zero matrix elements
                        E0,E1,E2,E3 are the energy of the sp levels (p-1 in our case)
                        A_core,constant,exponent: the parameters of the mass dependence [constant/(A_core+n_val)]^exponent
                        other lines: sp_1, sp_2, sp_3, sp_4, J_tot, T_tot, matrix element

    """


    # g is the value of the pairing parameter
    index = 0
    tbme_list = []
    J = 0
    T = 1

    p_1=1
    p_2=2
    p_3=3
    p_4=4

    constant= 0
    A_core= 0
    exponent= 0

    nr_sp_states = int(nr_sp_states)

    for a in range(1, nr_sp_states+1,2):
        for b in range(a, nr_sp_states+1,2):
            index += 1
            tbme_list.extend([a,a+1,b,b+1,J,T,-g])
    dim_tbme = index
    tbme_array = np.array(tbme_list)
    tbme_matrix = tbme_array.reshape(dim_tbme,7)


    out_tbme = open(tbme_filename,"w")
    out_tbme.write("! %s matrix elements\n" % (tbme_filename))
    out_tbme.write("! list of states\n")
    out_tbme.write("%d %7.3f %7.3f %7.3f %7.3f %7.3f %7.3f %7.3f \n" % (dim_tbme, p_1-1, p_2-1, p_3-1, p_4-1, constant, A_core, exponent))
    for i in range(0,dim_tbme):
        out_tbme.write('%2d %2d %2d %2d %2d %2d %7.3f \n' % (tuple(tbme_matrix[i,0:6])+tuple([tbme_matrix[i,6]])))
    out_tbme.close()



