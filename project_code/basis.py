import numpy as np
############################
'''
DEFINITIONS OF FUNCTION TO CALCULATE SINGLE PARTICLE STATES
the single-particle states are identified by the quantum numbers (n,l,2j,2m_j,2tz) 
starting with the smallest 2m_j value and 2tz [2tz=-1 for p, 2tz=+1 for n]
ATTENTION the variable j, m and tz are equal to 2 times the corresponding quantum number

nmin, nmax are the min and max principal quantum number  
lmin, lmax are the min and max of orbital angular moments
jmin and jmax are the min and max of total angular moments
isos is the number of different isospin species only n -> isos=1, np -> isos=2
'''
def sp_pairing(nmin, nmax, lmin, lmax, jmin, jmax, isos):
#
  if lmin == lmax: 
    l = lmax
  else:
    print 'ERROR: lmin != lmax not allowed in pairing sp-basis'
# CALCULATE THE DIMENSION OF THE SP-BASIS
  print 'MODEL SINGLE-PARTICLE STATES'
  print 'index n  l 2j 2m 2tz'
#
  sp = []
  index = 0
  if isos == 1:
    tz_min = 1
    tz_max = 1
  elif isos == 2:
    tz_min = -1
    tz_max = 1
  else:
    print 'ERROR: wrong number of isospin species' 
#
  for tz in range (tz_min, tz_max+2, 2):
    for n in range(0, nmax+1, 1):
      for j in range(1, jmax+2, 2):
        m = -j
        while m <= jmax:
          index = index+1
          sp.append(index)
          sp.append(n)
          sp.append(l)
          sp.append(j)
          sp.append(m)
          sp.append(tz)
          print ' %2d %3d %2d %2d %2d %2d' % (index, n, l, j, m, tz)
          m = m+2
        #end of while m
      #end of for j
    #end of for n
  #end of for tz
#
  dim_basis = index
  print ' tot s.p. states = %d ' % (dim_basis)
#
# transform sp list in matrix
  sp_array = np.array(sp)
  sp_matrix = sp_array.reshape(dim_basis,6)
#
# write an output in a NutshellX similar file .ps
  out_sp = open("3s.sp","w")
  out_sp.write("!4 level 2j=1 l=0 single-particle states\n")
  out_sp.write("!this describes a system with paired particles of the same isospin\n")
  out_sp.write("n \n")
  out_sp.write("0  0 \n")# assuming A=0 nad Z=0 for the core
  out_sp.write("%d \n" % dim_basis) # total number of sp states
  out_sp.write("1 %d \n" % dim_basis) # 1 group of sp states, number of sp states per group
  np.savetxt(out_sp, sp_matrix, fmt='%d %d %d %d %2d %d')
  out_sp.close()
  return sp_matrix
#
#######################################################
# HARMONIC OSCILLATOR SINGLE PARTICLE STATE
#
def sp_harmoscill(nmin,nmax,lmin, lmax,jmin, jmax, isos):
#
  print 'MODEL SINGLE-PARTICLE STATES'
  print 'index n  l 2j 2m 2tz'
#
  sp = []
  index = 0
  if isos == 1:
    tz_min = 1
    tz_max = 1
  elif isos == 2:
    tz_min = -1
    tz_max = 1
  else:
    print 'ERROR: wrong number of isospin species' 
#
  for tz in range (tz_min, tz_max+2, 2):
    for ntot in range(nmin, nmax+1, 1):
      l_start = max(lmin,ntot%2)
      for l in range(l_start, ntot+2, 2):
        n = (ntot-l)/2
        j_start = max(jmin,abs(2*l-1))
        for j in range(j_start, 2*l+1+2, 2):
          for m in range (-j, j+2, 2):
            index = index+1
            sp.append(index)
            sp.append(n)
            sp.append(l)
            sp.append(j)
            sp.append(m)
            sp.append(tz)
            print ' %2d %3d %2d %2d %2d %2d' % (index, n, l, j, m, tz)
          #end for m
        #end of for j
      #end for l
    #end of for n
  #end of for tz
#
  dim_basis = index
  print ' tot s.p. states = %d ' % (dim_basis)
#
# transform sp list in matrix
  sp_array = np.array(sp)
  sp_matrix = sp_array.reshape(dim_basis,6)
#
# write an output in a NutshellX similar file .ps
  out_sp = open("ho.sp","w")
  out_sp.write("!harmonic oscillator single-particle states\n")
  out_sp.write("np \n")
  out_sp.write("0  0 \n")# assuming A=0 nad Z=0 for the core
  out_sp.write("%d \n" % dim_basis) # total number of sp states
  out_sp.write("2 %d %d \n" % (dim_basis/2, dim_basis/2) ) # 1 group of sp states, number of sp states per group
  np.savetxt(out_sp, sp_matrix, fmt='%2d %d %d %d %2d %d')
  out_sp.close()
  return sp_matrix
##############################################################
#
nmax = 3
nmin = 0
lmax = 0
lmin = 0
jmin = 1
jmax = 1
isos = 1
# test of the fuction sp_pairing
sp_pairing(nmin, nmax, lmin, lmax, jmin, jmax, isos)
#
#
nmax = 2
lmax = 2
jmax = 5
# test of the function sp_harmoscill
sp_harmoscill(0,nmax,0, lmax,1, jmax, 2)
#
