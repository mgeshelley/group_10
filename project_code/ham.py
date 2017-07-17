# Creates the one-body and the two body hamiltonian matrix for the pairing problem

import numpy as np
import sys

def Hamiltonian_one_body(N_particles, nr_sp_states, matrix, SD_filename, tbme_filename):
	"""
	This function builds the one-body part of the Hamiltonian <beta_SD|H|alpha_SD>

	To call it
	Hamiltonian_one_body(N_particles, nr_sp_states, SD_filename, tbme_filename)

	Input

    N_particles:    float,
                    number of particles
    nr_sp_states:   float,
                    the total number of single-particle states
    SD_filename:    string,
                	filename of the file with the Slater Determinants
    tbme_filename:  string,
                	filename of the file with the interaction .int

    Output

    hamiltonian_1body:    ndarray,
    				Hamiltonian matrix with the one-body interaction terms
	"""

	nr_sp_states = int(nr_sp_states)
	N_particles = int(N_particles)

	# The file with Slater Determinants (s_d) is loaded [index, sp states]
	s_d = np.loadtxt(SD_filename, comments = "!", skiprows=0, dtype = 'int')
	# number of Slater determinants
	nr_sd = s_d.shape[0]

	# Read the single-particle energies from the first line of .int file
	sp_energies = matrix[:,-1]

	# Make a matrix with the single-particle energies on the diagonal <p|h_1body|q>
	H_diag = np.zeros((nr_sp_states, nr_sp_states))
	for i in range(nr_sp_states):
		H_diag[i,i] = sp_energies[i] #this is an integer division

	# initialize to zero the Hamiltonian <beta_SD|H|alpha_SD>
	hamiltonian_1body = np.zeros((nr_sd, nr_sd))

	# loop over <beta_SD|
	for beta in range(0, nr_sd, 1):

		beta_list = s_d[beta,1:]
		# loop over |alpha_SD>
		for alpha in range(0, nr_sd, 1):

			alpha_list = s_d[alpha,1:]
			# index = -1 means not index found

			# Add single-particle energies to diagonal of Hamiltonian
			if alpha == beta:

				for i in range(0,N_particles):
					eps_i = sp_energies[alpha_list[i] - 1]
					hamiltonian_1body[beta, alpha] = hamiltonian_1body[beta, alpha] + eps_i

	return hamiltonian_1body


##########################################################################################################


def Hamiltonian_two_body(N_particles, nr_sp_states, SD_filename, tbme_filename):

	"""
	This function builds the two-body part of the Hamiltonian <beta_SD|H|alpha_SD>

	To call it
	Hamiltonian_two_body(N_particles, nr_sp_states, SD_filename, tbme_filename)

	Input

    N_particles:    float,
                    number of particles
    nr_sp_states:   float,
                    the total number of single-particle states
    SD_filename:    string,
                	filename of the file with the Slater Determinants
    tbme_filename:  string,
                	filename of the file with the interaction .int

    Output

    hamiltonian_2body:    ndarray,
    				Hamiltonian matrix with the one-body interaction terms
	"""

	nr_sp_states = int(nr_sp_states)
	N_particles = int(N_particles)

	# The file with Slater Determinants (s_d) is loaded [index, sp states]
	#s_d = np.loadtxt(folder_name+"3s_slater_det.sd", comments = "!", skiprows=0) #only for testing
	s_d = np.loadtxt(SD_filename, comments = "!", skiprows=0)

	# number of Slater determinants
	nr_sd = s_d.shape[0]

	# Read the two-body matrix elements from the .int file
	#two_body_me = np.loadtxt(folder_name+"pairing_g1.int", comments = "!", skiprows=3) #only for testing
	two_body_me = np.loadtxt(tbme_filename, comments = "!", skiprows=3)


	# nr_2bme is the number of two body matrix elements
	nr_2bme = two_body_me.shape[0]
	#if np.genfromtxt(folder_name+"pairing_g1.int", comments = "!", skip_header=2, max_rows=1)[0] != nr_2bme:
	#	sys.exit("ERROR: Dimension of 2-body matrix not consistent!!!") #only for testing
	if np.genfromtxt(tbme_filename, comments = "!", skip_header=2, max_rows=1)[0] != nr_2bme:
		sys.exit("ERROR: Dimension of 2-body matrix not consistent!!!")


	# initialize to zero the Hamiltonian <beta_SD|H|alpha_SD>
	hamiltonian_2body = np.zeros((nr_sd, nr_sd))


	# loop over <beta_SD|
	for beta in range(0, nr_sd, 1):

		beta_list = s_d[beta,1:]
		# loop over |alpha_SD>
		for alpha in range(0, nr_sd, 1):
			alpha_list = s_d[alpha,1:]

			alpha_beta_compare = list( set(alpha_list).symmetric_difference(set(beta_list)) )
			# if len(alpha_beta_compare) == 0:
			# 	# Sum over i and j (all 2-body matrix elements)
			# 	for i in range(0,nr_sp_states):
			#
			# elif len(alpha_beta_compare) == 2:
			#
			# elif len(alpha_beta_compare) == 4:

			sum_p,q,r,s <pq|v_2body|rs> a_p^+ a_q^+ a_s a_r:

				# Loop over two body me
			for tbme in range(0, nr_2bme, 1):



				# fetching the p, q, r, s indices from the text file
				p = int(two_body_me[tbme,0])
				q = int(two_body_me[tbme,1])
				r = int(two_body_me[tbme,2])
				s = int(two_body_me[tbme,3])
				v_pqrs = two_body_me[tbme,6]
				# stating the restriction on v
				#print v_pqrs

				if v_pqrs != 0:
					#print v_pqrs
					index_r = -1
					index_r_bol = True
					i = 0 # variable to count the position in alpha_list

					while index_r_bol and i < N_particles:

						if r == int(alpha_list[i]):
							index_r = i
							index_r_bol = False
						else:
							i += 1

					if index_r < 0:
						continue

					alpha_list = np.delete(alpha_list,index_r) # remove r state from list

					index_s = -1
					index_s_bol = True
					j = 0 # variable to count the position in alpha_list

					while index_s_bol and j < N_particles-1:

						if s == int(alpha_list[j]):
							index_s = j
							index_s_bol = False
						else:
							j += 1

					if index_s < 0:
						continue

					alpha_list = np.delete(alpha_list,index_s) # remove s state from list

					# insert phase that should be related with index_r and index_s and the permutation of a^+
					alpha_list = np.append(alpha_list,p)
					alpha_list = np.append(alpha_list,q)

					alpha_list = np.sort(alpha_list)

					# if <beta|alpha'> = 1 the matrix element H_diag(p,q) is added to the Hamiltonian matrix
					if np.array_equal(beta_list,alpha_list):
						hamiltonian_2body[beta, alpha] = hamiltonian_2body[beta, alpha] + v_pqrs
			hamiltonian_2body[alpha, beta] = hamiltonian_2body[beta, alpha]
	return hamiltonian_2body
