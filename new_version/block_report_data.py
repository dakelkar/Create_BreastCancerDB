def block_report_info (conn, cursor, file_number, table):
    from add_update_sql import update_multiple
    block_sr = input("Block Serial Number: ")
    block_id = input ("Biopsy Block ID: ")
    block_number = input("No of blocks: ")
    block_date = input("Date of Biopsy: ")
    lab_id = input("Lab ID: ")
    biopsy_type = input("Biopsy Type: ")
    columns = "Block_SR_Number", "Biopsy_Block_ID", "No_of_blocks", "Date_of_Biopsy", "Lab_ID", "Biopsy_Type"
    data = block_sr, block_id, block_number, block_date, lab_id,biopsy_type
    update_multiple(conn, cursor, table, columns, file_number, data)

def tumour_biopsy_data(conn, cursor, file_number, table):
    from ask_y_n_statement import ask_option
    from add_update_sql import update_multiple
    category = "Tumour biopsy diagnosis"
    options = ['Benign', "Ductal carcinoma in situ(DCIS) with microinvasion",
               "Ductal carcinoma in situ(DCIS) without microinvasion", "Lobular Carcinoma in Situ (LCS)",
               "Invasive Ductal Carcinoma (IDC)", "Invasive Lobular Carcinoma (ILC)", "Granulamatous Mastitis",
               "Papillary Carcinoma", "Phylloid Carcinoma", "Other"]
    tumour_diagnosis = ask_option(category, options)
    if tumour_diagnosis == 'Other':
        tumour_diagnosis = input ('Detail of other diagnosis: ')
    check = False
    while not check:
        tumour_grade = input("Tumour_biopsy_diagnosis_grade (1, 2 or 3): ")
        val = ["1", "2", "3"]
        check = tumour_grade in val
    category = "ER Status"
    options = ["Positive", "Negative"]
    tumour_er= ask_option(category, options)
    if (tumour_er == "Positive"):
        tumour_er_percent = input ("ER Percent: ")
    else:
        tumour_er_percent = "NA"
    category = "PR Status"
    options = ["Positive", "Negative"]
    tumour_pr = ask_option(category, options)
    if (tumour_pr == "Positive"):
        tumour_pr_percent = input ("PR Percent: ")
    else:
        tumour_pr_percent = "NA"
    category = "HER2 Status"
    options = ["Positive", "Negative"]
    tumour_her2 = ask_option(category, options)
    if (tumour_her2 == "Positive"):
        tumour_her2_percent = input ("HER2 Percent: ")
    else:
        tumour_her2_percent = "NA"
    category = "FISH"
    options = ["Positive", "Negative"]
    tumour_fish = ask_option(category, options)
    tumour_ki67 = input("Ki67 Percent")
    data = tumour_diagnosis,tumour_er ,tumour_er_percent ,tumour_pr, tumour_pr_percent, tumour_her2, tumour_her2_percent,\
           tumour_fish, tumour_ki67
    columns = "Tumour_biopsy_diagnosis", "Tumour_biopsy_diagnosis_grade", "Tumour_biopsy_ER", "Tumour_biopsy_ER_Percent", "Tumour_biopsy_PR", "Tumour_biopsy_PR_Percent", "Tumour_biopsy_HER2", "Tumour_biopsy_HER2_Grade", "Tumour_biopsy_FISH", "Tumour_biopsy_Ki67_Percent"
    update_multiple(conn, cursor, table, columns, file_number, data)

def lymphnode_biopsy(conn, cursor, file_number, table):
    from ask_y_n_statement import ask_option
    from add_update_sql import update_multiple
    category = "Lymph Node biopsy FNAC" 
    options = ["Done", "Not Done"]
    fnac = ask_option(category, options)
    if fnac == "Done":
        category = "Lymph Node biopsy location"
        options = ["Right", "Left", "Both"]
        fnac_location = ask_option(category, options)
        category = "Lymph Node biopsy diagnosis"
        options = ["Normal", "Benign", "Malignant"]
        fnac_diagnosis = ask_option(category, options)
    else:
        fnac_location = "NA"
        fnac_diagnosis = "NA" 
    data = fnac, fnac_location, fnac_diagnosis
    columns = "Lymph_Node_biopsy_FNAC", "Lymph_Node_biopsy_location", "Lymph_Node_biopsy_diagnosis"
    update_multiple(conn, cursor, table, columns, file_number, data)

