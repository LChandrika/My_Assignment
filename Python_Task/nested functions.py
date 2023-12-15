#nested functions for multiplication
def multi1(x):
    def multi2(y):
        def multi3(z):
            return x*y*z
        return multi3
    return multi2
result=multi1(6)(7)(8)
print(result)

#nested functions for addition of two numbers
def num1(x):
    def num2(y):
        return x+y
    return num2
print(num1(10)(5))


#nested functions to print strings
def greeting(first,last):
    def name():
        return first+" "+last
    print("Hello"+" "+name()+" "+"!")
greeting('lucky','Chandu')



 


