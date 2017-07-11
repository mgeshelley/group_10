from basis import *
import os.path

# Input parameters:
##############################################################


class Error(Exception):
    """Base class for other exceptions"""
    pass

class ValueBelowZeroError(Error):
    """Raised when the input value is too small"""
    pass

class minValueLargerThanMaxError(Error):
    """Raised when the input value is too large"""
    pass

class FloatError(Error):
    """Raised when the input value is not a float"""
    pass

class IsosError(Error):
    """Raised when the input value is not a n or np"""
    pass
"""
while True:
    try:
        nmin, nmax = map(int,raw_input("Write: nmin nmax ").split(' '))
        if np.logical_or(nmin < 0, nmax < 0):
            raise ValueBelowZeroError
        if nmin > nmax:
            raise minValueLargerThanMaxError
    except ValueBelowZeroError:
        print("Please provide numbers above zero.")
        #better try again... Return to the start of the loop
        continue
    except ValueError:
        print("Please provide integers.")
        #better try again... Return to the start of the loop
        continue
    except minValueLargerThanMaxError:
        print("The maximum value must be larger than the minimum value.")
        #better try again... Return to the start of the loop
        continue
    else:
        #age was successfully parsed!
        #we're ready to exit the loop.
        break

while True:
    try:
        lmin, lmax = map(int,raw_input("Write: lmin lmax ").split(' '))
        if np.logical_or(lmin < 0, lmax < 0):
            raise ValueBelowZeroError
        if lmin > lmax:
            raise minValueLargerThanMaxError

    except ValueBelowZeroError:
        print("Please provide numbers above zero.")
        continue
    except ValueError:
        print("Please provide integers.")
        continue
    except minValueLargerThanMaxError:
        print("The maximum value must be larger than the minimum value.")
        continue
    else:
        break

while True:
    try:
        jmin, jmax = map(int,raw_input("Write: 2jmin 2jmax ").split(' '))
        if np.logical_or(jmin < 0, jmax < 0):
            raise ValueBelowZeroError
        if jmin > jmax:
            raise minValueLargerThanMaxError
        
    except ValueBelowZeroError:
        print("Please provide numbers above zero.")
        continue
    except ValueError:
        print("Please provide integers.")
        continue
    except minValueLargerThanMaxError:
        print("The maximum value must be larger than the minimum value.")
        continue
    else:
        break

while True:
    try:
        isos = raw_input("Write: isospin species (n or np) ")
        if isos not in ['n', 'np']:
            raise IsosError

    except IsosError:
        print("Please write either 'n' or 'np'.")
    else:
        break
"""
while True:
    try:
        g = float(raw_input("Write: g "))
        print type(g)
        if not isinstance(g, (float, int)):
            raise FloatError
    except FloatError:
        print("Please provide a float / real number.")

    else:
        break

while True:
    try:        
        N_particles = int(raw_input("Write: N_particles "))
    except ValueBelowZeroError:
        print("Please provide numbers above zero.")
        continue
    except ValueError:
        print("Please provide integers.")
        continue
    else:
        break
        

print g
sys.exit()



##############################################################

nmax = 3
nmin = 0
lmax = 0
lmin = 0
jmin = 1
jmax = 1
isos = 1

g = 1

# read the number of particles in the system
N_particles = 4

"""
# for the harmonic oscillator:
nmax = 2
lmax = 2
jmax = 5
# test of the function sp_harmoscill
#sp_harmoscill(0,nmax,0, lmax,1, jmax, 2)
"""

# filename for the basis:
sp_basis_filename = '3s.sp'
SD_filename = "3s_slater_det.sd"


tbme_filename = "pairing_g%s.int" %(g) #this need to be updated with the current value of g


# Functions
##############################################################

