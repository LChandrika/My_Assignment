class Hospital:
   
    def __init__(self):
        self.patients= []

    def add_patient(self,Patient_Id,Patient_Name,Patient_Age,Patient_Gender,Patient_Diagnosis):
        patient = {
            "ID"        : Patient_Id,
            "Name"      : Patient_Name,
            "Age"       : Patient_Age,
            "Gender"    : Patient_Gender,
            "Diagnosis" : Patient_Diagnosis
        }

        self.patients.append(patient)

    def display_patients(self):

        if not self.patients:
            print("No Patients in this Hospital....")

        else:
            for x in self.patients:
                print("Patient ID        : ",x['ID'])
                print("Patient Name      : ",x['Name'])
                print("Patient Age       : ",x['Age'])
                print("Patient Gender    : ",x['Gender'])    
                print("Patient Diagnosis : ",x['Diagnosis'])
                print("     ")

    def search_patient(self,Patient_id):

        for x in self.patients:
            if x['ID'] ==Patient_id:
                print("Patient Found")
                print("Patient ID :",x['ID'])
                print("Patient Name :",x["Name"])
                print("Patient Age : ",x['Age'])
                print("Patient Gender : ",x['Gender'])
                print("Patient Diagnosis : ",x['Diagnosis'])
                return
        print("Patient With ID : ",Patient_id," Not Found")

    def delete_patient(self,patient_id):

        for x in self.patients:
            if x['ID'] ==patient_id:
                self.patients.remove[x]
                print("Patient With ID", patient_id," Deleted Sucess fully...")
                return
        print("Patient With ID ",patient_id, " Not Found ")
        
    def update_patient(self,patient_id,diagnosiss):

        for x in self.patients:
            if x['ID'] == patient_id:
                x['Diagnosis'] = diagnosiss
                print("Patient information updated....")
                return
        print("patient with ID ",patient_id, " Not Found.... ")

main = Hospital()

while True:
    print(".....................WELCOME TO MAROLIX HOSPITAL....................")
    print("     1. ADD A NEW PATIENT                : ")
    print("     2.DISPLAY ALL PATIENTS              : ")
    print("     3.SEARCH A PATIENT BY ID            : ")
    print("     4.DELETE A PATIENT BY ID            :  ")
    print("     5.UPDATE A PATIENT DIAGNOSIS BY ID  : ")
    print("     6.EXIT")
    choice =input("Enter your option :  ")

    if choice== '1':
        Patient_Id        = int(input("Enter Patient ID     : "))
        Patient_Name      = input("Enter Patient Name       : ")
        Patient_Age       = int(input("Enter Patient Age    : "))
        Patient_Gender    = input("Enter patient Gender     : ")
        Patient_Diagnosis = input("Enter patient Diagnosis  : ")
        main.add_patient(Patient_Id,Patient_Name,Patient_Age,Patient_Gender,Patient_Diagnosis)

    elif choice =='2':
        main.display_patients()

    elif choice == '3':
        patient_id = int(input("Entet Your Patient ID : "))
        main.search_patient(patient_id)

    elif choice == '4':
        patient_id = int(input("Enter Your Patient ID : "))
        main.delete_patient(patient_id)
    
    elif choice == '5':
        patient_id = int(input("Enter Your Patinet ID : "))
        Patient_Diagnosiss = input("Enter Patient Diagnosis's : ")
        main.update_patient(patient_id,Patient_Diagnosiss)
    
    elif choice == '6':
        print(" Thank You... ")
        break

    else:
        print("Invalid option, Please try Again ")