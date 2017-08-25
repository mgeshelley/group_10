# This program runs the whole simulation by calling the functions from the other programs

# Importing the files containing the needed functions (that we wrote our selves)
#from basis import *
from create_table_files import *
from read_files import *
from unit_tests import *
from ham import *
from input_func import *

# other imports:
import os.path

##############################################################
# Choose if you want to interact with the terminal:
# (uncomment your choice and comment the other):
'''
#nmin, nmax, lmin, lmax, jmin, jmax, isos, g, N_particles, sp_basis_filename, SD_filename, tbme_filename = command_line_input()
#nmin, nmax, lmin, lmax, jmin, jmax, isos, g, N_particles = manual_input()
#sp_basis_filename, SD_filename, tbme_filename = give_file_names(g)

#FOR TESTING PURPOUSE ONLY
tbme_filename = 'table_files/sd_mscheme.int'

##############################################################
# Deciding if using the sd shell or not:

sd_shell = 'sd'

if sd_shell == 'sd':
    sp_matrix = read_sd_basis('table_files/sd_shell.sp')
    nr_sp_states = np.shape(sp_matrix)[0]


elif sd_shell != 'sd':
    # Checking if the files containing the basis and the slater
    # determinants  already exist, if not create them:
    if os.path.isfile(sp_basis_filename) == False:
        sp_pairing(nmin, nmax, lmin, lmax, jmin, jmax, isos, sp_basis_filename)

    # Read in the basis from file
    particle, A_core, Z_core, nr_sp_states, nr_groups, nr_sp_n, nr_sp_p, sp_matrix = read_basis(sp_basis_filename)


##############################################################

if os.path.isfile(SD_filename) == False:
    #create_SD(N_particles, nr_sp_states, sp_matrix, SD_filename)
    create_SD_perm(N_particles, nr_sp_states, sp_matrix, SD_filename, 'pair')


# Read in the SD from files:
SlaterD_matrix = read_SD(N_particles, SD_filename)
nr_SD = SlaterD_matrix.shape[0]

#for g in (loop over g values)

# Creating the file containing the pairing interaction:
if os.path.isfile(tbme_filename) == False:
    create_tbme_pairing(tbme_filename,nr_sp_states,g)

'''

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

'''
sp_basis_filename = 'table_files/3s_mscheme.sp'
SD_filename = 'table_files/3s_pairing.sd'
tbme_filename = 'table_files/pairing_g1.int'
restriction = 'pair'
g = 1

#SD case
sp_basis_filename = 'table_files/sd_shell.sp'
SD_filename = 'table_files/sd_SlaterD.sd'
tbme_filename = 'table_files/sd_mscheme.int'
restriction = 'no'
'''
print("\n...calculating...\n")
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
#print g
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

##############################################################
# Uncomment here to demonstrate the unit test:
##############################################################
#hamiltonian_total[0,1] = 100

##############################################################
# Test if the hamiltonian is correct for the pairing problem:

#unit_test_hamiltonian_pairing(N_particles, g, hamiltonian_total)

##############################################################
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

#print 'g =',g


# DONE!

