# This program runs the whole simulation by calling the functions from the other programs

# Importing the files containing the needed functions (that we wrote our selves)

from create_table_files import *
from read_files import *
from unit_tests import *
from ham import *
from input_func import *

# other imports:
import os.path

##############################################################

# MAIN 
# name of the folder with files
folder_name = 'table_files/'

#input from command line
N_particles,case,g = command_line_input()

'''
#manual input to be used instead of command line
N_particles = 4
g = 1
case = 'sd'
'''

# PAIRING case works only for N=2,4,6,8
if case == 'pairing':
	if N_particles%2 == 1 or N_particles <= 0 or N_particles > 8:
		print("\nERROR: N_particles need can be only 2,4,6 or 8 in the pairing case.\n")
	else:
		sp_basis_filename = folder_name+'3s_mscheme.sp'
		SD_filename = folder_name+'3s_pairing.sd'
		tbme_filename = folder_name+"pairing_g%s.int" %g
		restriction = 'pair'
		g = float(g)/2 # the strenght is g but 1/2 factor come from the definition of pairing interaction
#SD case	
elif case == 'sd':
	sp_basis_filename = folder_name+'sd_shell.sp'
	SD_filename = folder_name+'sd_SlaterD.sd'
	tbme_filename = folder_name+'sd_mscheme.int'
	restriction = 'no'


print("\n...calculating...\n")


##############################################################
# Test if the hamiltonian is correct for the pairing problem:

unit_test_hamiltonian_pairing()

##############################################################

# read sp_basis from file .sp
sp_matrix = read_sd_basis(sp_basis_filename)
nr_sp_states = np.shape(sp_matrix)[0]

create_SD_perm(N_particles, nr_sp_states, sp_matrix, SD_filename, restriction)

# Read in the SD from files:
SlaterD_matrix = read_SD(N_particles, SD_filename)
nr_SD = SlaterD_matrix.shape[0]


# Creating the file containing the pairing interaction:
if case == 'pairing' and os.path.isfile(tbme_filename) == False:
    create_tbme_pairing(tbme_filename,nr_sp_states,g)
#
##############################################################
# Creating the hamiltonian matrix

# The 1-body and 2-body hamiltonian matrices are added together to form hamiltonian_total
# hamiltonian_total is initialized to zeros
hamiltonian_total = np.zeros((nr_SD, nr_SD))
hamiltonian_1body = np.zeros((nr_SD, nr_SD))
hamiltonian_2body = np.zeros((nr_SD, nr_SD))
hamiltonian_1body = Hamiltonian_one_body(N_particles, nr_sp_states, sp_matrix, SD_filename)
hamiltonian_2body = Hamiltonian_two_body(N_particles, nr_sp_states, SD_filename, tbme_filename, case)

hamiltonian_total = hamiltonian_1body+hamiltonian_2body


# Finding the eigenvalues and eigenvectors
eigval, eigvec = np.linalg.eigh(hamiltonian_total)

print 'model space %s' % case
print "Number of particles (neutrons): %d" % N_particles
print '\n'
print 'Eigenvalues:'
np.set_printoptions(formatter={'float': '{: 0.3f}'.format})
print(eigval)
print '\n'
print 'Eigenvectors:'
np.set_printoptions(formatter={'float': '{: 0.2f}'.format})
print(eigvec)


# DONE!

