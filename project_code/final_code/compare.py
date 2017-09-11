def beta_alpha_compare(beta_list, alpha_list):
    """
    This function compare <beta_SD| with |alpha_SD>

    To call it
    beta_alpha_compare(beta_list, alpha_list)

    Input

    beta_list:      list,
                    occupied states in the beta Slater determinant
    alpha_list:     list,
                    occupied states in the alpha Slater determinant

    Output

    diff_list:      list,
                    different states between beta and alpha Slater determinants

    phase:          float,
                    phase due to the anticommutation of the creation and annihilation operators
    """
  
    phase = 0
    diff_list = []
    beta_list_red = list(beta_list)
    alpha_list_red = list(alpha_list)
    #if len(beta_list) == len(alpha_list):
    for i in range(0, len(beta_list)):
        j=0
        j_found = False
        while j < len(alpha_list) and j_found == False:
            #print beta_list[i],i, alpha_list[j],j, diff_list
            if beta_list[i] == alpha_list[j]:
                j_found = True
                alpha_list_red.remove(alpha_list[j])
                beta_list_red.remove(beta_list[i])
                #phase = phase+j+len(beta_list)-i-1
            else:
                j = j+1
    diff_list.extend(beta_list_red)
    diff_list.extend(alpha_list_red)


    for i in range(0,len(diff_list)/2):
    	phase = phase + (list(beta_list).index(diff_list[i]))
        #phase = phase + len(beta_list)-(list(beta_list).index(diff_list[i]))-1
    for i in range(len(diff_list)/2,len(diff_list)):
        phase = phase + (list(alpha_list).index(diff_list[i]))
    
    phase = (-1)**phase

    #print diff_list, phase
    
    return diff_list, phase
