#Multiple inheritance
class parent_1:
    def mother_name(self):
        print("Mother Name: Mallika")

class Parent_2:
    def father_name(self):
        print("Father Name: Prabath kumar")

class Child(parent_1,Parent_2):
    def display(self):
        self.mother_name()
        self.father_name()
        print("Child Name: Chandrika")

C = Child()
C.display()