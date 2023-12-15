# 1.write a python program to merge two lists.
L1 = eval(input("Enter L1"))
L2 = eval(input("Enter L2"))
L3 = L1 + L2
print(L3)

#2.write a python program to find the sum of list elements.
A1 = eval(input("Enter A1:"))  
a = 0
for i in A1:
    a = a+i
print(a) 

#3.write a python program to print even and odd numbers seperatly in list.
P1 = list(map(int,input("\nEnter P1:").split()))
odd = []
even = []
for i in P1:
    if i % 2 != 0:
        odd.append(i)
    else:
        even.append(i)
print(odd)
print(even)

#4.write a python program to delete element of given index in list.
B1 = list(map(int,input("\nEnter B1:").split()))
B1.pop(2)
print(B1)

#5.write a python program to delete given elemet from the list 
C1 = list(map(int,input("\nEnter C1:").split()))
C1.remove(3)
print(C1)

#6.write a python program to insert an elemet at given index location.
D1 = list(map(int,input("\nEnter D1:").split()))
D1.insert(2,10)
print(D1)

#7.write a python program to check the sizes of given two lists are same.
R1 = list(map(str,input("\nEnter R1:").split()))
R2 = list(map(str,input("\nEnter R2:").split()))
if len(R1) == len(R2):
    print("true")
else:
    print("false") 


#8.Write a Python function that takes two lists and returns True if they have at least one common member.
s1 = list(map(str,input("\nEnter s1:").split()))
s2 = list(map(str,input("\nEnter s2:").split()))
for i in s1:
    if i in s2:
        print("true")



#9.Write a Python program to remove a specified column from a given nested list.
m = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
main_list = []
for i in range(0,len(m)):
    result = []
    for j in range(1,len(m)):
        result.append(m[i][j])
    main_list.append(result)
print(main_list)

#10. Write a Python program to convert a list of multiple integers into a single integer.
list1 = list(map(int,input("\nEnter list1:").split()))
s = ""
for i in list1:
    s=s+str(i)
print(int(s))


#11.Write a Python program to remove duplicates from a list.
lst = list(map(int,input("\nEnter lst:").split()))
res = []
for i in lst:
    if i not in res:
        res.append(i)
print(res)        

