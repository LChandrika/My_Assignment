class Company_1:
    def google(self):
        print("google search....... ")

class Company_2(Company_1):
    def marolix(self):
        self.google()
        print('HRMS Marolix')
    
class Company_3(Company_2):
    def employee(self):
        self.marolix()
        print("Lakshmi Chandrika" )

e=Company_3()
e.employee()