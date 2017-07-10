from basis import *


# Input parameters:
##############################################################
nmax = 3
nmin = 0
lmax = 0
lmin = 0
jmin = 1
jmax = 1
isos = 1
# test of the fuction sp_pairing
#sp_pairing(nmin, nmax, lmin, lmax, jmin, jmax, isos)
#
#
nmax = 2
lmax = 2
jmax = 5
# test of the function sp_harmoscill
#sp_harmoscill(0,nmax,0, lmax,1, jmax, 2)
#

# filename for the basis:
sp_basis_filename = '3s.sp'

##############################################################





matrix = np.genfromtxt(sp_basis_filename,skip_header=5, usecols=(0,1,2,3,4,5))

particle = np.genfromtxt(sp_basis_filename,skip_header=1, usecols=(0), max_rows=1, dtype='string')



print matrix
print particle
