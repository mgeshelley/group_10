# This file contains a function to read in the input from the command line

import numpy as np


class Error(Exception):
    """Base class for other exceptions"""
    pass

class ValueBelowZeroError(Error):
    """Raised when the input value is too small"""
    pass

class minValueLargerThanMaxError(Error):
    """Raised when the input value is too large"""
    pass

class IsosError(Error):
    """Raised when the input value is not a n or np"""
    pass

def command_line_input():

    while True:
        try:
            nmin, nmax = map(int,raw_input("Write: nmin nmax ").split(' '))
            if np.logical_or(nmin < 0, nmax < 0):
                raise ValueBelowZeroError
            if nmin > nmax:
                raise minValueLargerThanMaxError
        except ValueBelowZeroError:
            print("Please provide numbers above zero.")
            #better try again... Return to the start of the loop
            continue
        except ValueError:
            print("Please provide integers.")
            #better try again... Return to the start of the loop
            continue
        except minValueLargerThanMaxError:
            print("The maximum value must be larger than the minimum value.")
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
            print("Please provide numbers above zero.")
            continue
        except ValueError:
            print("Please provide integers.")
            continue
        except minValueLargerThanMaxError:
            print("The maximum value must be larger than the minimum value.")
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
            print("Please provide numbers above zero.")
            continue
        except ValueError:
            print("Please provide integers.")
            continue
        except minValueLargerThanMaxError:
            print("The maximum value must be larger than the minimum value.")
            continue
        else:
            break

    while True:
        try:
            isos = raw_input("Write: isospin species (n or np) ")
            if isos not in ['n', 'np']:
                raise IsosError

        except IsosError:
            print("Please write either 'n' or 'np'.")
        else:
            break


    while True:
        try:
            g = float(raw_input("Write: g "))
        except ValueError:
            print("Please provide g as a float / real number.")

        else:
            break

    while True:
        try:        
            N_particles = int(raw_input("Write: N_particles "))
        except ValueBelowZeroError:
            print("Please provide numbers above zero.")
            continue
        except ValueError:
            print("Please provide the number of particles as an integer.")
            continue
        else:
            break
           
    return nmax, nmin, lmax, lmin, jmin, jmax, isos, g, N_particles

