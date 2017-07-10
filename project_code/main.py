from basis import *


# Input parameters:
##############################################################
nmax = 3
nmin = 0
lmax = 0
lmin = 0
jmin = 1
jmax = 1
isos = 1
# test of the fuction sp_pairing
#sp_pairing(nmin, nmax, lmin, lmax, jmin, jmax, isos)
#
#
nmax = 2
lmax = 2
jmax = 5
# test of the function sp_harmoscill
#sp_harmoscill(0,nmax,0, lmax,1, jmax, 2)
#

# filename for the basis:
sp_basis_filename = '3s.sp'

##############################################################

def read_basis(sp_basis_filename):
	"""
	Reads in data from the .sp file

	Input: 		string,
				filename of the basis file to read data from

	Returns 
	
	particle: 	ndarray,
				type of particle
	A_core:		float,
				mass number for the core
	Z_core:		float,
				proton nrumber for the core
	nr_sp_states: float,	
				the total number of single-particle states
	nr_groups:	float,
				the total number of group of particles 
	nr_sp_n:	float, 
				number of neutron single-particle states
	nr_sp_p:	float,
				number of proton single-particle states
	sp_matrix: 	ndarray,
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

##############################################################


a, b, ... = read_basis(sp_basis_filename)


#print nr_sp_states
#print matrix

