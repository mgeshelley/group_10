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


def read_SD(N_particles, SD_filename):
    """
    Reads in data from the .sd file

    Input   

    SD_filename:string,
                filename of the slater determinant file to read data from

    Returns 
    
    SlaterD_matrix:  ndarray,
                matrix containing the slater determinants.
                Every row identifies a different slater determinant.
                First column: the index of the slater determinants.
                In the last four columns the labels of the occupied single particle states are listed.
                
    """

    SlaterD_matrix = np.genfromtxt(SD_filename)
    #print SlaterD_matrix
    return SlaterD_matrix