def surgery_info (conn, cursor, file_number, table):
    from ask_y_n_statement import ask_option
    from add_update_sql import update_multiple
    surg_block_id = input("Surgical Block ID: ")
    surg_no_block = input("Number of Blocks: ")
    surg_block_source = input ("Surgery Block Source: ")
    surg_tumour_block = input ("Tumour Block Reference: ")
    surg_node_block = input ("Nodes Block Reference: ")
    surg_normal_block = input ("Adjacent Normal Block Reference: ")
    surg_red_block = input ("Reduction Tissue Block Reference: ")
    surg_date = input ("Date of Surgery: ")
    surg_name = input ("Name of surgeon: ")
    surg_hosp_id = input ("Hospital ID: ")
    category = "Lesion Side"
    options = ["RB-UOQ", "RB-UIQ", "RB-C", "RB-LOQ", "RB-LIQ", "LB-UOQ", "LB-UIQ", "LB-C", "LB-LOQ", "LB-LIQ"]
    lesion_side = ask_option(category, options)
    category = "Type Surgery"
    options = ["Reconstruction", "Breast Conservation Surgery (BCS)", "Therapeutic Mammoplasty"]
    surg_type = ask_option (category, options)
    if (surg_type == "Reconstruction"):
        category = "Type Reconstruction"
        options = ["Mastectomy/Modified Radical Mastectomy", "Implant"]
        surg_type = ask_option(category, options)
    elif (surg_type == "Breast Conservation Surgery"):
        category = "Type Breast Conservation Surgery"
        options = ["Therapeutic Mammoplasty/Reduction Mammoplasty", "Wide Local Excision"] 
        surg_type = ask_option(category, options)
    category = "Response to Surgery"
    options = ["Complete_Remission/No Residual Tumor", "Progressing", "Partial", "Static"]
    surg_response = ask_option(category, options)
    data = surg_block_id, surg_no_block, surg_block_source, surg_tumour_block, surg_node_block, surg_normal_block, \
           surg_red_block, surg_date, surg_name, surg_hosp_id, lesion_side, surg_type, surg_response
    columns = "Surgical_Block_ID", "Surgery_No_of_blocks", "Block_Source", "Tumor_block_ref", "Nodes_block_ref", \
              "Ad_Normal_block_ref", "Reduction_tissue_block_ref", "Date_of_Surgery", "Name_Surgeon", "Hospital_ID", \
              "Lesion_Side", "Type_surgery", "Response_surgery"
    update_multiple(conn, cursor, table, columns, file_number, data)
def surgery_block (conn, cursor, file_number, table):
    from ask_y_n_statement import ask_option
    from add_update_sql import update_multiple
    tumour_size = input ("Tumour size: ")
    tumour_grade = input ("Tumour Grade (1, 2, or 3: ")
    check = False
    while not check:
        val = ['1', '2', '3']
        check = tumour_grade is val
    category = "Surgery Diagnosis"
    options = ["Ductal carcinoma in situ(DCIS)", "Invasive Ductal Carcinoma"]
    surg_diag = ask_option(category, options)
    if (surg_diag == "Ductal carcinoma in situ(DCIS)"):
        dcis_percent = input (Percent DCIS)
        category = "DCIS Invasion"
        options = {'Microinvasion', 'Macroinvasion'}
        dcis_invasion = ask_option(category, options)
    else:
        dcis_percent = "NA"
        dcis_invasion = "NA"



surgery_block = DCIS_Percent_Surgery_Block_Report", "DCIS_Invasion_Surgery_Block_Report", \
                "Perineural_Invasion_Surgery_Block_Report", "Necrosis_Surgery_Block_Report", \
                "Lymphovascular_Invasion_Surgery_Block_Report", "Margins_Surgery_Block_Report", \
                "Surgery_Block_Report"
surgery_block = "Tumour_size_Surgery_Block_Report", "Grade_Surgery_Block_Report", "Diagnosis_Surgery_Block_Report",
                "DCIS_Percent_Surgery_Block_Report", "DCIS_Invasion_Surgery_Block_Report", \
                "Perineural_Invasion_Surgery_Block_Report", "Necrosis_Surgery_Block_Report", \
                "Lymphovascular_Invasion_Surgery_Block_Report", "Margins_Surgery_Block_Report", \
                "Surgery_Block_Report"