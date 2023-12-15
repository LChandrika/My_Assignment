class Atm:
    def __init__(self):
        self.pin=""
        self.balance= 1000
        self.menu()
        
    def menu(self):
        while True:
            print("CREATE PIN    Enter- 1:")
            print("DEPOSIT       Enter- 2:")
            print("WITHDRAW      Enter- 3:")
            print("CHECK BALANCE Enter- 4:")
            print("EXIT PROGRAM  Enter- 5:")
            user_input=int(input("CHOOSE ONE (1/2/3/4/5): "))
            if (user_input == 1):
                self.create_pin()
            elif(user_input == 2):
                self.deposit()
            elif(user_input == 3):
                self.withdraw()
            elif(user_input == 4):
                self.check_balance()
        
            else:
                print("Thank you for banking with us.")
                break
    def create_pin(self):
        self.pin=input("Enter your pin: ")
        if(len(self.pin) == 4): 
            print("pin set successfully")  
        else:
            print("Please Enter valid 4 digit pin number")
            self.create_pin()

    def deposit(self):
        temp=input("Enter your pin: ")
        if temp==self.pin:
            amount=int(input("Enter amount to deposit: "))
            self.balance=self.balance+amount
            print("Deposit Successfully")
            print("The Total Balance after the deposit:",self.balance)
        else:
            print("Invalid Pin")

    def withdraw(self):
        temp=input("Enter your pin: ")
        if temp==self.pin:
            amount=int(input("Enter amount to withdraw: "))
            if amount<self.balance:
                self.balance=self.balance-amount
                print("Succesfully Withdraw")
                print("The Total Balance after the Withdraw:",self.balance)
            else:
                print("Insufficient Balance")
        else:
            print("Invalid Pin") 

    def check_balance(self):
        temp=input("Enter your pin: ")
        if temp==self.pin:
            print("The current balance is",self.balance)
        else:
            print("Invalid Pin")             
            

Atm()
                         