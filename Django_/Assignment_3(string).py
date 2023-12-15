#1 Write a python program to remove a given  character from string.
S=input ("Enter string")
Character=input ("Enter Character")
print(S.replace(Character,""))

#2  Write a program to check String is Palindrome or not.
string = input("Enter  String : ")
string1 = " "
for i in string:
    string1= i+string1
if(string == string1):
    print("string is palindrome")
else:
    print("string is not a palindrome")

# 3.Write a python program to check given character is vowel or consonant.
vowels= ['A','E','I','O','U','a','e','i','o','u']
a = input("Enter a value: ")
if a in vowels:
    print( a," is vowel")
else:
    print(a," is consonant")

# 4.Write a python program to replace string space with given character in Python.  
a = input("Enter String : ")
c = input("Enter  Character : ")
print(p.replace(" ",c)) 


# 5.Write a python program to count alphabets, digits, and special characters in the string.
String= input("Enter String : ")
alphabets = 0
digits =0 
special_charcters = 0
for i in range(len(String))
    if(String_1[i].isalpha()):
        alphabets = alphabets +1
    elif(String_1[i].isdigit()):
        digits = digits +1
    else:
        special_charcters = special_charcters +1
print(" Alphabets : ",alphabets)
print("Digits : ",digits)
print("Special Characters : ",special_charcters)

# 6.Write a python program to remove all the blank spaces in a given string.
string = input("Enter string : ")
print(string.replace(" ",""))


#7.Write a python program to find sum of integers in the string.
string = input("enter string : ")
sum = 0
for i in string:
    if(i.isdigit()):
        sum = sum + int(i)
print(sum)

#8.Write a python program to Remove Repeated Character from String
s = input("Enter String : ")
e = ""
for i in s:
    if i not in e:
        e= e + i
print(e)

#9.Write a python program to count occurrence of given character in string. 
a = input("Enter string : ")
Character = input("enter character : ")
count = 0
for i in a:
    if(i == Character):
        count = count + 1
print(count)        

#10.Write a python program to check string is anagrams or not in Python.
 str1 = ("Enter string 1 : ")
 str2 = ("Enter string 2:  ")
count = 0
for i in str1:
    for j in str2:
        if i==j:
            count=count+1
if count==len(a):
    print("string are anagram")
else:
    print("string are not anagram")                