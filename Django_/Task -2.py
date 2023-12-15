#write a python program that allows you to add an employee with domain, name, empid, and email details using user input and then print the employee's details.
employees = {}
def add_employees():
    name = input("enter the employee name : ")
    domian = input("enter the domain : ")
    employee_ID = input("enter the employee_ID : ")
    email_id = input("enter the email_id : ")
    employees[name] = {"domain":domian,"employee_ID":employee_ID,"email_id":email_id}
    print("Employee details added successfully!")

def get_employee_details_by_compare_with_domain():  
    domain = input("enter the domain to compare: ") 
    found = False
    for key,value in employees.items():
        if(value["domain"]== domain):
            print(f"{key}: {value}")  
            found = True
    if not found:
        print("no employees are found with this domain")

def remove_the_particular_employee():
    name_to_remove = input("enter the name of the employee we need to remove: ")
    if (name_to_remove in employees):
        del employees[name_to_remove]
        print(f"{name_to_remove} is removed from the employees list.")
    else:
        print(f"Not found with the employee name of {name_to_remove}.")

No_of_employees = int(input("Enter the Number of Employees: "))
for i in range (No_of_employees):
    add_employees()
    
print(employees)
get_employee_details_by_compare_with_domain()   
remove_the_particular_employee()
    


