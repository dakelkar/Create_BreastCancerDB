def nut_supplements(conn, cursor, file_number, table):
	from add_update_sql import update_single
	from breast_cancer_tables import nut_supp_table
	from ask_y_n_statement import  ask_y_n
	nut_supplements = ask_y_n("Nutritional supplements taken")
	if nut_supplements:
		nut_supp_table(conn, cursor, file_number)
		nut_supplements = "Nutritional supplements taken"
	else:
		nut_supplements = "No nutritional supplements taken"
	update_single(conn, cursor, table, "Nutritional_supplements_y_n", file_number, nut_supplements)

def phys_act (conn, cursor, file_number, table):
	from breast_cancer_tables import physical_activity_table
	from add_update_sql import update_single
	from ask_y_n_statement import ask_y_n
	phys_act = ask_y_n("Any Physical Activities ?")
	if phys_act:
		physical_activity_table(conn, cursor, file_number)
		phys_act = "Physical Activities Performed"
	else:
		phys_act = "No Physical Activities"
	update_single(conn, cursor, table, "Physical_Activity_y_n", file_number, phys_act)

def med_history (conn, cursor, file_number, table):
	from breast_cancer_tables import med_history_table
	from ask_y_n_statement import ask_y_n
	from add_update_sql import update_single
	medical_history_y_n = ask_y_n("Other Medical History ?")
	if medical_history_y_n:
		med_history_table(conn, cursor, file_number)
		medical_history_y_n = "Previous medical history present"
	else:
		medical_history_y_n = "No previous medical history present"
	update_single(conn, cursor, table, "Any_Other_Medical_History_y_n", file_number, medical_history_y_n)

def  cancer_history (conn, cursor, file_number, table):
	from breast_cancer_tables import cancer_table
	from add_update_sql import update_single
	from ask_y_n_statement import ask_y_n
	previous_cancer_history_y_n = ask_y_n("Previous history of cancer ?")
	if previous_cancer_history_y_n:
		cancer_table(conn, cursor, file_number)
		previous_cancer_history_y_n = "Previous history of cancer"
	else:
		previous_cancer_history_y_n = "No previous history of cancer"
	update_single(conn, cursor, table, "Previous_Cancer_History_y_n", file_number, previous_cancer_history_y_n)

def family_details (conn, cursor, file_number, table):
	from add_update_sql import update_multiple
	from ask_y_n_statement import ask_y_n
	marital_status = input ('Marital_Status :')
	siblings = ask_y_n ('Siblings')
	if siblings:
		siblings_number = input ("Number of siblings: ")
		sisters = input ('Sisters :')
		brothers = input ('Brothers :')
	else:
		siblings_number, sisters, brothers = "No Siblings", "0", "0"
	children_y_n = ask_y_n('Children')
	if children_y_n:
		children_number = input("Number of children: ")
		daughters = input ('Daughters :')
		sons = input ('Sons :')
	else:
		children_number, daughters, sons = "No Children", "0", "0"
	columns = "Marital_Status", "Siblings", "Sisters", "Brothers", "Children", "Daughters", "Sons"
	new_data = marital_status, siblings_number, sisters, brothers, children_number, daughters, sons
	update_multiple (conn, cursor, table, columns, file_number, new_data)

