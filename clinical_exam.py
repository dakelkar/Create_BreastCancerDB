def clinical_exam_initial (conn, cursor, file_number, table):
    import ask_y_n_statement
    from add_update_sql import update_multiple
    prov_diag = input ("Provisional Diagnosis: ")
    options = ["Definite", "Vague", "Diffuse", "Nil", "Other"]
    lump_palp = ask_y_n_statement.ask_option("Palpable lump in the breast?", options)
    lump_location = ask_y_n_statement.ask_option("Location of lump", ["Right Breast", "Left Breast", "Both", "Not present"])
    lump_location_data = []
    if lump_location == "Right Breast" or lump_location == "Both":
        category = "Lump location on Right Breast"
        options = ["UOQ", "UIQ", "C", "UCQ", "LCQ", "LOQ", "LIQ"]
        lump_location_rb = ask_y_n_statement.ask_option(category, options)
        lump_location_rb_data = "RB-"+lump_location_rb
        lump_location_data.append(lump_location_rb_data)
    if lump_location == "Left Breast" or lump_location == "Both":
        category = "Lump location on Left Breast"
        options = ["UOQ", "UIQ", "C", "UCQ", "LCQ", "LOQ", "LIQ"]
        lump_location_lb = ask_y_n_statement.ask_option(category, options)
        lump_location_lb_data = "LB-" + lump_location_lb
        lump_location_data.append(lump_location_lb_data)
    lump_location_data = "; ".join(lump_location_data)
    if lump_location == "Not present":
        lump_location_data = "Lump" + lump_location
        lump_size, lump_number,lump_consistency,lump_fixity  = "NA", "NA", "NA", "NA"
    else:
        lump_size = input("Lump size")
        lump_number = ask_y_n_statement.ask_option("Number of lumps", ["Single", "Multiple", "Other"])
        lump_consistency = ask_y_n_statement.ask_option("Consistency of lumps", ["Soft", "Firm", "Hard", "Cystic",
                                                                                 "Mobile", "Other"])
        lump_fixity = ask_y_n_statement.ask_option("Lump fixity to ", ["Skin", "Chest wall", "Pectoral major muscle",
                                                                       "No Fixation", "Other"])
    mastitis_location = ask_y_n_statement.ask_option("Location of mastitis",
                                                 ["Right Breast", "Left Breast", "Both", "Not present"])
    mastitis_location_data = []
    if mastitis_location == "Right Breast" or mastitis_location == "Both":
        category = "Mastitis location on Right Breast"
        options = ["UOQ", "UIQ", "C", "UCQ", "LCQ", "LOQ", "LIQ"]
        mastitis_location_rb = ask_y_n_statement.ask_option(category, options)
        mastitis_location_rb_data = "RB-" + mastitis_location_rb
        mastitis_location_data.append(mastitis_location_rb_data)
    if mastitis_location == "Left Breast" or mastitis_location == "Both":
        category = "Mastitis location on Left Breast"
        options = ["UOQ", "UIQ", "C", "UCQ", "LCQ", "LOQ", "LIQ"]
        mastitis_location_lb = ask_y_n_statement.ask_option(category, options)
        mastitis_location_lb_data = "LB-" + mastitis_location_lb
        mastitis_location_data.append(mastitis_location_lb_data)
    mastitis_location_data = "; ".join(mastitis_location_data)
    if mastitis_location == "Not present":
        mastitis_location_data = "mastitis" + mastitis_location
        mastitis_type = "NA"
    else:
        mastitis_type = ask_y_n_statement.ask_option("Mastitis type", ["Diffuse", "Sectoral", "Other"])
    tender = ask_y_n_statement.ask_option("Tenderness in breast ?",["Right Breast", "Left Breast", "Both", "Not Present", "Other"])
    retract = ask_y_n_statement.ask_option("Nipple Retraction ?",["Right Breast", "Left Breast", "Both", "Not Present", "Other"])
    discharge = ask_y_n_statement.ask_option("Nipple Discharge ?",
                                 ["Right Breast", "Left Breast", "Both", "Not Present", "Other"])
    if discharge == "Not Present":
        discharge_type = "NA"
    else:
        discharge_type = ask_y_n_statement.ask_option("Discharge Type?",
                                 ["Serous", "Milky", "Brown", "Bloody", "Other"])
    skin_change_location = ask_y_n_statement.ask_option("Skin Changes?",
                                 ["Right Breast", "Left Breast", "Both", "Not Present", "Other"])
    if skin_change_location == "Not Present":
        skin_change_type = "NA"
    else:
        skin_change_type = ask_y_n_statement.ask_option("Type of skin change?",
                                 ["Dimpling", "Ulceration", "Discolouration", "Eczema", "Edema", "Redness",
                                  "Peau d'orange", "Other"])
    ax_nodes = ask_y_n_statement.ask_option("Palpable axillary nodes",
                                 ["Right Breast", "Left Breast", "Both", "Not palpable", "Other"])
    if ax_nodes == "Not palpable":
        ax_nodes_number, ax_nodes_size, ax_nodes_fixity = "NA", "NA", "NA"
    else:
        ax_nodes_number = input("Number of nodes: ")
        ax_nodes_size = input("Size of nodes: ")
        ax_nodes_fixity =  ask_y_n_statement.ask_y_n("Fixity of axillary nodes", "Yes", "No")
    supra_nodes = ask_y_n_statement.ask_option("Palpable supraclavicular nodes",
                                            ["Right Breast", "Left Breast", "Both", "Not palpable", "Other"])
    if supra_nodes == "Not palpable":
        supra_nodes_number, supra_nodes_size, supra_nodes_fixity = "NA", "NA", "NA"
    else:
        supra_nodes_number = input("Number of nodes: ")
        supra_nodes_size = input("Size of nodes: ")
        supra_nodes_fixity = ask_y_n_statement.ask_y_n("Fixity of supraclavicular nodes", "Yes", "No")
    contra_breast = ask_y_n_statement.ask_option("Contralateral Breast", ["Nomral", "Diffuse Mastitis", "Localised Mastitis", "Other"])
    arm_edema = ask_y_n_statement.ask_option("Edema of arm", ["Right", "Left", "Both", "Not Present", "Other"])
    arm_circ_right = input("Circumference of right arm (cm): ")
    arm_volume_right = input("Upper limb volume - right arm (cc): ")
    arm_elbow_right = input("Distance from the elbow - right arm (cm): ")
    arm_circ_left = input("Circumference of left arm (cm): ")
    arm_volume_left = input("Upper limb volume - left arm (cc): ")
    arm_elbow_left = input("Distance from the elbow - left arm (cm): ")

    data = prov_diag, lump_palp, lump_location_data, lump_size, lump_number, lump_consistency, lump_fixity, \
           mastitis_location_data, mastitis_type, tender, retract, discharge, discharge_type, skin_change_location, \
           skin_change_type, ax_nodes, ax_nodes_number, ax_nodes_size, ax_nodes_fixity, supra_nodes, supra_nodes_number, \
           supra_nodes_size, supra_nodes_fixity, contra_breast, arm_edema, arm_circ_right, arm_volume_right, \
           arm_elbow_right, arm_circ_left, arm_volume_left, arm_elbow_left

    columns = 'Provisional_Diagnosis_Clinical_Examination_CE', 'Lump_Palpable_CE', 'Lump_Location_CE', 'Lump_Size_CE', 'Lump_Number_CE', \
              'Lump_Consistency_CE', 'Lump_Fixity_CE', 'Mastitis_CE', 'Mastitis_type_CE', 'Tenderness_CE', \
              'Nipple_Retraction_CE', 'Nipple_Discharge_CE', 'Nipple_Discharge_Type_CE', 'Skin_changes_CE', \
              'Skin_change_type_CE', 'Palpable_axillary_nodes_CE', 'Palpable_axillary_nodes_number_CE', \
              'Palpable_axillary_nodes_size_CE', 'Palpable_axillary_nodes_fixity_CE', \
              'Palpable_supraclavicular_nodes_CE', 'Palpable_supraclavicular_nodes_number_CE', \
              'Palpable_supraclavicular_nodes_size_CE', 'Palpable_supraclavicular_nodes_fixity_CE', \
              'Contralateral_Breast_CE', 'Edema_arm_CE', 'RightArm_Circumference_cm_CE', \
              'RightArm_UpperLimbVolume_cc_CE', 'RightArm_ElbowDistance_cm_CE', 'LeftArm_Circumference_cm_CE', \
              'LeftArm_UpperLimbVolume_cc_CE', 'LeftArm_ElbowDistance_cm_CE'
    update_multiple(conn, cursor, table, columns, file_number, data)

