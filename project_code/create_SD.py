# OLD FILE - NOT IN USE - why is it in this folder?


import numpy as np
############################
dim_basis = 8
# read the number of particles in the system
N_part = 4
#
def create_SD(N_part, dim_basis):
  index = 0
  SD_list = []
  '''
# initialize the first Slater Det : {1,2,3,4}
  #SD_first = []
  for i in range (1, N_part+1,1):
    SD_first.append(i)
  #if condition of good Slated determinant are fulfilled
     index += 1
     SD_list.append(index)
     SD_list.extend(SD_first)
  #end if
  '''
  for a in range (1, dim_basis-2,1):
    for b in range (a+1, dim_basis-1, 1):
      for c in range (b+1, dim_basis, 1):
        for d in range (c+1, dim_basis+1, 1):
#      SD_add = SD_first
#      SD_add.pop(j) # remove the last element
#      SD_add.append(i) # add the next new element
      #if condition of same state and M=0  
          index += 1
          SD_list.append(index)
          SD_list.extend([a,b,c,d])
      #end if
  dim_SD = index
  print ' tot Slater Determinants = %d ' % (dim_SD)
  SD_array = np.array(SD_list)
  SD_states = SD_array.reshape(dim_SD,5)
#
  for i in range(0,dim_SD,1):
    print '%2d %2d %2d %2d %2d' % (SD_states[i,0],SD_states[i,1],SD_states[i,2],SD_states[i,3],SD_states[i,4])
#
#test this N_part=4 fixed routine create_SD
create_SD(N_part, dim_basis)
#