def repro_details (conn, cursor, file_number, table):
	from add_update_sql import update_multiple
	from breast_cancer_tables import feed_duration
	from ask_y_n_statement import ask_option, ask_y_n
	menarche = input('Age at menarche (yrs): ')
	category= "Menopausal Status"
	options = ["Pre-menopausal", "Peri-menopausal", "Post-Menopausal", "Other"]
	menopause = ask_option(category, options)
	menopause_age = menopause
	if menopause == "Post-Menopausal":
		menopause_age = input('Age at menopause (yrs): ')
		lmp = "Last menstrual period "+ menopause_age +" yrs"
		period_type = "NA"
	else:
		lmp = input("Date of last menstrual period: ")
		category = "Period"
		options = ["Regular", "Irregular", "Other"]
		period_type = ask_option (category, options)
	number_pregnancy = input("Number of pregnancies: ")
	number_term = input("Pregnancy carried to term (include abortion after 6 months): )")
	number_abortion = input("Number of abortions: ")
	sql = ('SELECT Children FROM Patient_Information_History WHERE File_number = \'' + file_number + "'")
	cursor.execute(sql)
	kids = cursor.fetchall()
	children_number = kids[0][0]
	sql = ('SELECT Age_yrs FROM Patient_Information_History WHERE File_number = \'' + file_number + "'")
	cursor.execute(sql)
	age = cursor.fetchall()
	age_mother = age[0][0]
	if children_number == 'No Children':
		age_first = 'NA'
		age_last = 'NA'
	else:
		age_first = input ("Age of first child: ")
		if int(children_number)>1:
			age_last = input ("Age of last child: ")
		else:
			age_last = age_first
	age_first_preg = input ("Age at first pregnancy: ")
	if str.lower(age_first_preg) == "na":
		age_first_preg = str(int(age_mother) - int(age_first))
	age_last_preg = input ("Age at last pregnancy: ")
	if str.lower(age_first_preg) == "na":
		age_last_preg = str(int(age_mother) - int(age_last))
	twice_birth = ask_y_n("Two births in a year (not twins) y/n: ", "Two births in a year", "No two births in a year")
	breast_feeding = ask_y_n ("Breast feeding?")
	if breast_feeding:
		breast_feeding = "Breast feeding"
		feed_duration (conn, cursor, file_number, children_number)
	else:
		breast_feeding = "No Breast feeding"
	type_birth_control = input("Type of birth control used: ")
	if str.lower(type_birth_control) == "na":
		detail_birth_control = "NA"
		duration_birth_control = "NA"
	else:
		detail_birth_control = input ("Details of birth control used: ")
		duration_birth_control = input ("Duration of birth control use: ")
	new_data = menarche, menopause, menopause_age, lmp, period_type, number_pregnancy, number_term, number_abortion, \
			   age_first, age_first_preg, age_last,age_last_preg, twice_birth, breast_feeding, \
			   type_birth_control,detail_birth_control, duration_birth_control
	columns = "Menarche_yrs", "Menopause_Status", "Age_at_Menopause_yrs", "Date_last_menstrual_period", "Period_Type", \
			  "Number_pregnancies", "Pregnancy_to_term", "Number_abortions", "Age_first_child", "Age_first_pregnancy",\
			  "Age_last_child", "Age_last_pregnancy", "Two_births_in_year", "Breast_feeding", \
			  "Type_birth_control_used", "Details_birth_control", "Duration_birth_control"
	update_multiple (conn, cursor, table, columns, file_number, new_data)

def breast_symptoms (conn, cursor, file_number, table):
	from ask_y_n_statement import get_symptom, get_rb_lb, ask_y_n
	from add_update_sql import update_multiple
	from breast_cancer_tables import other_symp
	symp_state = "Pain or tenderness", "Lumps", "Nipple Discharge", "Nipple Retraction", "Dimpling", \
				 "Discolouration", "Ulceration", "Eczema"
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
	other_symptom = ask_y_n("Other Symptoms?", True, False)
	if other_symptom:
		other_symp(conn, cursor, file_number, table)
	else:
		other_symptom = "No other symptoms"
		other_symp_dur = "NA"
		data = (other_symptom, other_symp_dur, other_symptom, other_symp_dur)
		columns = "RB_Other_Symptoms", "RB_Other_Symptoms_duration", "LB_Other_Symptoms", "RB_Other_Symptoms_duration"
		update_multiple(conn, cursor, table, columns, file_number, data)

def habits (conn, cursor, file_number, table):
	from add_update_sql import update_multiple, update_single
	from ask_y_n_statement import  ask_option, ask_y_n
	category = "Diet"
	options = ["Vegetarian", "Non-Vegetarian", "Ovo-Vegetarian", "Other"]
	diet = ask_option(category, options)
	alcohol = ask_y_n ("Alcohol consumption")
	if alcohol:
		alcohol_consump = "Alcohol Consumption"
		alcohol_age= input ("Consumption of alcohol from which age (yrs): ")
		alcohol_quant = input ("Quantity of alcohol consumed per week: ")
		alcohol_duration = input ("Duration of alcohol consumption: ")
		alcohol_comments = input ("Additional comments for alcohol consumption: ")
	else:
		alcohol_consump = "No Alcohol Consumption"
		alcohol_age = "NA"
		alcohol_quant = "NA"
		alcohol_duration = "NA"
		alcohol_comments = "NA"
	columns = "Diet","Alcohol_y_n", "Alcohol_Consumption_age_yrs", "Quantity_alcohol_per_week", "Duration_alcohol", "Comments_alcohol"
	new_data = diet, alcohol_consump, alcohol_age, alcohol_quant, alcohol_duration, alcohol_comments
	update_multiple (conn, cursor, table, columns, file_number, new_data)
	tobacco = ask_y_n("Tobacco consumption")
	if tobacco:
		tobacco = "Tobacco consumption"
		tobacco_type = input ("Type of tobacco consumption: ")
		tobacco_age= input ("Consumption of tobacco from which age (yrs): ")
		tobacco_quant = input ("Quantity of tobacco consumed per week: ")
		tobacco_duration = input ("Duration of tobacco consumption: ")
		tobacco_comments = input ("Additional comments for tobacco consumption: ")
	else:
		tobacco = "No Tobacco Consumption"
		tobacco_type = "NA"
		tobacco_age = "NA"
		tobacco_quant = "NA"
		tobacco_duration = "NA"
		tobacco_comments = "NA"
	columns = "Tobacco_y_n", "Type_tobacco", "Tobacco_consumption_age_yrs", "Quantity_tobacco_per_week", "Duration_tobacco", "Comments_tobacco"
	new_data = tobacco, tobacco_type, tobacco_age, tobacco_quant, tobacco_duration, tobacco_comments
	update_multiple (conn, cursor, table, columns, file_number, new_data)
	other_del_habits = input ("Other Deleterious Habits (if present give details): ")
	update_single (conn, cursor, table, "Other_Deleterious_Habits", file_number, other_del_habits)