def nipple_cytology (conn, cursor, file_number, table):
    import ask_y_n_statement
    import add_update_sql
    cyto = ask_y_n_statement.ask_option("Nipple Cytology", ["Done", "Not Done"])
    if cyto == "Not Done":
        cyto_date, cyto_number, cyto_report = "NA", "NA", "NA"
    else:
        cyto_date = input("Date of nipple cytology: ")
        cyto_number = input("Nipple Cytology number: ")
        cyto_report = ask_y_n_statement.ask_option("Nipple Cytology report and interpretation", ["Normal", "Suspicious", "Diagnostic for Cancer", "Other"])
    data = cyto, cyto_date, cyto_number, cyto_report
    columns = "Nipple_Cytology", "Date_Nipple_Cytology", "Number_Nipple_Cytology", "Report_Nipple_Cytology"
    add_update_sql.update_multiple(conn, cursor, table, columns, file_number, data)

def mammography (conn, cursor, file_number, table):
    import ask_y_n_statement
    import add_update_sql
    mammo_loc = ask_y_n_statement.ask_option("Mammography Diagnosis at", ["PCCM", "Outside", "Other"])
    mammo_details = ask_y_n_statement.ask_y_n("First Mammography?")
    mammo_date = input("Date of last mammography done: ")
    if mammo_details:
        mammo_details = "First Mammography"
        mammo_number, mammo_rep_previous = "NA", "NA"
    else:
        mammo_details = "More than one Mammography"
        mammo_number = input ("Number of mammographies undergone: ")
        mammo_rep_previous = input ("Report of previous mammography: ")
    mammo = ask_y_n_statement.ask_y_n("Mammography diagnosis done")
    if mammo:
        mammo = "Mammography diagnosis done"
        mammo_diag_date = input("Date of mammography diagnosis: ")
        mammo_diag_acc = input ("Accession number of mammography diagnosis")
    else:
        mammo = "Mammography diagnosis not done"
        mammo_diag_date, mammo_diag_acc = "NA", "NA"
    mammo_lesion = ask_y_n_statement.ask_option("Location of lesion",
                                                         ["Right Breast", "Left Breast", "Both", "Not present"])
    mammo_lesion_data = []
    if mammo_lesion == "Right Breast" or mammo_lesion == "Both":
        category = "Mastitis location on Right Breast"
        options = ["UOQ", "UIQ", "C", "UCQ", "LCQ", "LOQ", "LIQ"]
        mammo_lesion_rb = ask_y_n_statement.ask_option(category, options)
        mammo_lesion_rb_data = "RB-" + mammo_lesion_rb
        mammo_lesion_data.append(mammo_lesion_rb_data)
    if mammo_lesion == "Left Breast" or mammo_lesion == "Both":
        category = "Mastitis location on Left Breast"
        options = ["UOQ", "UIQ", "C", "UCQ", "LCQ", "LOQ", "LIQ"]
        mammo_lesion_lb = ask_y_n_statement.ask_option(category, options)
        mammo_lesion_lb_data = "LB-" + mammo_lesion_lb
        mammo_lesion_data.append(mammo_lesion_lb_data)
    mammo_lesion_data = "; ".join(mammo_lesion_data)
    if mammo_lesion == "Not present":
        mammo_lesion_data = "Lesion" + mammo_lesion
    mammo_shape = ask_y_n_statement.ask_option("Shape", ["Oval", "Round", "Irregular"])
    mammo_size = input ("Size: ")
    mammo_margin = ask_y_n_statement.ask_option("Margins", ["Circumscribed", "Obscured", "Indistinct", "Spiculated", "Other"])
    mammo_density = ask_y_n_statement.ask_option("Density", ["High Density", "Equal Density", "Low Density",
                                                            "Fat-containing", "Other"])
    mammo_calcification = ask_y_n_statement.ask_option("Calcification Type", ["Skin", "Vascular",
    "Coarse or 'Popcorn-like'", "Large Rod-like", "Round and punctate", "Lucent-Centered", "Eggshell or Rim",
    "Milk of Calcium", "Suture", "Dystrophic", "Amorphous", "Coarse Heterogeneous", "Fine Pleomorphic",
                                            "Fine Linear or Fine Linear Branching", "Other"])
    mammo_calcification_type = ask_y_n_statement.ask_option("Is calcification type", ["Typically Benign",
                                                                                      "Suspicious Morphology", "Other"])
    mammo_arch = ask_y_n_statement.ask_option("Architectural distortion", ["Right", "Left", "Both", "Not present"])
    mammo_asymm = ask_y_n_statement.ask_option("Asymmetry", ["Global", "Focal", "Developing", "Not present", "Other"])
    mammo_intra = ask_y_n_statement.ask_option("Intra mammary lymph nodes", ["Right", "Left", "Both", "Other"])
    mammo_lesion_skin = ask_y_n_statement.ask_option("Skin Lesion",["Right", "Left", "Both", "Other"] )
    mammo_dil = ask_y_n_statement.ask_option("Solitary Dilated duct",["Right", "Left", "Both", "Other"])
    asso_feat = ["Skin Retraction", "Nipple Retraction", "Skin Thickening", "Trabecular Thickening",
                 "Axillary lymphadenopathy"]
    asso_feat_data = []
    for index in (asso_feat):
        var = ask_y_n_statement.ask_option(index, ["Right", "Left", "Both", "Other"])
        asso_feat_data.append(var)
    asso_feat_1, asso_feat_2, asso_feat_3, asso_feat_4, asso_feat_5 = asso_feat_data
    mammo_sec = input ("Secondary Lesion/Contralateral Lesion: ")
    mammo_dist = input ("Distance from Skin (cm): ")
    mammmo_pect = input ("Distance from Pectoralis Major (cm): ")
    mammo_birads = ask_y_n_statement.ask_option("BI-RADS", ["0", "I", "II", "III", "IV", "IVA", "IVB","IVC" "V"])

    data = mammo_loc, mammo_details, mammo_date, mammo_number, mammo_rep_previous, mammo, mammo_diag_date, mammo_diag_acc, \
           mammo_lesion, mammo_lesion_data, mammo_shape, mammo_size, mammo_margin, mammo_density, mammo_calcification, \
           mammo_calcification_type, mammo_arch, mammo_asymm, mammo_intra, mammo_lesion_skin, mammo_dil,  asso_feat_1, \
           asso_feat_2, asso_feat_3, asso_feat_4, asso_feat_5, mammo_sec, mammo_dist, mammmo_pect,  mammo_birads
    columns = 'DiagnosisLocation_Mammography', 'First_Mammography', 'LatestDate_Mammography', 'Number_Mammography', \
              'PreviousDate_Mammography', 'Diagnosis_Mammography', 'Date_Diagnosis_Mammography', 'AccessionNumber_Mammography', \
              'Lesion_Mammography', 'LesionLocation_Mammography', 'Shape_Mammography', 'Size_Mammography', \
              'Margin_Mammography', 'Density_Mammography', 'Calcification_Mammography', \
              'Calcification_Implication_Mammography', 'Architecture_Mammography', 'Asymmetry_Mammography', \
              'IntraMammaryLN_Mammography', 'SkinLesion_Mammography', 'DilatedDuct_Mammography', \
              'Features_SkinRetraction_Mammography', 'Features_NippleRetraction_Mammography', \
              'Features_SkinThickening_Mammography', 'Features_TrabecularThickening_Mammography', \
              'Features_AxillaryLymphadenopathy_Mammography', 'SecondaryLesion_ContralateralBreast_Mammography', \
              'DistancefromSkin_Mammography', 'DistanceFromPectMaj_Mammography', 'BIRADS_Mammography'
    add_update_sql.update_multiple(conn, cursor, table, columns, file_number, data)
