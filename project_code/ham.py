import numpy as np
import sys

nr_sp_states = 8
N_particles = 4

folder_name = 'table_files/'


def Hamiltonian_one_body(N_particles, nr_sp_states, SD_filename, tbme_filename):
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
    
    hamiltonian:    ndarray,
    				Hamiltonian matrix with the one-body interaction terms
	"""

	# The file with Slater Determinants (s_d) is loaded [index, sp states]
	s_d = np.loadtxt(SD_filename, comments = "!", skiprows=0)
	# number of Slater determinants
	nr_sd = s_d.shape[0]

	# Read the single-particle energies from the first line of .int file 
	sp_energies = np.genfromtxt(tbme_filename, comments = "!", skip_header=2, max_rows=1)[1:5]	

	# Make a matrix with the single-particle energies on the diagonal <p|h_1body|q>
	H_diag = np.zeros((nr_sp_states, nr_sp_states))
	for i in range(nr_sp_states):
		H_diag[i,i] = sp_energies[i/2] #this is an integer division 

	# initialize to zero the Hamiltonian <beta_SD|H|alpha_SD>
	hamiltonian = np.zeros((nr_sd, nr_sd))

	# loop over <beta_SD|
	for beta in range(0, nr_sd, 1):

		beta_list = s_d[beta,1:]
		# loop over |alpha_SD>
		for alpha in range(0, nr_sd, 1):
			
			# sum_p,q <p|h_1body|q> a_p^+ a_q
			for p in range(1,nr_sp_states+1):
				for q in range(1,nr_sp_states+1):

					alpha_list = s_d[alpha,1:]
					# index = -1 means not index found

					# this part substitutes a_p^+ with a_i^+ if q == i, producing |alpha'_SD> 
					# if it does not exist i that is equal to q, the code executes continue
					index = -1
					index_bol = True
					i = 0 # variable to count the position in alpha_list 
				
					while index_bol and i < N_particles:
				
						if q == int(alpha_list[i]):
							index = i
							index_bol = False
						else:
							i += 1
				
					if index < 0:
						continue

					alpha_list = np.insert(alpha_list,index,p)
					alpha_list = np.delete(alpha_list,index+1)
					alpha_list = np.sort(alpha_list)

					# if <beta|alpha'> = 1 the matrix element H_diag(p,q) is added to the Hamiltonian matrix
					if np.array_equal(beta_list,alpha_list):
						hamiltonian[beta, alpha] = hamiltonian[beta, alpha] + H_diag[p-1,q-1]
	# print the Hamiltonian matrix
	# print hamiltonian
	return hamiltonian

##########################################################################################################


#def Hamiltonian_one_body(N_particles, nr_sp_states, SD_filename, tbme_filename):
def Hamiltonian():  #used only for testing 

	# The file with Slater Determinants (s_d) is loaded [index, sp states]
	s_d = np.loadtxt(folder_name+"3s_slater_det.sd", comments = "!", skiprows=0) #only for testing
	#s_d = np.loadtxt(SD_filename, comments = "!", skiprows=0)
	
	# number of Slater determinants
	nr_sd = s_d.shape[0]

	# Read the two-body matrix elements from the .int file 
	two_body_me = np.loadtxt(folder_name+"pairing_g1.int", comments = "!", skiprows=3) #only for testing
	#two_body_me = np.loadtxt(tbme_filename, comments = "!", skiprows=3)
	
	
	# nr_2bme is the number of two body matrix elements	
	nr_2bme = two_body_me.shape[0]
	if np.genfromtxt(folder_name+"pairing_g1.int", comments = "!", skip_header=2, max_rows=1)[0] != nr_2bme:
		sys.exit("ERROR: Dimension of 2-body matrix not consistent!!!") #only for testing
	#if np.genfromtxt(tbme_filename, comments = "!", skip_header=2, max_rows=1)[0] != nr_2bme:
	#	sys.exit("ERROR: Dimension of 2-body matrix not consistent!!!")


	# initialize to zero the Hamiltonian <beta_SD|H|alpha_SD>
	hamiltonian_2body = np.zeros((nr_sd, nr_sd))


# loop over <beta_SD|
	for beta in range(0, nr_sd, 1):

		beta_list = s_d[beta,1:]
		# loop over |alpha_SD>
		for alpha in range(0, nr_sd, 1):
			
			# sum_p,q,r,s <pq|v_2body|rs> a_p^+ a_q^+ a_s a_r:

				# Loop over two body me
			for tbme in range(0, nr_2bme, 1):
				alpha_list = s_d[alpha,1:]
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
	print hamiltonian_2body

'''
					if s in alpha_list and r in s_d[alpha,1:]:
						# Temporarily saving variables s, r
						stemp = s
						rtemp = r

						alpha_temp = s_d[alpha,1:5]

						counter += 1

						# Renaming these
						stemp = np.where(alpha_temp == s)
						rtemp = np.where(alpha_temp == r)

						print 'b', s_d[beta,1:5]
						
						alpha_temp[stemp] = p
						alpha_temp[rtemp] = q
						
						print 'a', s_d[beta,1:5]

						print s_d2[beta,1:5]
						alpha_temp = np.sort(alpha_temp)
						alpha_temp = alpha_temp.astype(int)
						#print alpha_temp
						#print s_d[beta,1:5]
						#sys.exit()

						
						
						if np.array_equal(alpha_temp,s_d2[beta,1:5]):
							neo[alpha,beta] = neo[alpha,beta] + v
							print alpha_temp
							print 'if'
							if alpha != beta:
								neo[beta,alpha] = neo[alpha,beta] + v

						# UP UNTIL HERE IT WORKS
						"""for slater in range(0,nr_sd,1):
							beta = s_d[slater, 1:5]
							#HERE WE NEED A WAY TO PICK ONLY THE SDS THAT HAVE
							#ALL ELEMENTS DIFFERENT!!! (P!=Q!=R!=S)

							print beta
						"""

						#neo[alpha,beta] = neo[alpha,beta] + v

						#if alpha != beta:
						#	neo[beta,alpha] = neo[beta,alpha] + v
							# print 'YES'
						#	print neo

						# print 'yes'
						


						s = stemp
						r = rtemp

					else:
						phase = 0

						# print s, r
					# else:
						# print 'yes'

					# #phase needs to be entered later

	print neo
'''
Hamiltonian()

