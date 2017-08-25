# This file contains a function to read in the input from the command line

import numpy as np

def give_file_names(g, extension=''):
    folder_name = 'table_files/'

    sp_basis_filename = folder_name+'%s3s.sp' %extension
    SD_filename = folder_name+"%s3s_slater_det.sd" %extension
    tbme_filename = folder_name+"%spairing_g%s.int" %(extension, g) 

    return sp_basis_filename, SD_filename, tbme_filename

'''
def manual_input(model='pairing'):
    
    """
    "Standard" input parameters (when to lazy to give the input on the command line)
    
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
    if model=='pairing':
        
        nmin = 0
        nmax = 3
        lmin = 0
        lmax = 0
        jmin = 1
        jmax = 1
        isos = 'n'
        g = 1
        N_particles = 4 # read the number of particles in the system

    if model=='harmonic':
        #do stuff
        n = 0
        #...

    return nmin, nmax, lmin, lmax, jmin, jmax, isos, g, N_particles



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

class FileNameError(Error):
    """Raised when the input value is not 'n' or 'np'"""
    pass
class ExtensionError(Error):
    """Raised when the input value is not 'n' or 'np'"""
    pass

'''

'''
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

    standard_input = True

    while True:
        try:
            yn = raw_input("Whould you like standard input? \ny/n: ")

            if yn not in ['y', 'n']:
                    raise FileNameError

            if yn == 'y':
                nmin, nmax, lmin, lmax, jmin, jmax, isos, g, N_particles = manual_input()

            if yn == 'n':
                standard_input = False
                

        except FileNameError:
            print("\nERROR: Please write either 'y' or 'n'.\n")

        else:
            break

    if not standard_input:

        while True:
            try:
                nmin, nmax = map(int,raw_input("Write: nmin nmax ").split(' '))

                if np.logical_or(nmin < 0, nmax < 0):
                    raise ValueBelowZeroError
                if nmin > nmax:
                    raise minValueLargerThanMaxError
            except ValueBelowZeroError:
                print("\nERROR: Please provide numbers above zero.\n")
                #better try again... Return to the start of the loop
                continue
            except ValueError:
                print("\nERROR: Please provide integers (without whitespace behind the last number).\n")
                #better try again... Return to the start of the loop
                continue
            except minValueLargerThanMaxError:
                print("\nERROR: The maximum value must be larger than the minimum value.\n")
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
                print("\nERROR: Please provide numbers above zero.\n")
                continue
            except ValueError:
                print("\nERROR: Please provide integers (without whitespace behind the last number).\n")
                continue
            except minValueLargerThanMaxError:
                print("\nERROR: The maximum value must be larger than the minimum value.\n")
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
                print("\nERROR: Please provide numbers above zero.\n")
                continue
            except ValueError:
                print("\nERROR: Please provide integers (without whitespace behind the last number).\n")
                continue
            except minValueLargerThanMaxError:
                print("\nERROR: The maximum value must be larger than the minimum value.\n")
                continue
            else:
                break

        while True:
            try:
                isos = raw_input("Write: isospin species ('n' or 'np' without whitespace behind) ")
                if isos not in ['n', 'np']:
                    raise IsosError

            except IsosError:
                print("\nERROR: Please write either 'n' or 'np'.\n")
            else:
                break

        while True:
            try:
                g = float(raw_input("Write: g "))
            except ValueError:
                print("\nERROR: Please provide g as a float / real number (without whitespace behind the last number).\n")

            else:
                break

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
            file_type = raw_input("\nWould you like standard file names? \nThe standard file names will be: \n'3s_slater_det.sd', '3s.sp' and 'pairing_g1.int' for g=1 \n y/n: ")

            if file_type not in ['y', 'n']:
                raise FileNameError

            if file_type == 'y':
                sp_basis_filename, SD_filename, tbme_filename = give_file_names(g)

            if file_type == 'n':
                extension = raw_input("Provide your extension to the file names: ")
                
                if not extension.isalpha():
                    raise ExtensionError
                
                sp_basis_filename, SD_filename, tbme_filename =  give_file_names(g, extension+'_')
            #print sp_basis_filename, SD_filename, tbme_filename

        except FileNameError:
            print("\nERROR: Please write either 'y' or 'n'.\n")
        except ExtensionError:
            print("\nERROR: Please provide the extension for the file name as a string without special characters (only letters).\n")

        else:
            break


           
    return nmin, nmax, lmin, lmax, jmin, jmax, isos, g, N_particles, sp_basis_filename, SD_filename, tbme_filename
'''


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
            yn = raw_input("Whould you like standard input? \ny/n: ")

            if yn not in ['y', 'n']:
                    raise FileNameError

            if yn == 'y':
                break

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
                g = float(raw_input("Write: g "))
            except ValueError:
                print("\nERROR: Please provide g as a float / real number (without whitespace behind the last number).\n")

            else:
                break

        while True:
            try:
                case = raw_input("Write: model space ('pairing' or 'sd' without whitespace behind) ")
                if isos not in ['n', 'np']:
                    raise CeseError

            except CaseError:
                print("\nERROR: Please write either 'pairing' or 'sd'.\n")
            else:
                break

           
    return N_particles, g, case




