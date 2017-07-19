import numpy as np
import sys
import matplotlib.pyplot as plt


g_list = np.linspace(-1,1,5)
N = 6
E = np.zeros(len(g_list))

plt.figure(1)
for j in range(6):
    for i in range(len(g_list)):

        g = g_list[i]

        analytical_hamiltonian = -g*np.ones([N,N])
        np.fill_diagonal(analytical_hamiltonian, 2.-2.*g)
        np.fill_diagonal(np.rot90(analytical_hamiltonian), 0)

        for n in range(N):
            analytical_hamiltonian[n,n] += 2*n

        for m in range(5,2,-1):
            analytical_hamiltonian[m,m] = analytical_hamiltonian[m-1,m-1]

        eigval, eigvec = np.linalg.eigh(analytical_hamiltonian)

        E[i] = eigval[j]

    if j==3:
        plt.plot(g_list, E, 'kx')
    else:
        plt.plot(g_list, E)


plt.xlabel('g [A.u]')
plt.ylabel('Energy [A.u]')
plt.legend(['E_0', 'E_1', 'E_2', 'E_3', 'E_4', 'E_5'])
#plt.title('The energy levels as a function of g')

plt.savefig('figures/eigval_vs_g.png')
#plt.show()






