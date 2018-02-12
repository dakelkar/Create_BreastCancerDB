def ask_symptom (symp_state):
	symp_y_n = input ("Symptom of "+ symp_state+"? (y/n) ")
	if str.lower(symp_y_n) == "y":
		symp_breast_right = input ("Right Breast y/n: ")
		if str.lower(symp_breast_right) == "y":
			symp_breast_right = symp_state
			symp_duration_right = input ("Duration of symptoms in right breast: ")
		else:
			symp_breast_right = None
			symp_duration_right	= None
		symp_breast_left = input ("Left Breast y/n: ")
		if str.lower(symp_breast_left) == "y":
			symp_breast_left = symp_state
			symp_duration_left = input ("Duration of symptoms in left breast: ")
		else:
			symp_breast_left = None
			symp_duration_left = None
	else:
		symp_breast_right = None
		symp_duration_right	= None
		symp_breast_left = None
		symp_duration_left = None
	RB = [symp_breast_right, symp_duration_right]
	LB = [symp_breast_left, symp_duration_left]
	data = [RB, LB]
	return data

def get_symptom (symp_state):
	#from ask_y_n_statement import ask_symptom
	all_data = []
	for index in range (0, len(symp_state)):
		var = ask_symptom (symp_state[index])
		all_data.append(var)
	return all_data

def get_rb_lb (all_data, pos):
	data_list = []
	data_index = len(all_data) 
	for index in range(0,data_index):
		var= all_data[index][pos]
		data_list.append(var)
	return (data_list)