def read_basis(sp_basis_filename):
    """
    Reads in data from the .sp file

    Input   

    sp_basis_filename:  string,
                filename of the basis file to read data from

    Returns 
    
    particle:   ndarray,
                type of particle
    A_core:     float,
                mass number for the core
    Z_core:     float,
                proton nrumber for the core
    nr_sp_states: float,    
                the total number of single-particle states
    nr_groups:  float,
                the total number of group of particles 
    nr_sp_n:    float, 
                number of neutron single-particle states
    nr_sp_p:    float,
                number of proton single-particle states
    sp_matrix:  ndarray,
                matrix containing the single particle states and the quantum numbers.
                data organized in the following way, columns labeld as:
                index, n, l, 2j, 2mj, 2t_z
    """

    particle = np.genfromtxt(sp_basis_filename,skip_header=1, usecols=(0), max_rows=1, dtype='string')
    A_core = np.genfromtxt(sp_basis_filename,skip_header=2, usecols=(0), max_rows=1)
    Z_core = np.genfromtxt(sp_basis_filename,skip_header=2, usecols=(1), max_rows=1)
    nr_sp_states = np.genfromtxt(sp_basis_filename,skip_header=3, usecols=(0), max_rows=1)

    if particle == 'n':
        nr_groups = np.genfromtxt(sp_basis_filename,skip_header=4, usecols=(0), max_rows=1)
        nr_sp_n = np.genfromtxt(sp_basis_filename,skip_header=4, usecols=(1), max_rows=1)
        nr_sp_p = None

    if particle == 'np':
        nr_groups = np.genfromtxt(sp_basis_filename,skip_header=4, usecols=(0), max_rows=1)
        nr_sp_p = np.genfromtxt(sp_basis_filename,skip_header=4, usecols=(1), max_rows=1)
        nr_sp_n = np.genfromtxt(sp_basis_filename,skip_header=4, usecols=(2), max_rows=1)

    sp_matrix = np.genfromtxt(sp_basis_filename,skip_header=5, usecols=(0,1,2,3,4,5))


    return particle, A_core, Z_core, nr_sp_states, nr_groups, nr_sp_n, nr_sp_p, sp_matrix


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

    dim_SD = index
    SD_array = np.array(SD_list)
    SD_states = SD_array.reshape(dim_SD,5)


    out_sd = open(SD_filename,"w")
    out_sd.write("! Tot Slater Determinants = %d \n" % (dim_SD))
    for i in range(0,dim_SD,1):
        out_sd.write('%2d %2d %2d %2d %2d \n' % (SD_states[i,0],SD_states[i,1],SD_states[i,2],SD_states[i,3],SD_states[i,4]))
    out_sd.close()


def read_SD(SD_filename):
    """
    Reads in data from the .sd file

    Input   

    SD_filename:string,
                filename of the slater determinant file to read data from

    Returns 
    
    SD_matrix:  ndarray,
                matrix containing the slater determinants.
                Every row identifies a different slater determinant.
                First column: the index of the slater determinants.
                In the last four columns the labels of the occupied single particle states are listed.
                
    """

    SD_matrix = np.genfromtxt(SD_filename,skip_header=1, usecols=(0,1,2,3,4))

    return SD_matrix


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
    
##############################################################

#checking if the basis file exist, if not create the basis
if os.path.isfile(sp_basis_filename) == False: 
    sp_pairing(nmin, nmax, lmin, lmax, jmin, jmax, isos)

particle, A_core, Z_core, nr_sp_states, nr_groups, nr_sp_n, nr_sp_p, sp_matrix = read_basis(sp_basis_filename)

#creating the slater determinants
if os.path.isfile(SD_filename) == False:
    create_SD(N_particles, nr_sp_states, sp_matrix, SD_filename)

SD_matrix = read_SD(SD_filename)

#creating the pairing interaction
if os.path.isfile(tbme_filename) == False:
    create_tbme_pairing(tbme_filename,nr_sp_states,g)

# Here we should read in the hamiltonian matrix


# Finding the eigenvalues and eigenvectors
##############################################################
#eigval, eigvec = np.linalg.eigh(hamiltonian_matrix)












