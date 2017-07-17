# Creates the one-body and the two body hamiltonian matrix for the pairing problem

import numpy as np
import sys

def Hamiltonian_one_body(N_particles, nr_sp_states, matrix, SD_filename):
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
	
	''' THIS PART IS NO LONGER NECESSARY WITH sd-model space
	H_diag = np.zeros((nr_sp_states, nr_sp_states))
	for i in range(nr_sp_states):
		H_diag[i,i] = sp_energies[i] #this is an integer division
	'''

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
					eps_i = sp_energies[alpha_list[i] - 1] # to account for the energy of the sp_states with label i
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
	s_d = np.loadtxt(SD_filename, comments = "!", skiprows=0, dtype = 'int')

	# number of Slater determinants
	nr_sd = s_d.shape[0]

	# Read the two-body matrix elements from the .int file
	#two_body_me = np.loadtxt(folder_name+"pairing_g1.int", comments = "!", skiprows=3) #only for testing
	two_body_me = np.loadtxt(tbme_filename, comments = "!", skiprows=3)


	# nr_2bme is the number of two body matrix elements
	nr_2bme = two_body_me.shape[0]
	
	#if np.genfromtxt(folder_name+"pairing_g1.int", comments = "!", skip_header=2, max_rows=1)[0] != nr_2bme:
	#	sys.exit("ERROR: Dimension of 2-body matrix not consistent!!!") #only for testing

	''' THIS GIVE AN ERROR CORRECT IT
	if np.genfromtxt(tbme_filename, comments = "!", skip_header=1, max_rows=1)[0] != nr_2bme:
		sys.exit("ERROR: Dimension of 2-body matrix not consistent!!!")
	'''
	two_body_matrix = np.empty((nr_sp_states+1,nr_sp_states+1,nr_sp_states+1,nr_sp_states+1))
	for k in range(0,nr_2bme):
		two_body_matrix[int(two_body_me[k,0]),int(two_body_me[k,1]), \
						int(two_body_me[k,2]),int(two_body_me[k,3])] = two_body_me[k,4] 


	# initialize to zero the Hamiltonian <beta_SD|H|alpha_SD>
	hamiltonian_2body = np.zeros((nr_sd, nr_sd))


	# loop over <beta_SD|
	for beta in range(0, nr_sd, 1):

		beta_list = s_d[beta,1:]
		# loop over |alpha_SD>
		for alpha in range(beta, nr_sd, 1):
			alpha_list = s_d[alpha,1:]

			# THIS WAY TO FIND THE DIFFERENCES BETWEEN TWO LISTS DOES NOT WORK PROPERLY
			alpha_beta_compare = list(set(beta_list).symmetric_difference(set(alpha_list)) )

			# AlphA and beta are same
			if len(alpha_beta_compare) == 0:
				# Sum over i and j (all 2-body matrix elements)
				for i in range(0,N_particles):
					for j in range(0,N_particles):
						a = alpha_list[i]
						b = alpha_list[j]

						# If 2-body me exists, add to Hamiltonian
						if two_body_matrix[a,b,a,b] != 0.0:
							mat_element = 0.5 * two_body_matrix[a,b,a,b]
							hamiltonian_2body[beta,alpha] = hamiltonian_2body[beta,alpha] + mat_element


			# Alpha and beta have one difference
			elif len(alpha_beta_compare) == 2:
				print beta_list, alpha_list, alpha_beta_compare
				sys.exit()
				# phase from the action of the first annihilation operator
				#print list(alpha_list).index(alpha_beta_compare[1])
				phase = (-1)**(list(alpha_list).index(alpha_beta_compare[1]))
				alpha_list_red = np.delete(alpha_list,list(alpha_list).index(alpha_beta_compare[1]))
				exp_phase1 = 0
				# phase from the action of the first creation operator
				for index in range(0, N_particles):
					if alpha_beta_compare[0] > alpha_list_red[index]:
						exp_phase1 = index+1
					else:
						break

				phase = phase*(-1)**exp_phase1
				# Sum over i and j (all 2-body matrix elements)
				for i in range(0,N_particles):
					b = alpha_list[i]
					a = alpha_beta_compare[0]
					c = alpha_beta_compare[1]

					# If 2-body me exists, add to Hamiltonian
					if two_body_matrix[a,b,c,b] != 0.0:
						mat_element = two_body_matrix[a,b,c,b]*phase
						hamiltonian_2body[beta,alpha] = hamiltonian_2body[beta,alpha] + mat_element



			# Alpha and beta have two differences
			elif len(alpha_beta_compare) == 4:
				# phase from the action of the first annihilation operator
				phase = (-1)**alpha_list.index(alpha_beta_compare[2])
				alpha_list_red = np.delete(alpha_list,alpha_list.index(alpha_beta_compare[2]))
				# phase from the action of the second annihilation operator
				phase1 = (-1)**alpha_list_red.index(alpha_beta_compare[3])
				alpha_list_red_red = np.delete(alpha_list_red,alpha_list_red.index(alpha_beta_compare[3]))
				exp_phase2 = 0
				exp_phase3 = 0
				# phase from the action of the second creation operator
				for index in range(0, N_particles-2):
					if alpha_beta_compare[1] > alpha_list_red_red[index]:
						exp_phase2 = index+1
					else:
						break
				# phase from the action of the first creation operator
				for index1 in range(0, N_particles-2):
					if alpha_beta_compare[0] > alpha_list_red_red[index1]:
						exp_phase3 = index1+1
					else:
						break
				phase = phase*phase1*(-1)**(exp_phase2+exp_phase3)

				a = alpha_beta_compare[0]
				b = alpha_beta_compare[1]
				c = alpha_beta_compare[2]
				d = alpha_beta_compare[3]

				# If 2-body me exists, add to Hamiltonian
				if two_body_matrix[a,b,c,d] != 0.0:
					mat_element = two_body_matrix[a,b,c,d]*phase
					hamiltonian_2body[beta,alpha] = hamiltonian_2body[beta,alpha] + mat_element




			# # sum_p,q,r,s <pq|v_2body|rs> a_p^+ a_q^+ a_s a_r:
			#
			# 	# Loop over two body me
			# for tbme in range(0, nr_2bme, 1):
			#
			#
			#
			# 	# fetching the p, q, r, s indices from the text file
			# 	p = int(two_body_me[tbme,0])
			# 	q = int(two_body_me[tbme,1])
			# 	r = int(two_body_me[tbme,2])
			# 	s = int(two_body_me[tbme,3])
			# 	v_pqrs = two_body_me[tbme,6]
			# 	# stating the restriction on v
			# 	#print v_pqrs
			#
			# 	if v_pqrs != 0:
			# 		#print v_pqrs
			# 		index_r = -1
			# 		index_r_bol = True
			# 		i = 0 # variable to count the position in alpha_list
			#
			# 		while index_r_bol and i < N_particles:
			#
			# 			if r == int(alpha_list[i]):
			# 				index_r = i
			# 				index_r_bol = False
			# 			else:
			# 				i += 1
			#
			# 		if index_r < 0:
			# 			continue
			#
			# 		alpha_list = np.delete(alpha_list,index_r) # remove r state from list
			#
			# 		index_s = -1
			# 		index_s_bol = True
			# 		j = 0 # variable to count the position in alpha_list
			#
			# 		while index_s_bol and j < N_particles-1:
			#
			# 			if s == int(alpha_list[j]):
			# 				index_s = j
			# 				index_s_bol = False
			# 			else:
			# 				j += 1
			#
			# 		if index_s < 0:
			# 			continue
			#
			# 		alpha_list = np.delete(alpha_list,index_s) # remove s state from list
			#
			# 		# insert phase that should be related with index_r and index_s and the permutation of a^+
			# 		alpha_list = np.append(alpha_list,p)
			# 		alpha_list = np.append(alpha_list,q)
			#
			# 		alpha_list = np.sort(alpha_list)
			#
			# 		# if <beta|alpha'> = 1 the matrix element H_diag(p,q) is added to the Hamiltonian matrix
			# 		if np.array_equal(beta_list,alpha_list):
			# 			hamiltonian_2body[beta, alpha] = hamiltonian_2body[beta, alpha] + v_pqrs
			hamiltonian_2body[alpha, beta] = hamiltonian_2body[beta, alpha]
	return hamiltonian_2body
