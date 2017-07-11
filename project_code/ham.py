import numpy as np

"""
This a function that will build the Hamiltonian matrix
that will use the single particle states
"""

def Hamiltonian():
	# s_d is slater determinant
	s_d = np.loadtxt("3s_slater_det.sd", comments = "!", skiprows=0)
	# nos is number of states
	nos = s_d.shape[0]

	# Read in two-body matrix elements
	two_body_me = np.loadtxt("pairing_g1.int", comments = "!", skiprows=5)
	# nme is the number of two body matrix elements
	nme = two_body_me.shape[0]

	# neo is the hamiltonian with zero elements
	neo = np.zeros((nos, nos))
	# Starting loop over NSD
	for alpha in range(0, nos, 1):
		print s_d[alpha,1:5]

		# Loop over two body me
		for tbme in range(0, nme, 1):
			# fetching the p, q, r, s indices from the text file
			v = two_body_me[tbme,6]
			p = two_body_me[tbme,0]
			q = two_body_me[tbme,1]
			r = two_body_me[tbme,2]
			s = two_body_me[tbme,3]
			# stating the restriction on v
			if v == 0:
				continue
			else:



			# applying the two body operator

				r = int(round(r))
				s = int(round(s))
				q = int(round(q))
				p = int(round(p))




			for beta in range(0, nos, 1):
				if s in s_d[beta,:] and r in s_d[beta,:]:
					s = p
					r = q
					neo[alpha,beta] = neo[alpha,beta] + v
					neo[beta,alpha] = neo[beta,alpha] + v

					print neo

				else:
					phase = 0



					# print s, r
				# else:
					# print 'yes'





				# #phase needs to be entered later


	# print neo


Hamiltonian()