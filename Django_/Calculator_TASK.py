class Calculator:
    def _init_(self):
        print("*MY CALCULATOR*")
        self.operations()
    
    def operations(self):
        print(''' Select Which operations do you need
        1.Addition
        2.Subtarction
        3.Multipliaction
        4.Divison
Press 1 for Add , 2 for sub, 3 for Mul, 4 for Div''')
        
        n = int(input("\nEnter the value:"))
        self.numbers = list(map(int,input("\nEnter number of values:").split()))
        if(n == 1):
            self.add(self.numbers)
        elif(n == 2):
            self.sub(self.numbers)
        elif(n == 3):
            self.mul(self.numbers)
        elif(n == 4):
            self.div(self.numbers)    
        else:
            print("PLEASE CHOOSE OPTIONS")
            self.operations()   

    def add(self,numbers):
        print(f'Sum of numbers is {sum(numbers)}')
        

    def sub(self,numbers):
        result = self.numbers[0]
        for i in self.numbers[1:]:
           result -= i  
        print(f'Subtraction of numbers is {result}')
           

    def mul(self,numbers):
        result = 1
        for i in self.numbers[0:]:
            result *= i 
        print(f'Multipliaction of numbers is {result}') 
         

    def div(self,numbers):
        result = self.numbers[0]
        for i in self.numbers[1:]:
           result /= i  
        print(f'Division of numbers is {result}')
                 
              
c = Calculator()
print("Thanks for using my calculator")