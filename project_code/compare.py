def beta_alpha_compare(beta_list, alpha_list):
	
	diff_list = []
	beta_list_red = list(beta_list)
	alpha_list_red = list(alpha_list)
	#if len(beta_list) == len(alpha_list):
	for i in range(0, len(beta_list)):
		j=0
		j_found = False
		while j < len(alpha_list) and j_found == False:
			print beta_list[i],i, alpha_list[j],j, diff_list
			if beta_list[i] == alpha_list[j]:
				j_found = True
				alpha_list_red.remove(alpha_list[j])
				beta_list_red.remove(beta_list[i])
			else:
				j = j+1
	diff_list.extend(beta_list_red)
	diff_list.extend(alpha_list_red)
	print diff_list

	#phase

	#(list(alpha_list).index(alpha_beta_compare[1]))
	return diff_list




beta_list = [1,2,3,5,4]
alpha_list = [1,3,4,5,7]

beta_alpha_compare(beta_list, alpha_list)
