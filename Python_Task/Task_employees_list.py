#Variable length arguments. 
#2. Write a program to enter employee details and also filter the stored employee  details  with name and empid and designation and email. 
Employees = {}
def add_employee():
    name = input("enter the employee name: ")
    empid = input("enter the employee id: ")
    email = input("enter the employee email id: ") 
    designation = input("enter the employee designation: ")
    Employees[name] = {'empid':empid, 'emailid':email, 'designation':designation}
    print("employee details added successfully")

def fliter_stored_employees_details():
    designation = input("enter fliter designation: ")
    found = False
    for key , value in Employees.items():
        if (value['designation'] == designation):
            print(key,value)
            found = True
    if not found:
        print("employees not found with this desgination")
        
            
no_of_employees = int(input("enter number of employees: "))
for i in range(no_of_employees):
    add_employee()
print(Employees) 


fliter_stored_employees_details()
