# Functions to read files

import numpy as np

def read_sd_basis(sp_basis_filename):
    """
    Reads in data from the sd.sp file given from Morten 

    Input   

    sp_basis_filename:  string,
                filename of the file of the sd shell basis

    Returns 
    
    sp_matrix:  ndarray,
                matrix containing the single particle states and the quantum numbers.
                data organized in the following way, columns labeld as:
                index, n, l, 2j, 2m_j, single-particle energies
    """

    sp_matrix = np.genfromtxt(sp_basis_filename,skip_header=1, usecols=(0,1,2,3,4,5))

    return sp_matrix



def read_basis(sp_basis_filename):
    """
    Reads in data from the .sp file (not the sd shell)

    Input   

    sp_basis_filename:  string,
                filename of the basis file to read data from

    Returns 
    
    particle:   ndarray,
                type of particle
    A_core:     float,
                mass number for the core
    Z_core:     float,
                proton nrumber for the core
    nr_sp_states: float,    
                the total number of single-particle states
    nr_groups:  float,
                the total number of group of particles 
    nr_sp_n:    float, 
                number of neutron single-particle states
    nr_sp_p:    float,
                number of proton single-particle states
    sp_matrix:  ndarray,
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

def read_SD(N_particles, SD_filename):
    """
    Reads in data from the .sd file

    Input   

    SD_filename:string,
                filename of the slater determinant file to read data from

    Returns 
    
    SD_matrix:  ndarray,
                matrix containing the slater determinants.
                Every row identifies a different slater determinant.
                First column: the index of the slater determinants.
                In the last four columns the labels of the occupied single particle states are listed.
                
    """

    SD_matrix = np.genfromtxt(SD_filename)

    return SD_matrix

