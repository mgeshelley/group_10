# This file contains a function to read in the input from the command line

import numpy as np

# These classes are needed for the function below. 

class Error(Exception):
    """Base class for other exceptions"""
    pass

class ValueBelowZeroError(Error):
    """Raised when the input value is below zero"""
    pass


class CaseError(Error):
    """Raised when the input value is not 'pairing' or 'sd'"""
    pass

class FileNameError(Error):
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
    
    N_particles: int,
                the number of particles in the simulation

    case:       string,
                model space 'pairing' or 'sd'

    g:          float, 
                the pairing constant



    """

    standard_input = True

    while True:
        try:
            yn = raw_input("Whould you like default input? \ny/n: ")

            if yn not in ['y', 'n']:
                    raise FileNameError

            if yn == 'y':
            	N_particles = 4
            	case = 'sd'
            	g = 0
                print("\nDefault inputs: ")
                print("N_particles = %d ") %N_particles
                print("case = %s \n") %case

            if yn == 'n':
                standard_input = False
                

        except FileNameError:
            print("\nERROR: Please write either 'y' or 'n'.\n")

        else:
            break

    if not standard_input:

        while True:
            try:        
                N_particles = int(raw_input("Write: N_particles "))
            except ValueBelowZeroError:
                print("\nERROR: Please provide numbers above zero.\n")
                continue
            except ValueError:
                print("\nERROR: Please provide the number of particles as an integer (without whitespace behind the last number).\n")
                continue
            else:
                break



        while True:
            try:
                case = raw_input("Write: model space ('pairing' or 'sd' without whitespace behind) ")
                if case not in ['pairing', 'sd']:
                    raise CaseError

            except CaseError:
                print("\nERROR: Please write either 'pairing' or 'sd'.\n")
            else:
                break


        while True:
            try:
                g = float(raw_input("Write: g (if 'sd' write '0.0')"))
            except ValueError:
                print("\nERROR: Please provide g as a float / real number (without whitespace behind the last number).\n")

            else:
                break

    return N_particles, case, g




