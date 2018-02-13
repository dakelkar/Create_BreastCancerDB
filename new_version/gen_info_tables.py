def nut_supplements(conn, cursor, file_number, mr_number, name, table):
	from add_update_sql import update_single
	from breast_cancer_tables import nut_supp_table
	nut_supplements = input("Nutritional supplements taken (y/n): ")
	if str.lower(nut_supplements) == "y":
		nut_supp_table(conn, cursor, file_number, mr_number, name)
		nut_supplements = "Nutritional supplements taken"
	else:
		nut_supplements = "No nutritional supplements taken"
	update_single(conn, cursor, table, "Nutritional_supplements_y_n", file_number, nut_supplements)

def phys_act (conn, cursor, file_number, mr_number, name, table):
	from breast_cancer_tables import physical_activity_table
	from add_update_sql import update_single
	phys_act = input("Physical Activities (y/n): ")
	if str.lower(phys_act) == "y":
		physical_activity_table(conn, cursor, file_number, mr_number, name)
		phys_act = "Physical Activities Performed"
	else:
		phys_act = "No Physical Activities"
	update_single(conn, cursor, table, "Physical_Activity_y_n", file_number, phys_act)

def med_history (conn, cursor, file_number, mr_number, name, table):
	from breast_cancer_tables import med_history_table
	from add_update_sql import update_single
	medical_history_y_n = input('Medical_History_y_n :')
	if (str.lower(medical_history_y_n) == 'y'):
		med_history_table(conn, cursor, file_number, mr_number, name)
		medical_history_y_n = "Previous medical history present"
	else:
		medical_history_y_n = "No previous medical history present"
	update_single(conn, cursor, table, "Medical_History_y_n", file_number, medical_history_y_n)

def  cancer_history (conn, cursor, file_number, mr_number, name, table):
	from breast_cancer_tables import cancer_table
	from add_update_sql import update_single
	previous_cancer_history_y_n = input('Previous history of cancer (y/n): ')
	if str.lower(previous_cancer_history_y_n) == 'y':
		cancer_table(conn, cursor, file_number, mr_number, name)
		previous_cancer_history_y_n = "Previous history of cancer"
	else:
		previous_cancer_history_y_n = "No previous history of cancer"
	update_single(conn, cursor, table, "Previous_Cancer_History_y_n", file_number, previous_cancer_history_y_n)

def family_details (conn, cursor, file_number, table):
	from add_update_sql import update_multiple
	marital_status = input ('Marital_Status :')
	siblings = input ('Siblings y/n:')
	siblings_number, sisters, brothers = "No Siblings", "0", "0"
	if (str.lower(siblings) == "y"):
		siblings_number = input ("Number of siblings: ")
		sisters = input ('Sisters :')
		brothers = input ('Brothers :')
	children_y_n = input ('Children_y_n :')
	children_number, daughters, sons = "No Children", "0", "0"
	if str.lower(children_y_n) == "y":
		children_number = input("Number of children: ")
		daughters = input ('Daughters :')
		sons = input ('Sons :')
	columns = "Marital_Status", "Siblings", "Sisters", "Brothers", "Children", "Daughters", "Sons"
	new_data = marital_status, siblings_number, sisters, brothers, children_number, daughters, sons
	update_multiple (conn, cursor, table, columns, file_number, new_data)

