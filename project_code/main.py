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



##############################################################
# This part of program is to run the whole simulation:
##############################################################
# Choose if you want to read the input from command line or inside this program:
# (uncomment your choice and comment the other):

nmin, nmax, lmin, lmax, jmin, jmax, isos, g, N_particles, sp_basis_filename, SD_filename, tbme_filename = command_line_input()
#nmin, nmax, lmin, lmax, jmin, jmax, isos, g, N_particles, sp_basis_filename, SD_filename, tbme_filename = manual_input()


# filename for the basis, slater det and tbme:
# (we could also implement the file names into the input functions)


##############################################################
# Checking if the files containing the basis and the slater 
# determinants  already exist, if not create them:
if os.path.isfile(sp_basis_filename) == False: 
    sp_pairing(nmin, nmax, lmin, lmax, jmin, jmax, isos, sp_basis_filename)

# Read in the basis from file
particle, A_core, Z_core, nr_sp_states, nr_groups, nr_sp_n, nr_sp_p, sp_matrix = read_basis(sp_basis_filename)

if os.path.isfile(SD_filename) == False:
    create_SD(N_particles, nr_sp_states, sp_matrix, SD_filename)

# Read in the SD from files:
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


