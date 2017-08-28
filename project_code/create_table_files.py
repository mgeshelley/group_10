# Creating table files

import numpy as np
import itertools

############################
'''
DEFINITIONS OF FUNCTION TO CALCULATE SINGLE PARTICLE STATES
the single-particle states are identified by the quantum numbers (n,l,2j,2m_j,2tz) 
starting with the smallest 2m_j value and 2tz [2tz=-1 for p, 2tz=+1 for n]
ATTENTION the variable j, m and tz are equal to 2 times the corresponding quantum number

nmin, nmax are the min and max principal quantum number  
lmin, lmax are the min and max of orbital angular moments
jmin and jmax are the min and max of total angular moments
isos is the number of different isospin species only n -> isos=1, np -> isos=2
'''
def sp_pairing(nmin, nmax, lmin, lmax, jmin, jmax, isos, sp_basis_filename):
#
  if lmin == lmax: 
    l = lmax
  if lmin != lmax:
    sys.exit('ERROR: lmin != lmax not allowed in pairing sp-basis')
# CALCULATE THE DIMENSION OF THE SP-BASIS
  print 'MODEL SINGLE-PARTICLE STATES'
  print 'index n  l 2j 2m 2tz'
#
  sp = []
  index = 0
  if isos == 'n':
    tz_min = 1
    tz_max = 1
  elif isos == 'np':
    tz_min = -1
    tz_max = 1
  else:
    sys.exit('ERROR: wrong number of isospin species')
#
  for tz in range (tz_min, tz_max+2, 2):
    for n in range(0, nmax+1, 1):
      for j in range(1, jmax+2, 2):
        m = -j
        while m <= jmax:
          index = index+1
          sp.append(index)
          sp.append(n)
          sp.append(l)
          sp.append(j)
          sp.append(m)
          sp.append(tz)
          print ' %2d %3d %2d %2d %2d %2d' % (index, n, l, j, m, tz)
          m = m+2
        #end of while m
      #end of for j
    #end of for n
  #end of for tz
#
  dim_basis = index
  print ' tot s.p. states = %d ' % (dim_basis)
#
# transform sp list in matrix
  sp_array = np.array(sp)
  sp_matrix = sp_array.reshape(dim_basis,6)
#
# write an output in a NutshellX similar file .ps
  out_sp = open(sp_basis_filename,"w")
  out_sp.write("!4 level 2j=1 l=0 single-particle states. This describes a system with paired particles of the same isospin\n")
  out_sp.write("n \n")
  out_sp.write("0  0 \n")# assuming A=0 nad Z=0 for the core
  out_sp.write("%d \n" % dim_basis) # total number of sp states
  out_sp.write("1 %d \n" % dim_basis) # 1 group of sp states, number of sp states per group
  np.savetxt(out_sp, sp_matrix, fmt='%d %d %d %d %2d %d')
  out_sp.close()
  return sp_matrix
#
#######################################################
# HARMONIC OSCILLATOR SINGLE PARTICLE STATE
#
def sp_harmoscill(nmin,nmax,lmin, lmax,jmin, jmax, isos):
#
  print 'MODEL SINGLE-PARTICLE STATES'
  print 'index n  l 2j 2m 2tz'
#
  sp = []
  index = 0
  if isos == 'n':
    tz_min = 1
    tz_max = 1
  elif isos == 'np':
    tz_min = -1
    tz_max = 1
  else:
    sys.exit('ERROR: wrong number of isospin species')
#
  for tz in range (tz_min, tz_max+2, 2):
    for ntot in range(nmin, nmax+1, 1):
      l_start = max(lmin,ntot%2)
      for l in range(l_start, ntot+2, 2):
        n = (ntot-l)/2
        j_start = max(jmin,abs(2*l-1))
        for j in range(j_start, 2*l+1+2, 2):
          for m in range (-j, j+2, 2):
            index = index+1
            sp.append(index)
            sp.append(n)
            sp.append(l)
            sp.append(j)
            sp.append(m)
            sp.append(tz)
            print ' %2d %3d %2d %2d %2d %2d' % (index, n, l, j, m, tz)
          #end for m
        #end of for j
      #end for l
    #end of for n
  #end of for tz
#
  dim_basis = index
  print ' tot s.p. states = %d ' % (dim_basis)
#
# transform sp list in matrix
  sp_array = np.array(sp)
  sp_matrix = sp_array.reshape(dim_basis,6)
#
# write an output in a NutshellX similar file .ps
  out_sp = open("ho.sp","w")
  out_sp.write("!harmonic oscillator single-particle states\n")
  out_sp.write("np \n")
  out_sp.write("0  0 \n")# assuming A=0 nad Z=0 for the core
  out_sp.write("%d \n" % dim_basis) # total number of sp states
  out_sp.write("2 %d %d \n" % (dim_basis/2, dim_basis/2) ) # 1 group of sp states, number of sp states per group
  np.savetxt(out_sp, sp_matrix, fmt='%2d %d %d %d %2d %d')
  out_sp.close()
  return sp_matrix
##############################################################




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



