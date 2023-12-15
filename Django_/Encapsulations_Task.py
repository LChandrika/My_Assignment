#Encapsulation with Public

class Employee:
    def __init__(self,name,domain):
        self.name = name
        self.domain = domain

    def m1(self):
        print("my name is ",self.name)
        print("I am working as ",self.domain," Developer")

e = Employee("Chandrika","python")
e.m1()

#Encapsulation with Protected

class Employee:
    def __init__(self,name,domain):
        self.name = name
        self.domain = domain

    def _m1(self):
        print("my name is ",self.name)
        print("I am working as ",self.domain," Developer")
    

e = Employee("Lucky","Java")
e._m1()

        

#Encapsulation with Privte

class Library:
    def __init__(self):
        self.Book_name = "Wings of fly"
        self.author = "A.P.J.Abdul kalam"

    def __m1(self):
        print("I am reading a Book ",self.Book_name)
        print("Author of the book is ", self.author)

    def m2(self):
        self.__m1()    


L = Library()
L.m2()

        