def physical_activity_table(conn, cursor, file_number, mr_number, name):
    from add_update_sql import insert
    table_act = "Physical_Activity"
    columns = "File_number, MR_number, Name, Type_activity, Frequency_activity"
    add_act = "y"
    while str.lower(add_act) == "y":
        type_phys_act = input("Type of physical activity: ")
        freq_phys_act = input("Frequency of physical activity: ")
        data = file_number, mr_number, name, type_phys_act, freq_phys_act
        insert(conn, cursor, table_act, columns, data)
        print("Add further activities?")
        add_act = input("(y/n): ")

def cancer_table(conn, cursor, file_number, mr_number, name):
    #add yes_no and NA. Remove yes no column
    from add_update_sql import insert
    table_cancer = "Previous_Cancer_History"
    add_cancer = "y"
    while str.lower(add_cancer) == "y":
        type_of_cancer = input("Type of Cancer: ")
        year_diagnosis = input("Year of diagnosis: ")
        columns = ("File_number, MR_number, Name, Type_Cancer, Year_diagnosis")
        data = file_number, mr_number, name, type_of_cancer, year_diagnosis
        insert(conn, cursor, table_cancer, columns, data)
        surgery_y_n = input("Surgical treatment (y/n)?")
        type_surgery = "No Surgery"
        if str.lower(surgery_y_n) == "y":
            surgery_y_n = "Surgical treatment"
            type_surgery = input("Type of surgery: ")
        radiation_y_n = input("Radiation Treatment (y/n): ")
        type_radiation = "No Radiation"
        duration_radiation = "No Radiation"
        if str.lower(radiation_y_n) == "y":
            radiation_y_n = "Radiation Treatment"
            type_radiation = input("Type of radiation: ")
            duration_radiation = input("Duration of treatment: ")
        chemotherapy_y_n = input("Chemotherapy Treatment (y/n): ")
        type_chemotherapy = "No Chemotherapy"
        duration_chemotherapy = "No Chemotherapy"
        if str.lower(chemotherapy_y_n) == "y":
            chemotherapy_y_n = "Chemotherapy Treatment"
            type_chemotherapy = input("Type of chemotherapy: ")
            duration_chemotherapy = input("Duration of treatment: ")
        hormone_y_n = input("Hormone Treatment (y/n): ")
        type_hormone = "No Hormone Treatment"
        duration_hormone = "No Hormone Treatment"
        if str.lower(hormone_y_n) == "y":
            hormone_y_n = "Hormone Treatment"
            type_hormone = input("Type of hormone: ")
            duration_hormone = input("Duration of treatment: ")
        alternative_y_n = input("Alternative Treatment (y/n): ")
        type_alternative = "No Alternative Treatment"
        duration_alternative = "No Alternative Treatment"
        if str.lower(alternative_y_n) == "y":
            alternative_y_n = "Alternative Treatment"
            type_alternative = input("Type of alternative medication: ")
            duration_alternative = input("Duration of treatment: ")
        home_y_n = input("Home Remedy (y/n): ")
        type_home = "No Home Remedy Treatment"
        duration_home = "No Home Remedy Treatment"
        if str.lower(home_y_n) == "y":
            home_y_n = "Home Remedy Treatment"
            type_home = input("Type of home remedy: ")
            duration_home = input("Duration of treatment: ")
        columns = "File_number, MR_number, Name, Type_Cancer, Year_diagnosis, Surgery, Type_Surgery,Radiation," \
                  "Type_Radiation,Duration_Radiation, Chemotherapy, Type_Chemotherapy,Duration_Chemotherapy, Hormone, " \
                  "Type_Hormone, Duration_Hormone, Alternative_Treatment,Type_Alternative_Treatment, " \
                  "Duration_Alternative_Treatment, Home_Remedy,Type_Home_Remedy, Duration_Home_Remedy"
        new_data = file_number, mr_number, name, type_of_cancer, year_diagnosis, surgery_y_n, type_surgery, \
                   radiation_y_n, type_radiation, duration_radiation, chemotherapy_y_n, type_chemotherapy, \
                   duration_chemotherapy, hormone_y_n, type_hormone, duration_hormone, alternative_y_n, \
                   type_alternative, duration_alternative, home_y_n, type_home, duration_home
        insert(conn, cursor, table_cancer, columns, new_data)
        print("Additional cancer history")
        add_cancer = input("y/n: ")