def repro_details (conn, cursor, file_number, table):
	from add_update_sql import update_multiple
	menarche = input('Age at menarche (yrs): ')
	menopause = input('Menopausal status (pre/peri/post): ')
	menopause_age = menopause +" menopausal"
	if str.lower(menopause) == "post":
		menopause_age = input('Age at menopause (yrs): ')
		lmp = "Last menstrual period "+ menopause_age +" yrs"
		menopause = menopause + " menopausal"
	else:
		menopause = menopause + " menopausal"
		lmp = input("Date of last menstrual period: ")
	number_pregnancy = input("Number of pregnancies: ")
	number_term = input("Pregnancy carried to term (include abortion after 6 months): )")
	number_abortion = input("Number of abortions: ")
	sql = ('SELECT Children FROM Patient_Information_History WHERE File_number = \'' + file_number + "'")
	cursor.execute(sql)
	kids = cursor.fetchall()
	children_number = kids[0][0]
	if children_number == 'No Children':
		age_first = 'No Children'
		age_last = 'No Children'
	else:
		age_first = input ("Age of first child: ")
		if int(children_number)>1:
			age_last = input ("Age of last child: ")
		else:
			age_last = age_first
	age_first_preg = input ("Age at first pregnancy: ")
	age_last_preg = input ("Age at last pregnancy: ")
	twice_birth = input ("Two births in a year (not twins) y/n: ")
	if str.lower(twice_birth) == "y":
		twice_birth = "Two births in a year"
	else:
		twice_birth = "No two births in a year"
	breast_feeding = input ("Breast feeding y/n: ")
	if str.lower (breast_feeding) == "y":
		breast_feeding = "Breast feeding"
		feeding_details = input ("Feeding from right, left or both breasts? ")
	else:
		breast_feeding = "No breast feeding"
		feeding_details = "NA"
	type_birth_control = input ("Type of birth control used: ")
	detail_birth_control = input ("Details of birth control used: ")
	duration_birth_control = input ("Duration of birth control use: ")
	new_data = menarche, menopause, menopause_age, lmp, number_pregnancy, number_term, number_abortion, \
			   age_first, age_first_preg, age_last,age_last_preg, twice_birth, breast_feeding, feeding_details, \
			   type_birth_control,detail_birth_control, duration_birth_control
	columns = "Menarche_yrs", "Menopause_Status", "Age_at_Menopause_yrs", "Date_last_menstrual_period", \
			  "Number_pregnancies", "Pregnancy_to_term", "Number_abortions", "Age_first_child", "Age_first_pregnancy", \
			  "Age_last_child", "Age_last_pregnancy", "Two_births_in_year", "Breast_feeding_y_n", "Breast_usage_feeding",\
			  "Type_birth_control_used", "Details_birth_control", "Duration_birth_control"
	update_multiple (conn, cursor, table, columns, file_number, new_data)

def breast_symptoms (conn, cursor, file_number, table, symp_state):
	from ask_y_n_statement import get_symptom, get_rb_lb
	from add_update_sql import update_multiple
	from breast_cancer_tables import other_symp
	symptoms = get_symptom (symp_state)
	rb = get_rb_lb(symptoms, 0)
	rb_symp = list(filter(None, get_rb_lb(rb, 0)))
	rb_dur = list(filter(None, get_rb_lb(rb, 1)))
	lb = get_rb_lb(symptoms, 1)
	lb_symp = list(filter(None, get_rb_lb(lb, 0)))
	lb_dur = list(filter(None, get_rb_lb(lb, 1)))
	data = [rb_symp, rb_dur, lb_symp, lb_dur]
	for index in range(0,len(data)):
		if not data[index]:
			data[index] = ["NA"]
		else:
			data[index] = ["; ".join(data[index])]
	data_flat = [item for sublist in data for item in sublist]
	new_data = tuple(data_flat)
	columns = "RB_symptoms", "RB_symptoms_duration", "LB_symptoms", "LB_symptoms_duration"
	update_multiple (conn, cursor, table, columns, file_number, new_data)
	other_symptom = input("Other Symptoms? (y/n) ")
	if str.lower(other_symptom) == "y":
		other_symp(conn, cursor, file_number, table)
	else:
		other_symptom = "No other symptoms"
		other_symp_dur = "NA"
		data = (other_symptom, other_symp_dur, other_symptom, other_symp_dur)
		columns = "RB_Other_Symptoms", "RB_Other_Symptoms_duration", "LB_Other_Symptoms", "RB_Other_Symptoms_duration"
		update_multiple(conn, cursor, table, columns, file_number, data)

