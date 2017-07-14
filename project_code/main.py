# This program runs the whole simulation by calling the functions from the other programs

# Importing the files containing the needed functions (that we wrote our selves)
from basis import *
from create_table_files import *
from read_files import *
from unit_tests import *
from ham import *
from input_func import command_line_input

# other imports:
import os.path

##############################################################
# Function to give standard input (without command line)
##############################################################

def manual_input(model='pairing'):
    
    """
    "Standard" input parameters (when to lazy to give the input on the command line)
    
    Input (None)

    Returns 
    
    nmin:       int,
                minumum n

    nmax:       int,
                maximum n

    lmin:       int,
                minumum l

    lmax:       int,
                maximum l

    jmin:       int,
                minumum j

    jmax:       int,
                maximum j

    isos:       string,
                the species of the nucleons for the simulation

    g:          float, 
                the pairing constant

    N_particles: int,
                the number of particles in the simulation

    """
    if model=='pairing':
        
        nmin = 0
        nmax = 3
        lmin = 0
        lmax = 0
        jmin = 1
        jmax = 1
        isos = 'n'
        g = 1
        N_particles = 4 # read the number of particles in the system
    if model=='harmonic':
        #do stuff
        n = 0

    return nmin, nmax, lmin, lmax, jmin, jmax, isos, g, N_particles


##############################################################
# This part of program is to run the whole simulation:
##############################################################
# Choose if you want to read the input from command line or inside this program:
# (uncomment your choice and comment the other):

#nmin, nmax, lmin, lmax, jmin, jmax, isos, g, N_particles = command_line_input()
nmin, nmax, lmin, lmax, jmin, jmax, isos, g, N_particles = manual_input()


# filename for the basis, slater det and tbme:
# (we could also implement the file names into the input functions)
folder_name = 'table_files/'
sp_basis_filename = folder_name+'3s.sp'
SD_filename = folder_name+"3s_slater_det.sd"
tbme_filename = folder_name+"pairing_g%s.int" %(g) 

##############################################################
# Checking if the files containing the basis and the slater 
# determinants  already exist, if not create them:
if os.path.isfile(sp_basis_filename) == False: 
    sp_pairing(nmin, nmax, lmin, lmax, jmin, jmax, isos, folder_name)

if os.path.isfile(SD_filename) == False:
    create_SD(N_particles, nr_sp_states, sp_matrix, SD_filename)

# Read in the basis and the SD from files:
particle, A_core, Z_core, nr_sp_states, nr_groups, nr_sp_n, nr_sp_p, sp_matrix = read_basis(sp_basis_filename)
SD_matrix = read_SD(SD_filename)
nr_SD = SD_matrix.shape[0]

# Creating the file containing the pairing interaction:
if os.path.isfile(tbme_filename) == False:
    create_tbme_pairing(tbme_filename,nr_sp_states,g)

##############################################################
# Creating the hamiltonian matrix

# The 1-body and 2-body hamiltonian matrices are added together to form hamiltonian_total
# hamiltonian_total is initialized to zeros
hamiltonian_total = np.zeros((nr_SD, nr_SD))
hamiltonian_1body = Hamiltonian_one_body(N_particles, nr_sp_states, SD_filename, tbme_filename)
hamiltonian_2body = Hamiltonian_two_body(N_particles, nr_sp_states, SD_filename, tbme_filename)

hamiltonian_total = hamiltonian_1body+hamiltonian_2body
#print hamiltonian_total

##############################################################
# Uncomment here to demonstrate the unit test:
##############################################################
#hamiltonian_total_error_test = hamiltonian_total
#hamiltonian_total_error_test[0,1] = 0
#unit_test_hamiltonian_pairing(N_particles, g, hamiltonian_total_error_test)

##############################################################
# test if the hamiltonian is correct for the pairing problem:
unit_test_hamiltonian_pairing(N_particles, g, hamiltonian_total)


##############################################################
# Finding the eigenvalues and eigenvectors
eigval, eigvec = np.linalg.eigh(hamiltonian_total)

print 'Eigenvalues:'
print eigval
print '\n'
print 'Eigenvectors:'
print eigvec
print '\n'


# DONE!


