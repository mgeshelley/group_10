import numpy as np

"""
This a function that will build the Hamiltonian matrix
that will use the single particle states
"""

def Hamiltonian():
	# s_d is slater determinant
	s_d = np.loadtxt("iso.int", comments = "!", skiprows=3)
	# nos is number of states
	nos = s_d.shape[0]
	# neo is the hamiltonian with zero elements
	neo = np.zeros((nos, nos))
	for alpha in range(0, nos, 1):
		for tbme in range(0, nos, 1):
			# fetching the p, q, r, s indices from the text file
			v = s_d[tbme,6]
			p = s_d[tbme,0]
			q = s_d[tbme,1]
			r = s_d[tbme,2]
			s = s_d[tbme,3]
			# stating the restriction on v
			if v == 0:
				continue
			else:
			# applying the two body operator
				r = r - 1
				s = s - 1
				q = q + 1
				p = p + 1

			for beta in range(0, nos, 1):
				if p == s_d[beta,0]:
					if q == s_d[beta,1]:
						if s == s_d[beta,2]:
							if r == s_d[beta,3]:
								#phase needs to be entered later
								neo[alpha,beta] = neo[alpha,beta] + v
								neo[beta,alpha] = neo[beta,alpha] + v
								print "yes"

	print neo								

Hamiltonian()