def habits (conn, cursor, file_number, table):
	from add_update_sql import update_multiple, update_single
	alcohol = input ("Alcohol consumption (y/n): ")
	alcohol_consump = "No Alcohol Consumption"
	alcohol_age= "No Alcohol Consumption"
	alcohol_quant = "No Alcohol Consumption"
	alcohol_duration = "No Alcohol Consumption"
	alcohol_comments = "No Alcohol Consumption"
	if str.lower(alcohol) == "y":
		alcohol_consump = "Alcohol Consumption"
		alcohol_age= input ("Consumption of alcohol from which age (yrs): ")
		alcohol_quant = input ("Quantity of alcohol consumed per week: ")
		alcohol_duration = input ("Duration of alcohol consumption: ")
		alcohol_comments = input ("Additional comments for alcohol consumption: ")
	columns = "Alcohol_y_n", "Alcohol_Consumption_age_yrs", "Quantity_alcohol_per_week", "Duration_alcohol", "Comments_alcohol"
	new_data = alcohol_consump, alcohol_age, alcohol_quant, alcohol_duration, alcohol_comments
	update_multiple (conn, cursor, table, columns, file_number, new_data)
	tobacco = input ("Tobacco consumption (y/n)")
	tobacco_type = "No Tobacco Consumption"
	tobacco_age= "No Tobacco Consumption"
	tobacco_quant = "No Tobacco Consumption"
	tobacco_duration = "No Tobacco Consumption"
	tobacco_comments = "No Tobacco Consumption"
	if str.lower(tobacco) == "y":
		tobacco = ("Tobacco consumption")
		tobacco_type = input ("Type of tobacco consumption: ")
		tobacco_age= input ("Consumption of tobacco from which age (yrs): ")
		tobacco_quant = input ("Quantity of tobacco consumed per week: ")
		tobacco_duration = input ("Duration of tobacco consumption: ")
		tobacco_comments = input ("Additional comments for tobacco consumption: ")
	else:
		tobacco = "No Tobacco Consumption"
	columns = "Tobacco_y_n", "Type_tobacco", "Tobacco_consumption_age_yrs", "Quantity_tobacco_per_week", "Duration_tobacco", "Comments_tobacco"
	new_data = tobacco, tobacco_type, tobacco_age, tobacco_quant, tobacco_duration, tobacco_comments
	update_multiple (conn, cursor, table, columns, file_number, new_data)
	other_del_habits = input ("Other Deleterious Habits: ")
	update_single (conn, cursor, table, "Other_Deleterious_Habits", file_number, other_del_habits)

def metastasis_symp (conn, cursor, file_number, table):
	from add_update_sql import update_single
	print ("Metastatis Symptoms: ")
	met = []
	met_none = input ("(y/n): ")
	if str.lower(met_none) == "n":
		met = [["No Metastatis Symptoms"]]
	else:
		met_bone = input ("Bone Pain (y/n): ")
		if str.lower(met_bone) == "y":
			met = ["Bone Pain"]
		met_cough = input ("Cough (y/n): ")
		if str.lower(met_cough) == "y":
			met.append(["Cough"]) 
		met_jaundice = input ("Jaundice (y/n): ")
		if str.lower(met_jaundice) == "y":
			met.append(["Jaundice"])
		met_headache = input ("Headache (y/n): ")
		if str.lower(met_headache) == "y":
			met.append(["Headache"])
		met_weight = input ("Weightloss (y/n): ")
		if str.lower(met_weight) == "y":
			met.append(["Weightloss"])
	met_flat = [item for sublist in met for item in sublist]
	data_met = "; ".join(met_flat)
	update_single (conn, cursor, table, "Metatasis_Symptoms", file_number, data_met)

def det_by (conn, cursor, table, file_number):
	from add_update_sql import update_single
	check = False
	while not check:
		print ("Detected by 1. Self, 2. Physician 3. Screening Camp")
		determined_by = input ("Please enter 1, 2, or 3: ")
		if determined_by== "1":
			determined_by= "Self"
			check = True
		elif determined_by == "2":
			determined_by = "Physician"
			check = True
		elif determined_by == "3":
			sc_id = input ("Screening Camp ID: ")
			determined_by = "Screening Camp ID " + sc_id
			check = True
	update_single(conn, cursor, table, "Detected_by", file_number,determined_by)
