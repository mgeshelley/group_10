# This file contains a function to read in the input from the command line

import numpy as np

# These classes are needed for the function below. 
class Error(Exception):
    """Base class for other exceptions"""
    pass

class ValueBelowZeroError(Error):
    """Raised when the input value is below zero"""
    pass

class minValueLargerThanMaxError(Error):
    """Raised when the min value is larger than the max value"""
    pass

class IsosError(Error):
    """Raised when the input value is not 'n' or 'np'"""
    pass

def command_line_input():
    """
    This function asks the user to provide the input parameter on the command line. 
    It makes sure that the provided input is of correct type and within the allowed limits.
    If the input is not correct the program gives an error message and asks the user to provide
    the input again. 
    
    Input (None)

    Returns 
    
    nmin:       int,
                minumum n

    nmax:       int,
                maximum n

    lmin:       int,
                minumum l

    lmax:       int,
                maximum l

    jmin:       int,
                minumum j

    jmax:       int,
                maximum j

    isos:       string,
                the species of the nucleons for the simulation

    g:          float, 
                the pairing constant

    N_particles: int,
                the number of particles in the simulation

    """

    while True:
        try:
            nmin, nmax = map(int,raw_input("Write: nmin nmax ").split(' '))

            if np.logical_or(nmin < 0, nmax < 0):
                raise ValueBelowZeroError
            if nmin > nmax:
                raise minValueLargerThanMaxError
        except ValueBelowZeroError:
            print("ERROR: Please provide numbers above zero.")
            #better try again... Return to the start of the loop
            continue
        except ValueError:
            print("ERROR: Please provide integers (without whitespace behind the last number).")
            #better try again... Return to the start of the loop
            continue
        except minValueLargerThanMaxError:
            print("ERROR: The maximum value must be larger than the minimum value.")
            #better try again... Return to the start of the loop
            continue
        else:
            #age was successfully parsed!
            #we're ready to exit the loop.
            break

    while True:
        try:
            lmin, lmax = map(int,raw_input("Write: lmin lmax ").split(' '))
            if np.logical_or(lmin < 0, lmax < 0):
                raise ValueBelowZeroError
            if lmin > lmax:
                raise minValueLargerThanMaxError

        except ValueBelowZeroError:
            print("ERROR: Please provide numbers above zero.")
            continue
        except ValueError:
            print("ERROR: Please provide integers (without whitespace behind the last number).")
            continue
        except minValueLargerThanMaxError:
            print("ERROR: The maximum value must be larger than the minimum value.")
            continue
        else:
            break

    while True:
        try:
            jmin, jmax = map(int,raw_input("Write: 2jmin 2jmax ").split(' '))
            if np.logical_or(jmin < 0, jmax < 0):
                raise ValueBelowZeroError
            if jmin > jmax:
                raise minValueLargerThanMaxError
            
        except ValueBelowZeroError:
            print("ERROR: Please provide numbers above zero.")
            continue
        except ValueError:
            print("ERROR: Please provide integers (without whitespace behind the last number).")
            continue
        except minValueLargerThanMaxError:
            print("ERROR: The maximum value must be larger than the minimum value.")
            continue
        else:
            break

    while True:
        try:
            isos = raw_input("Write: isospin species ('n' or 'np' without whitespace behind) ")
            if isos not in ['n', 'np']:
                raise IsosError

        except IsosError:
            print("ERROR: Please write either 'n' or 'np'.")
        else:
            break

    while True:
        try:
            g = float(raw_input("Write: g "))
        except ValueError:
            print("ERROR: Please provide g as a float / real number (without whitespace behind the last number).")

        else:
            break

    while True:
        try:        
            N_particles = int(raw_input("Write: N_particles "))
        except ValueBelowZeroError:
            print("ERROR: Please provide numbers above zero.")
            continue
        except ValueError:
            print("ERROR: Please provide the number of particles as an integer (without whitespace behind the last number).")
            continue
        else:
            break
           
    return nmin, nmax, lmin, lmax, jmin, jmax, isos, g, N_particles, sp_basis_filename, SD_filename, tbme_filename


def give_file_names(g):
    folder_name = 'table_files/'

    sp_basis_filename = folder_name+'3s.sp'
    SD_filename = folder_name+"3s_slater_det.sd"
    tbme_filename = folder_name+"pairing_g%s.int" %(g) 

    return sp_basis_filename, SD_filename, tbme_filename



