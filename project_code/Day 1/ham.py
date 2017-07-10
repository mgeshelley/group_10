import numpy as np

"""
This a function that will build the Hamiltonian matrix
that will use the single particle states
"""

def Hamiltonian():
	#s_d is slater determinant
	s_d = np.loadtxt("iso.int", comments = "!", skiprows=3)
	#nos is number of states
	nos = s_d.shape[0]
	# neo is the hamiltonian with zero elements
	neo = np.zeros((nos, nos))
	# i are the lines and j are the columns of neo
	for alpha in range(1, nos+1, 1):
		for tbme in range(1, nos+1, 1):
			#fetching the p, q, r, s indices from the text file
			v = s_d[6]
			p = s_d[0]
			q = s_d[1]
			r = s_d[2]
			s = s_d[3]


	print neo

Hamiltonian()