def nut_supp_table(conn, cursor, file_number, mr_number, name):
    from add_update_sql import insert
    add_supp = "y"
    table_nut = "Nutritional_Supplements"
    columns = "File_number, MR_number, Name, Type_nutritional_supplements, Quantity_nutritional_supplements_per_day, " \
              "Duration_nutritional_supplements"
    while str.lower(add_supp) == "y":
        nut_supplements_type = input("Type of nutritional supplements taken: ")
        nut_supplements_quant = input("Quantity of nutritional supplements taken per day: ")
        nut_supplements_duration = input("Duration of nutritional supplements use: ")
        new_data = file_number, mr_number, name, nut_supplements_type, nut_supplements_quant, nut_supplements_duration
        insert(conn, cursor, table_nut, columns, new_data)
        print('Add more nutritional supplements')
        add_supp = input('y/n: ')


def med_history_table (conn, cursor, file_number, mr_number, name):
    from add_update_sql import insert
    add_history = "y"
    while (str.lower(add_history) == "y"):
        condition = input("Condition : ")
        diagnosis_date = input("Date of diagnosis: ")
        treatment = input("Treatment: ")
        history = file_number, mr_number, name, condition, diagnosis_date, treatment
        table_med = "General_Medical_History"
        columns = "File_number, MR_number, Name, Condition, Diagnosis_date, Treatment"
        insert(conn, cursor, table_med, columns, history)
        print('Add more history')
        add_history = input('y/n: ')


def family_cancer_table(conn, cursor, file_number, mr_number, name):
    add_family = "y"
    # all_data = []
    while str.lower(add_family) == "y":
        type_of_cancer = input("Type of Cancer: ")
        relation_to_patient = input('Relation_to_patient :')
        age_at_detection_yrs = input('Age at detection (yrs)" :')
        family_history = file_number, mr_number, name, type_of_cancer, relation_to_patient, age_at_detection_yrs
        #	family_history_list = [file_number, mr_number, name, type_of_cancer, relation_to_patient, age_at_detection_yrs]
        #	all_data.append(family_history_list)
        cursor.execute(
            'INSERT INTO Family_Cancer_History (File_number, MR_number, Name, Type_Cancer, Relation_to_patient, Age_at_detection_yrs) VALUES (?, ?, ?, ?, ?, ?)',
            family_history)
        conn.commit()
        print("Add more family cancer history? ")
        add_family = input("y/n: ")


# type_of_cancer = get_rb_lb(all_data, 3)
# relation_to_patient = get_rb_lb(all_data, 4)
# age_at_detection_yrs = get_rb_lb (all_data, 5)
# data = [type_of_cancer, relation_to_patient, age_at_detection_yrs]
# for index in range(0,len(data)):
# data[index] = ["; ".join(data[index])]
# data_flat = [item for sublist in data for item in sublist]
# new_data = tuple(data_flat)
# columns = "Family_Type_Cancer","Relation_to_patient", "Age_at_detection_yrs"
# table = "Patient_Information_History"
# update_multiple (conn, cursor, table, columns, file_number, data)


def other_symp(conn, cursor, file_number, table):
    from add_update_sql import update_multiple
    from ask_y_n_statement import get_rb_lb
    #data = file_number, mr_number, name
    add_symp = "y"
    all_data = []
    while str.lower(add_symp) == "y":
        other_symp = input("Type of symptom: ")
        symp_breast_right = input("Right Breast y/n: ")
        if str.lower(symp_breast_right) == "y":
            symp_breast_right = other_symp
            symp_duration_right = input("Duration of symptoms in right breast: ")
        else:
            symp_breast_right = None
            symp_duration_right = None
        symp_breast_left = input("Left Breast y/n: ")
        if str.lower(symp_breast_left) == "y":
            symp_breast_left = other_symp
            symp_duration_left = input("Duration of symptoms in left breast: ")
        else:
            symp_breast_left = None
            symp_duration_left = None
        RB = [symp_breast_right, symp_duration_right]
        LB = [symp_breast_left, symp_duration_left]
        data = [RB, LB]
        all_data.append(data)
        print("Include more symptoms?")
        add_symp = input("y/n: ")
    rb = get_rb_lb(all_data, 0)
    rb_symp = list(filter(None, get_rb_lb(rb, 0)))
    rb_dur = list(filter(None, get_rb_lb(rb, 1)))
    lb = get_rb_lb(all_data, 1)
    lb_symp = list(filter(None, get_rb_lb(lb, 0)))
    lb_dur = list(filter(None, get_rb_lb(lb, 1)))
    data = [rb_symp, rb_dur, lb_symp, lb_dur]
    data = [rb_symp, rb_dur, lb_symp, lb_dur]
    for index in range(0, len(data)):
        if not data[index]:
            data[index] = ["No other symptoms"]
        else:
            data[index] = ["; ".join(data[index])]
    data_flat = [item for sublist in data for item in sublist]
    new_data = tuple(data_flat)
    columns = "RB_Other_Symptoms", "RB_Other_Symptoms_duration", "LB_Other_Symptoms", "RB_Other_Symptoms_duration"
    update_multiple(conn, cursor, table, columns, file_number, new_data)