def metastasis_symp (conn, cursor, file_number, table):
	from add_update_sql import update_single
	from ask_y_n_statement import ask_y_n
	met_none = ask_y_n ("Metastatis Symptoms Present?")
	met = []
	if not met_none:
		met = [["No Metastatis Symptoms"]]
	else:
		met_bone = ask_y_n ("Bone Pain")
		if met_bone:
			met.append(["Bone Pain"])
		met_cough = ask_y_n ("Cough")
		if met_cough:
			met.append(["Cough"]) 
		met_jaundice = ask_y_n("Jaundice")
		if met_jaundice:
			met.append(["Jaundice"])
		met_headache = ask_y_n ("Headache")
		if met_headache:
			met.append(["Headache"])
		met_weight = ask_y_n("Weight loss")
		if met_weight:
			met.append(["WeightLoss"])
	met_flat = [item for sublist in met for item in sublist]
	data_met = "; ".join(met_flat)
	update_single (conn, cursor, table, "Metatasis_Symptoms", file_number, data_met)

def det_by (conn, cursor, table, file_number):
	from add_update_sql import update_multiple
	from ask_y_n_statement import ask_option
	category = "Current Breast Cancer"
	options = ["Self", "Physician", "Screening Camp", "Other"]
	determined_by = ask_option (category, options)
	if determined_by == "Screening Camp":
		sc_id = input ("Screening Camp ID: ")
		determined_by = "Screening Camp ID " + sc_id
	det_date = input ("Date of current breast cancer detection: ")
	columns = "Current_Breast_Cancer_Detected_By", "Current_Breast_Cancer_Detected_Date"
	data = determined_by, det_date
	update_multiple (conn, cursor, table, columns, file_number, data)

def family_cancer (conn, cursor, file_number, table):
	from add_update_sql import update_single
	from breast_cancer_tables import family_cancer_table
	from ask_y_n_statement import ask_y_n
	family_cancer_history_y_n = ask_y_n('Cancer history in Family')
	if family_cancer_history_y_n:
		family_cancer_table(conn, cursor, file_number)
		family_cancer_history_y_n = "Family History of Cancer"
	else:
		family_cancer_history_y_n = "No Family History of Cancer"
	update_single(conn, cursor, table, "FamilyCancer_history_y_n", file_number, family_cancer_history_y_n)

def bio_info(conn, cursor, file_number, table):
	import add_update_sql
	import ask_y_n_statement
	check = False
	while not check:
		mr_number = input('MR_number :')
		name = input('Name :')
		consent = ask_y_n_statement.ask_y_n("Is consent form with signature present in file", "Consent Taken","Consent form not present")
		aadhaar_card = input ("Aadhaar card number (if available): ")
		date_first = input("Date of first visit: ")
		permanent_address = input('Permanent_Address :')
		current_address = input('Current_Address :')
		phone = input('Phone :')
		email_id = input('Email_ID :')
		gender = input('Gender :')
		age_yrs = input('Age (yrs) :')
		date_of_birth = input('Date of Birth :')
		place_birth = input('Place of Birth :')
		height_cm = input('Height (cm) :')
		weight_kg = input('Weight (kg) :')
		height = float(height_cm) / 100
		weight = float(weight_kg)
		BMI = str(round(weight / (height * height)))
		columns_list = ["MR_number", "Name", "Consent", "Aadhaar_Card", "FirstVisit_Date", "Permanent_Address",
						"Current_Address", "Phone", "Email_ID","Gender", "Age_yrs", "Date_of_Birth", "Place_Birth",
						"Height_cm", "Weight_kg", "BMI"]
		new_data = [mr_number, name, consent, aadhaar_card, date_first, permanent_address, current_address, phone,
                        email_id, gender, age_yrs, date_of_birth, place_birth, height_cm, weight_kg, BMI]
		check = add_update_sql.review_input(file_number, columns_list, new_data)
	columns = "MR_number", "Name", "Consent", "Aadhaar_Card", "FirstVisit_Date", "Permanent_Address", "Current_Address",\
			  "Phone", "Email_ID", "Gender", "Age_yrs", "Date_of_Birth", "Place_Birth", "Height_cm", "Weight_kg", "BMI"
	data = mr_number, name, consent, aadhaar_card, date_first, permanent_address, current_address, phone, email_id, \
              gender, age_yrs, date_of_birth, place_birth, height_cm, weight_kg, BMI
	add_update_sql.update_multiple(conn, cursor, table, columns, file_number, data)