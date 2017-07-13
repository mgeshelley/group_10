import numpy as np
import sys

"""
This a function that will build the Hamiltonian matrix
that will use the single particle states
"""

folder_name = 'table_files/'


def Hamiltonian_one_body():
	counter = 0 
	# s_d is slater determinant
	s_d = np.loadtxt(folder_name+"3s_slater_det.sd", comments = "!", skiprows=0)

	# nos is number of states
	nr_sd = s_d.shape[0]

	# Read in one-body matrix elements
	one_body_me = np.genfromtxt(folder_name+"pairing_g1.int", comments = "!", skip_header=2, max_rows=1)[1:5]	
	#print one_body_me

	nr_sp_states = 8
	Nr_particles = 4

	H_diag = np.zeros((nr_sp_states, nr_sp_states))
	for i in range(nr_sp_states):
		H_diag[i,i] = one_body_me[i/2] #this is an integer division 
	#print H_diag	
	# neo is the hamiltonian with zero elements
	hamiltonian = np.zeros((nr_sd, nr_sd))
	#print hamiltonian
	#sys.exit()
	# Starting loop over NSD
	count = 0
	for beta in range(0, nr_sd, 1):
		beta_list = s_d[beta,1:]
		for alpha in range(0, nr_sd, 1):
				# Loop over two body me
			
			for p in range(1,nr_sp_states+1):
				for q in range(1,nr_sp_states+1):
					alpha_list = s_d[alpha,1:]
					index = -1
					index_bol = True
					i = 0
				
					while index_bol and i < Nr_particles:
				
						if q == int(alpha_list[i]):
							index = i
							index_bol = False
						else:
							i += 1
				
					count +=1
				
					#if index < 0:
					#	continue		
					#index = np.argwhere(alpha_list-q)
					#print index
					#print alpha_list
					#sys.exit()
					alpha_list = np.insert(alpha_list,index,p)
					#alpha_list = alpha_list.add(p)
					alpha_list = np.delete(alpha_list,index+1)
					alpha_list = np.sort(alpha_list)

					if np.array_equal(beta_list,alpha_list):
						hamiltonian[beta, alpha] = hamiltonian[beta, alpha] + H_diag[p-1,q-1]

	print hamiltonian
					
#					if count > 1:
#						sys.exit()
					#if q in s_d[alpha]: #if any s_q[] is equal to q
					
						

			
Hamiltonian_one_body()			


####################################################################################


def Hamiltonian():
	counter = 0 
	# s_d is slater determinant
	s_d = np.loadtxt(folder_name+"3s_slater_det.sd", comments = "!", skiprows=0)

	s_d2 = np.loadtxt(folder_name+"3s_slater_det.sd", comments = "!", skiprows=0)
	
	# nos is number of states
	nos = s_d.shape[0]

	# Read in two-body matrix elements
	two_body_me = np.loadtxt(folder_name+"pairing_g1.int", comments = "!", skiprows=3)

	
	
	# nme is the number of two body matrix elements	
	nme = two_body_me.shape[0]
	if np.genfromtxt(folder_name+"pairing_g1.int", comments = "!", skip_header=2, max_rows=1)[0] != nme:
		sys.exit("ERROR: Dimention of tbmatrix not consistent!!!")


	# neo is the hamiltonian with zero elements
	neo = np.zeros((nos, nos))

	# Starting loop over NSD
	for beta in range(0, nos, 1):
		for alpha in range(0, nos, 1):
				# Loop over two body me
			for tbme in range(0, nme, 1):
				# fetching the p, q, r, s indices from the text file
				p = two_body_me[tbme,0]
				q = two_body_me[tbme,1]
				r = two_body_me[tbme,2]
				s = two_body_me[tbme,3]
				v = two_body_me[tbme,6]
				# stating the restriction on v

				if v == 0:
					continue
				else:
				# applying the two body operator
					r = int(round(r))
					s = int(round(s))
					q = int(round(q))
					p = int(round(p))

					if s in s_d[alpha,1:] and r in s_d[alpha,1:]:
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
						"""for slater in range(0,nos,1):
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



