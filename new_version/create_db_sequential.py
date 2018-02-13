import sqlite3
from add_update_sql import add_columns
from datetime import date

db_name = "BreastCancerDB_" + str(date.today()) + '.db'
conn = sqlite3.connect(db_name)
cursor = conn.cursor()
table_name1 = "Patient_Information_History"
columns1 = "File_number, MR_number, Name, FirstVisit_Date, Permanent_Address, Current_Address, Phone, Email_ID, " \
		   "Gender, Age_yrs, Date_of_Birth, Height_cm, Weight_kg, BMI, Diet"
cursor.execute('CREATE TABLE {tn} ({nf})'\
				.format( tn = table_name1, nf = columns1))
habits = "Alcohol_y_n", "Alcohol_Consumption_age_yrs", "Quantity_alcohol_per_week", "Duration_alcohol", \
		 "Comments_alcohol", "Tobacco_y_n", "Type_tobacco", "Tobacco_consumption_age_yrs", "Quantity_tobacco_per_week", "Duration_tobacco", "Comments_tobacco", "Other_Deleterious_Habits"
add_columns (cursor, table_name1, habits)
other_tables_y_n = "Nutritional_supplements_y_n", "Physical_Activity_y_n", "Medical_History_y_n", \
				   "Previous_Cancer_History_y_n", "FamilyCancer_history_y_n",
add_columns(cursor, table_name1, other_tables_y_n)

family_details = "Marital_Status", "Siblings", "Sisters", "Brothers", "Children", "Daughters", "Sons"
add_columns(cursor, table_name1, family_details)
repro_details = "Menarche_yrs", "Menopause_Status", "Age_at_Menopause_yrs", "Date_last_menstrual_period", \
			  "Number_pregnancies", "Pregnancy_to_term", "Number_abortions", "Age_first_child", "Age_first_pregnancy", \
			  "Age_last_child", "Age_last_pregnancy", "Two_births_in_year", "Breast_feeding_y_n", "Breast_usage_feeding",\
			  "Type_birth_control_used", "Details_birth_control", "Duration_birth_control"
add_columns(cursor, table_name1, repro_details)
symptoms = "RB_symptoms", "RB_symptoms_duration", "LB_symptoms", "LB_symptoms_duration", "RB_Other_Symptoms",\
		   "RB_Other_Symptoms_duration", "LB_Other_Symptoms","LB_Other_Symptoms_duration", "Detected_by", "Metatasis_Symptoms"
add_columns(cursor, table_name1, symptoms)

block_report_info = "Block_SR_Number", "Biopsy_Block_ID", "No_of_blocks", "Date_of_Biopsy", "Lab_ID", "Biopsy_Type"
add_columns(cursor, table_name1, block_report_info)

tumour_biopsy = "Tumour_biopsy_diagnosis", "Tumour_biopsy_diagnosis_grade", "Tumour_biopsy_ER", \
				"Tumour_biopsy_ER_Percent", "Tumour_biopsy_PR", "Tumour_biopsy_PR_Percent", "Tumour_biopsy_HER2", \
				"Tumour_biopsy_HER2_Grade", "Tumour_biopsy_FISH", "Tumour_biopsy_Ki67_Percent"
add_columns(cursor, table_name1, tumour_biopsy)

lymphnode_biopsy = "Lymph_Node_biopsy_FNAC", "Lymph_Node_biopsy_location", "Lymph_Node_biopsy_diagnosis"
add_columns(cursor, table_name1, lymphnode_biopsy)

surgery_info = "Surgical_Block_ID", "Surgery_No_of_blocks", "Block_Source", "Tumor_block_ref", "Nodes_block_ref",\
			   "Ad_Normal_block_ref", "Reduction_tissue_block_ref", "Date_of_Surgery", "Name_Surgeon", "Hospital_ID",\
			   "Lesion_Side", "Type_surgery", "Response_surgery"
add_columns(cursor, table_name1, surgery_info)
surgery_block = "Tumour_size_Surgery_Block_Report", "Grade_Surgery_Block_Report", "Diagnosis_Surgery_Block_Report", "DCIS_Percent_Surgery_Block_Report", "DCIS_Invasion_Surgery_Block_Report", "Perineural_Invasion_Surgery_Block_Report", "Necrosis_Surgery_Block_Report","Lymphovascular_Invasion_Surgery_Block_Report", "Margins_Surgery_Block_Report", "Surgery_Block_Report"
add_columns(cursor, table_name1, surgery_block)
node_block = "Sentinel_Node_Block_Report", "Sentinel_Node_Block_Report_Number", "Axillary_Node_Block_Report", "Axillary_Node_Block_Report_Number", "Apical_Node_Block_Report", "Apical_Node_Block_Report_Number","Perinodal_Spread_Node_Block_Report", "Supraclavicular_Involved_Node_Block_Report"
add_columns(cursor, table_name1, node_block)
staging = "Pathological_Staging_pT", "Pathological_Staging_pN", "Pathological_Staging_M", "Pathological_Staging_P_Stage", "Clinical_Staging"
add_columns(cursor, table_name1, staging)
table_name2 = "General_Medical_History"
columns2 = "File_number, MR_number, Name, Condition, Diagnosis_date, Treatment"
cursor.execute('CREATE TABLE {tn} ({nf})'\
				.format(tn=table_name2, nf=columns2))
table_name3 = "Family_Cancer_History"
columns3 = "File_number, MR_number, Name, Type_Cancer, Relation_to_patient, Age_at_detection_yrs"
cursor.execute('CREATE TABLE {tn} ({nf})'\
				.format(tn=table_name3, nf=columns3))
table_name4 = "Previous_Cancer_History"
columns4 = "File_number, MR_number, Name, Type_Cancer, Year_diagnosis, Surgery, Type_Surgery, " \
		   "Radiation, Type_Radiation, Duration_Radiation, Chemotherapy, Type_Chemotherapy, " \
		   "Duration_Chemotherapy, Hormone, Type_Hormone, Duration_Hormone, Alternative_Treatment, " \
		   "Type_Alternative_Treatment, Duration_Alternative_Treatment, Home_Remedy, Type_Home_Remedy, Duration_Home_Remedy"
cursor.execute('CREATE TABLE {tn} ({nf})'\
				.format(tn = table_name4, nf = columns4))
table_name5 = "Nutritional_Supplements"
columns5 = "File_number, MR_number,  Name, Type_nutritional_supplements, Quantity_nutritional_supplements_per_day, " \
		   "Duration_nutritional_supplements"
cursor.execute('CREATE TABLE {tn} ({nf})'\
				.format(tn = table_name5, nf = columns5))
table_name7 = "Physical_Activity"
columns7 = "File_number, MR_number,  Name, Type_activity, Frequency_activity"
cursor.execute('CREATE TABLE {tn} ({nf})'\
				.format(tn = table_name7, nf = columns7))
conn.commit()
conn.close()
