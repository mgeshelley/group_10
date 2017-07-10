from basis import *
import os.path

# Input parameters:
##############################################################
nmax = 3
nmin = 0
lmax = 0
lmin = 0
jmin = 1
jmax = 1
isos = 1

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


# read the number of particles in the system
N_particles = 4

# How to use command line input:
#if len(sys.argv) == ... :
	#nmax = int(sys.argv[1])

# Functions
##############################################################

def read_basis(sp_basis_filename):
	"""
	Reads in data from the .sp file

	Input	

	sp_basis_filename:	string,
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


def create_SD(N_particles, nr_sp_states, sp_matrix, SD_filename):
	"""
	Writes all the possible slater determinants to a .sd file.
	Every row identifies a different slater determinant.
	First column in the file is the index of the slater determinants.
	The four last columns gives the occupied single particle states. 

	Input

	N_particles: 	float,
					number of particles
	nr_sp_states: 	float,	
					the total number of single-particle states	
	sp_matrix: 		ndarray,
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

##############################################################

if os.path.isfile(sp_basis_filename) == False:
	sp_pairing(nmin, nmax, lmin, lmax, jmin, jmax, isos)

particle, A_core, Z_core, nr_sp_states, nr_groups, nr_sp_n, nr_sp_p, sp_matrix = read_basis(sp_basis_filename)

if os.path.isfile(SD_filename) == False:
	create_SD(N_particles, nr_sp_states, sp_matrix, SD_filename)







