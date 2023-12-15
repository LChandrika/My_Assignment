#filter fn to print only vowels
def vowels_list(variable):
    vowels=['a','e','i','o','u']
    if variable in vowels:
        return True
    else:
        return False
l =['a','b','c','d','e','f','g','h']
filtered=filter(vowels_list,l)
print('the filtered letters are:')
for s in filtered:
    print(s)

#filter fn to list where each element is greater than or equal to 70
scores=[50,40,30,20,10]
filtered=[]
for score in scores:
    if score>=30:
        filtered.append(score)
print(filtered)

#using lamda
scores=[50,40,30,20,10]
filtered=list(filter(lambda score:score>=20,scores))
print(filtered)

#to check if number is multiple of 3
def multiple_of(num):
    return num%3==0
numbers=[1,2,3,4,5,6,7,8,9,10,]
result=list(filter(lambda x:multiple_of(x),numbers))
print(result)

#lambda function examples
#sqaure of given no using  lambda function
s=lambda n:n*n
n=int(input("enter a number"))
print(s(n))

#write a lambda to find biggest of 2 numbers
s=lambda x,y:x
 if x>y else y
x=int(input("enter a number"))
y=int(input("enter a number"))
print("the biggest no is ",s(x,y))

#write lambda to find sum of two numbers
s=lambda x,y:x+y
x=int(input("enter a number"))
y=int(input("enter a number"))
print(s(x,y))

#recursive of factorial of a number
def recur_fact(n, a = 1):
    if (n == 0):
        return a
    return recur_fact(n = 1, n * a)
print(recur_fact(4))


#set a number to a power using recursive function
def power(num,topwr):
        if topwr==0:
            return 1
        else:
            return num*power(num,topwr-1)
        print('{} to the power of {}'.format(4,7,power(4,7)))

 #fibonacci series using recursive functions
def fibonacci(n):
     if n<=1:
          return n
     else:
          return fibonacci(n-1)+fibonacci(n-2)
number=14
print("fibonacci series")
for i in range(number):
     print(fibonacci(i))