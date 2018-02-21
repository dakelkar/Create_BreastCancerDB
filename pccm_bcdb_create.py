import sqlite3
from add_update_sql import add_columns
from datetime import date
import os.path

folder = "DB"
db_name = "PCCM_BreastCancerDB6_" + str(date.today()) + '.db'
path = os.path.join(folder, db_name)

if os.path.isfile(path):
    print (path + " file already exists")
else:
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    table_name1 = "Patient_Information_History"
    columns1 = "File_number, MR_number, Name, Consent, Aadhaar_Card, FirstVisit_Date, Permanent_Address, Current_Address, Phone, Email_ID, " \
           "Gender, Age_yrs, Date_of_Birth, Place_Birth, Height_cm, Weight_kg, BMI"
    cursor.execute(f'CREATE TABLE {table_name1} ({columns1})')
    habits = "Diet", "Alcohol_y_n", "Alcohol_Consumption_age_yrs", "Quantity_alcohol_per_week", "Duration_alcohol", \
             "Comments_alcohol", "Tobacco_y_n", "Type_tobacco", "Tobacco_consumption_age_yrs", \
             "Quantity_tobacco_per_week", "Duration_tobacco", "Comments_tobacco", "Other_Deleterious_Habits"
    add_columns(cursor, table_name1, habits)
    other_tables_y_n = "Nutritional_supplements_y_n", "Physical_Activity_y_n", "Any_Other_Medical_History_y_n", \
                       "Previous_Cancer_History_y_n", "FamilyCancer_history_y_n",
    add_columns(cursor, table_name1, other_tables_y_n)

    family_details = "Marital_Status", "Siblings", "Sisters", "Brothers", "Children", "Daughters", "Sons"
    add_columns(cursor, table_name1, family_details)
    repro_details = "Menarche_yrs", "Menopause_Status", "Age_at_Menopause_yrs", "Date_last_menstrual_period", \
                    "Period_Type", "Number_pregnancies", "Pregnancy_to_term", "Number_abortions", "Age_first_child", \
                    "Age_first_pregnancy", "Age_last_child", "Age_last_pregnancy", "Two_births_in_year", "Breast_feeding", \
                    "Type_birth_control_used", "Details_birth_control", "Duration_birth_control"
    add_columns(cursor, table_name1, repro_details)
    symptoms = "Current_Breast_Cancer_Detected_By", "Current_Breast_Cancer_Detected_Date", "RB_symptoms", "RB_symptoms_duration", "LB_symptoms", \
               "LB_symptoms_duration", "RB_Other_Symptoms", "RB_Other_Symptoms_duration", "LB_Other_Symptoms", \
               "LB_Other_Symptoms_duration", "Metatasis_Symptoms"
    add_columns(cursor, table_name1, symptoms)

    block_report_info = "Block_SR_Number", "Biopsy_Block_ID", "No_of_blocks", "Date_of_Biopsy", "Lab_ID", "Biopsy_Type"
    add_columns(cursor, table_name1, block_report_info)

    tumour_biopsy = "Tumour_biopsy_diagnosis", "Tumour_biopsy_diagnosis_grade", "Tumour_biopsy_ER", \
                    "Tumour_biopsy_ER_Percent", "Tumour_biopsy_PR", "Tumour_biopsy_PR_Percent", "Tumour_biopsy_HER2", \
                    "Tumour_biopsy_HER2_Grade", "Tumour_biopsy_FISH", "Tumour_biopsy_Ki67_Percent"
    add_columns(cursor, table_name1, tumour_biopsy)

    lymphnode_biopsy = "Lymph_Node_biopsy_FNAC", "Lymph_Node_biopsy_location", "Lymph_Node_biopsy_diagnosis"
    add_columns(cursor, table_name1, lymphnode_biopsy)
    surgery_info = "Surgical_Block_ID", "Surgery_No_of_blocks", "Block_Source", "Tumor_block_ref", "Nodes_block_ref", \
                  "Ad_Normal_block_ref", "Reduction_tissue_block_ref", "Date_of_Surgery", "Name_Surgeon", "Hospital_ID", \
                  "Lesion_Side", "Type_surgery", "Response_surgery"
    add_columns(cursor, table_name1, surgery_info)

    surgery_block = "Tumour_size_Surgery_Block_Report", "Grade_Surgery_Block_Report", "Diagnosis_Surgery_Block_Report", \
              "DCIS_Percent_Surgery_Block_Report", "DCIS_Invasion_Surgery_Block_Report", \
              "Perineural_Invasion_Surgery_Block_Report", "Necrosis_Surgery_Block_Report", \
              "Lymphovascular_Invasion_Surgery_Block_Report", "Margins_Surgery_Block_Report", "Surgery_Block_Report"
    add_columns(cursor, table_name1, surgery_block)

    node_block = "Sentinel_Node_Block_Report", "Sentinel_Node_Number_Removed", "Sentinel_Node_Number_Positive",\
                 "Sentinel_Node_Block_Report_Number", "Axillary_Node_Block_Report", "Axillary_Node_Number_Removed", \
                 "Axillary_Node_Number_Positive", "Axillary_Node_Block_Report_Number", "Apical_Node_Block_Report", \
                 "Apical_Node_Number_Removed", "Apical_Node_Number_Positive", "Apical_Node_Block_Report_Number", \
                 "Perinodal_Spread_Node_Block_Report", "Supraclavicular_Involved_Node_Block_Report"
    add_columns(cursor, table_name1, node_block)

    staging = "Pathological_Staging_pT", "Pathological_Staging_pN", "Pathological_Staging_M", \
              "Pathological_Staging_P_Stage", "Clinical_Staging"
    add_columns(cursor, table_name1, staging)
    table_name2 = "General_Medical_History"
    columns2 = "File_number, Condition, Diagnosis_date, Treatment"
    cursor.execute('CREATE TABLE {tn} ({nf})' \
                   .format(tn=table_name2, nf=columns2))
    table_name3 = "Family_Cancer_History"
    columns3 = 'File_number, Type_Cancer, Relation_to_Patient, Type_Relation, Age_at_detection_yrs'
    cursor.execute('CREATE TABLE {tn} ({nf})' \
                   .format(tn=table_name3, nf=columns3))
    table_name4 = "Previous_Cancer_History"
    columns4 = "File_number, Type_Cancer, Year_diagnosis, Type_Surgery," \
               "Type_Radiation,Duration_Radiation,Type_Chemotherapy,Duration_Chemotherapy," \
               "Type_Hormone, Duration_Hormone,Type_Alternative_Treatment, " \
               "Duration_Alternative_Treatment, Type_Home_Remedy, Duration_Home_Remedy"
    cursor.execute('CREATE TABLE {tn} ({nf})' \
                   .format(tn=table_name4, nf=columns4))
    table_name5 = "Nutritional_Supplements"
    columns5 = "File_number, Type_nutritional_supplements, Quantity_nutritional_supplements_per_day, " \
               "Duration_nutritional_supplements"
    cursor.execute('CREATE TABLE {tn} ({nf})' \
                   .format(tn=table_name5, nf=columns5))
    table_name7 = "Physical_Activity"
    columns7 = "File_number, Type_activity, Frequency_activity"
    cursor.execute('CREATE TABLE {tn} ({nf})' \
                   .format(tn=table_name7, nf=columns7))
    table_name8 = "Breast_Feeding"
    columns8 = "File_number, Child_number, Feeding_duration, Breast_usage_feeding"
    cursor.execute('CREATE TABLE {tn} ({nf})' \
                   .format(tn=table_name8, nf=columns8))

    clinical_exam = 'Provisional_Diagnosis_Clinical_Examination_CE', 'Lump_Palpable_CE', 'Lump_Location_CE', \
                    'Lump_Size_CE', 'Lump_Number_CE', 'Lump_Consistency_CE', 'Lump_Fixity_CE', 'Mastitis_CE', \
                    'Mastitis_type_CE', 'Tenderness_CE', 'Nipple_Retraction_CE', 'Nipple_Discharge_CE', \
                    'Nipple_Discharge_Type_CE', 'Skin_changes_CE', 'Skin_change_type_CE', \
                    'Palpable_axillary_nodes_CE', 'Palpable_axillary_nodes_number_CE', \
                    'Palpable_axillary_nodes_size_CE', 'Palpable_axillary_nodes_fixity_CE', \
                    'Palpable_supraclavicular_nodes_CE', 'Palpable_supraclavicular_nodes_number_CE', \
                    'Palpable_supraclavicular_nodes_size_CE', 'Palpable_supraclavicular_nodes_fixity_CE', \
                    'Contralateral_Breast_CE', 'Edema_arm_CE', 'RightArm_Circumference_cm_CE', \
                    'RightArm_UpperLimbVolume_cc_CE', 'RightArm_ElbowDistance_cm_CE', 'LeftArm_Circumference_cm_CE',\
                    'LeftArm_UpperLimbVolume_cc_CE', 'LeftArm_ElbowDistance_cm_CE'
    add_columns(cursor, table_name1, clinical_exam)

    nipple_cytology =  "Nipple_Cytology", "Date_Nipple_Cytology", "Number_Nipple_Cytology", "Report_Nipple_Cytology"
    add_columns(cursor, table_name1, nipple_cytology)

    mammography = 'DiagnosisLocation_Mammography', 'First_Mammography', 'LatestDate_Mammography', 'Number_Mammography', \
                  'PreviousDate_Mammography', 'Diagnosis_Mammography', 'Date_Mammography', 'AccessionNumber_Mammography',\
                  'Lesion_Mammography', 'LesionLocation_Mammography', 'Shape_Mammography', 'Size_Mammography', \
                  'Margin_Mammography', 'Density_Mammography', 'Calcification_Mammography', \
                  'Calcification_Implication_Mammography', 'Architecture_Mammography', 'Asymmetry_Mammography', \
                  'IntraMammaryLN_Mammography', 'SkinLesion_Mammography', 'DilatedDuct_Mammography', \
                  'Features_SkinRetraction_Mammography', 'Features_NippleRetraction_Mammography', \
                  'Features_SkinThickening_Mammography', 'Features_TrabecularThickening_Mammography', \
                  'Features_AxillaryLymphadenopathy_Mammography', 'SecondaryLesion_ContralateralBreast_Mammography', \
                  'DistancefromSkin_Mammography', 'DistanceFromPectMaj_Mammography', 'BIRADS_Mammography'
    add_columns(cursor, table_name1, mammography)

    conn.commit()
    print (path + (" file created"))
    conn.close()
