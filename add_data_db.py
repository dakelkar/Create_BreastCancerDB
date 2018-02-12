import sqlite3
from breast_cancer_tables import *
from gen_info_tables import *
from add_update_sql import *
db_name = 'DB\\BreastCancerDB_test_2018-02-12.db'
conn = sqlite3.connect(db_name)
cursor = conn.cursor()
new = "y"
while str.lower(new) == "y":
    print("Please enter new record")
    file_number = input("File Number: ")
    mr_number = input('MR_number :')
    name = input('Name :')
    date_first = input("Date of first visit: ")
    permanent_address = input('Permanent_Address :')
    current_address = input('Current_Address :')
    phone = input('Phone :')
    email_id = input('Email_ID :')
    gender = input('Gender :')
    age_yrs = input('Age_yrs :')
    date_of_birth = input('Date_of_Birth :')
    height_cm = input('Height_cm :')
    weight_kg = input('Weight_kg :')
    height = int(height_cm) / 100
    weight = int(weight_kg)
    BMI = str(round(weight / (height * height)))
    diet = input("Type of diet: ")
    columns = "File_number, MR_number, Name, FirstVisit_Date, Permanent_Address, Current_Address, Phone, Email_ID, " \
              "Gender, Age_yrs, Date_of_Birth, Height_cm, Weight_kg, BMI," \
              "Diet"
    new_data = file_number, mr_number, name, date_first, permanent_address, current_address, phone, email_id, gender, \
               age_yrs, date_of_birth, height_cm, weight_kg, BMI, diet
    table = "Patient_Information_History"
    insert(conn, cursor, table, columns, new_data)
    habits(conn, cursor, file_number, table)
    nut_supplements(conn, cursor, file_number, mr_number, name, table)
    phys_act(conn, cursor, file_number, mr_number, name, table)
    med_history(conn, cursor, file_number, mr_number, name, table)
    cancer_history(conn, cursor, file_number, mr_number, name, table)
    family_details(conn, cursor, file_number, table)
    family_cancer_history_y_n = input('Cancer history in Family (y/n) :')
    if str.lower(family_cancer_history_y_n) == "y":
        family_cancer_table(conn, cursor, file_number, mr_number, name)
        family_cancer_history_y_n = "Family History of Cancer"
    else:
        family_cancer_history_y_n = "No Family History of Cancer"
    update_single(conn, cursor, table, "FamilyCancer_history_y_n", file_number, family_cancer_history_y_n)
    repro_details(conn, cursor, file_number, table)
    symp_state = "Pain or tenderness", "Lumps", "Nipple Discharge", "Nipple Retraction", "Dimpling",\
                 "Discolouration", "Ulceration", "Eczema"
    breast_symptoms(conn, cursor, file_number, table, symp_state)

    det_by(conn, cursor, table, file_number)
    metastasis_symp(conn, cursor, file_number, table)
    print("Enter next new record?")
    new = input("y/n: ")
conn.close()
