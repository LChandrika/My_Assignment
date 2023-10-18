class Vehicle:
    def name(self):
        print("Vehicle Type: ")

class Vehicle_type(Vehicle):
    def display(self):
        print("four wheeler")
        
e = Vehicle_type()
e.name()
e.display()
