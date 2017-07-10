# OLD VERSION - NOT IN USE


############################
nmax = 3
lmax = 0
jmax = 1
# PAIRING SINGLE PARTICLE STATES
# function to enumerate the single-particle states with quantum numbers (n,l,2j,2m_j) starting with the smallest 2m_j value
# ATTENTION variable j = 2j quantum number as well as variable m = 2m_j quantum number
#
def sp_pairing(nmax, lmax, jmax):
  l = lmax
# CALCULATE THE DIMENSION OF THE SP-BASIS
  print 'PAIRING SINGLE PARTICLE STATES'
  print 'index n  l 2j 2m'
#
  sp = []
  index = 0
  for k in range(0, nmax+1, 1):
    n = k
    for i in range(1, jmax+2, 2):
      m = -i
      while m <= jmax:
        j = i
        index = index+1
        sp.append(index)
        sp.append(n)
        sp.append(l)
        sp.append(j)
        sp.append(m)
        print ' %2d %3d %2d %2d %2d ' % (index, n, l, j, m)
      # STORE IT
        m = m+2
      #end of while
    #end of for
  #end of for
#
  dim_basis = index
  print ' tot s.p. states = %d ' % (dim_basis)
#
  return sp
#
sp_pairing(nmax, lmax, jmax)
#######################################################
#
nmax = 2
lmax = 2
jmax = 5
#
# HARMONIC OSCILLATOR SINGLE PARTICLE STATE
#
def sp_harmoscill(nmax, lmax, jmax):
#
  print 'HARMONIC OSCILLATOR SINGLE PARTICLE STATE'
  print 'index n  l 2j 2m '
#
  sp = []
  index = 0
  for ntot in range(0, nmax+1, 1):
    for l in range(ntot%2, ntot+2, 2):
      n = (ntot-l)/2
      for j in range(abs(2*l-1), 2*l+1+2, 2):
        for m in range (-j, j+2, 2):
          index = index+1
          sp.append(index)
          sp.append(n)
          sp.append(l)
          sp.append(j)
          sp.append(m)
          print ' %2d %3d %2d %2d %2d ' % (index, n, l, j, m)
        #end m
      #end j
    #end l
   #end ntot
  dim_basis = index
  print ' tot s.p. states = %d ' % (dim_basis)
  return sp
#
#
sp_harmoscill(nmax, lmax, jmax)
