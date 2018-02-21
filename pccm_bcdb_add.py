def add_new(conn, cursor, file_number, table):
    from ask_y_n_statement import ask_option, ask_y_n
    import block_report_data
    import gen_info_tables
    import clinical_exam
    options = ["General Information", "Block Report", "Clinical Exam", "All"]
    check = ask_option("Enter new record for ", options)
    if check == "General Information" or check == "All":
        enter = ask_y_n("Enter Patient Biographical Information")
        if enter:
            gen_info_tables.bio_info(conn, cursor, file_number, table)
        enter = ask_y_n("Enter Patient habits")
        if enter:
            gen_info_tables.phys_act(conn, cursor, file_number, table)
            gen_info_tables.habits(conn, cursor, file_number, table)
            gen_info_tables.nut_supplements(conn, cursor, file_number, table)
        enter = ask_y_n("Enter Patient family and reproductive details?")
        if enter:
            gen_info_tables.family_details(conn, cursor, file_number, table)
            gen_info_tables.repro_details(conn, cursor, file_number, table)
        enter = ask_y_n("Enter Patient and family medical history?")
        if enter:
            gen_info_tables.med_history(conn, cursor, file_number, table)
            gen_info_tables.cancer_history(conn, cursor, file_number, table)
            gen_info_tables.family_cancer(conn, cursor, file_number, table)
        enter = ask_y_n("Enter Patient Symptoms?")
        if enter:
            gen_info_tables.det_by(conn, cursor, table, file_number)
            gen_info_tables.breast_symptoms(conn, cursor, file_number, table)
            gen_info_tables.metastasis_symp(conn, cursor, file_number, table)
    if check == "Block Report" or check == "All":
        enter = ask_y_n("Enter Block Report information?")
        if enter:
            block_report_data.block_report_info(conn, cursor, file_number, table)
        enter = ask_y_n("Enter Tumour Biopsy data?")
        if enter:
            block_report_data.tumour_biopsy_data(conn, cursor, file_number, table)
        enter = ask_y_n("Enter Lymphnode Biopsy data?")
        if enter:
            block_report_data.lymphnode_biopsy(conn, cursor, file_number, table)
        enter = ask_y_n("Enter Surgery Information?")
        if enter:
            block_report_data.surgery_info(conn, cursor, file_number, table)
        enter = ask_y_n("Enter Surgery Block Report?")
        if enter:
            block_report_data.surgery_block(conn, cursor, file_number, table)
        enter = ask_y_n("Enter Patient family and reproductive details?")
        if enter:
            block_report_data.node_block(conn, cursor, file_number, table)
        enter = ask_y_n("Enter Pathological Stage?")
        if enter:
            block_report_data.path_stage(conn, cursor, file_number, table)
    if check == "Clinical Exam" or check == "All":
        enter = ask_y_n("Enter Initial Clinical Examination?")
        if enter:
            clinical_exam.clinical_exam_initial(conn, cursor, file_number, table)
        enter = ask_y_n("Nipple Cytology and Mammography details?")
        if enter:
            clinical_exam.nipple_cytology(conn, cursor, file_number, table)
            clinical_exam.mammography(conn, cursor, file_number, table)


def update_record(conn, cursor, file_number, table):
    from ask_y_n_statement import ask_option, ask_y_n
    import block_report_data
    import gen_info_tables
    import clinical_exam
    options = ["General Information", "Block Report", "Clinical Information"]
    check = ask_option("Update Record for", options)
    if check == "General Information":
        enter = ask_y_n("Enter Patient Biographical Information")
        if enter:
            gen_info_tables.bio_info(conn, cursor, file_number, table)
        enter = ask_y_n("Enter Patient habits")
        if enter:
            gen_info_tables.phys_act(conn, cursor, file_number, table)
            gen_info_tables.habits(conn, cursor, file_number, table)
            gen_info_tables.nut_supplements(conn, cursor, file_number, table)
        enter = ask_y_n("Enter Patient family and reproductive details?")
        if enter:
            gen_info_tables.family_details(conn, cursor, file_number, table)
            gen_info_tables.repro_details(conn, cursor, file_number, table)
        enter = ask_y_n("Enter Patient and family medical history?")
        if enter:
            gen_info_tables.med_history(conn, cursor, file_number, table)
            gen_info_tables.cancer_history(conn, cursor, file_number, table)
            gen_info_tables.family_cancer(conn, cursor, file_number, table)
        enter = ask_y_n("Enter Patient Symptoms?")
        if enter:
            gen_info_tables.det_by(conn, cursor, table, file_number)
            gen_info_tables.breast_symptoms(conn, cursor, file_number, table)
            gen_info_tables.metastasis_symp(conn, cursor, file_number, table)
    if check == "Block Report":
        enter = ask_y_n("Enter Block Report information?")
        if enter:
            block_report_data.block_report_info(conn, cursor, file_number, table)
        enter = ask_y_n("Enter Tumour Biopsy data?")
        if enter:
            block_report_data.tumour_biopsy_data(conn, cursor, file_number, table)
        enter = ask_y_n("Enter Lymphnode Biopsy data?")
        if enter:
            block_report_data.lymphnode_biopsy(conn, cursor, file_number, table)
        enter = ask_y_n("Enter Surgery Information?")
        if enter:
            block_report_data.surgery_info(conn, cursor, file_number, table)
        enter = ask_y_n("Enter Surgery Block Report?")
        if enter:
            block_report_data.surgery_block(conn, cursor, file_number, table)
        enter = ask_y_n("Enter Patient family and reproductive details?")
        if enter:
            block_report_data.node_block(conn, cursor, file_number, table)
        enter = ask_y_n("Enter Pathological Stage?")
        if enter:
            block_report_data.path_stage(conn, cursor, file_number, table)
    if check == "Clinical Exam":
        enter = ask_y_n("Enter Initial Clinical Examination?")
        if enter:
            clinical_exam.clinical_exam_initial(conn, cursor, file_number, table)
        enter = ask_y_n("Nipple Cytology and Mammography details?")
        if enter:
            clinical_exam.nipple_cytology(conn, cursor, file_number, table)
            clinical_exam.mammography(conn, cursor, file_number, table)