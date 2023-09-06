#1.Write a Python script to add a key to a dictionary.
dictionary = {'0': 10, '1': 20}
dictionary['2'] = 30
print(dictionary)

#2.Write a Python script to check whether a given key already exists in a dictionary.
dic = {"Fruit":"apple", "cars":"Audi"}
b = "car"
if b in dic.keys():
    print("This key already exists in a dictionary")
else: 
    print("This key is not exists in a dictionary")

#3.Write a Python program to iterate over dictionaries using for loops.
dic = {"Fruit":"apple", "cars":"Audi","Brand":"Puma"}  
for key,value in dic.items():
    print(key,value)
    
#4.Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.
N = 16
d = dict()
for i in range(1,N):
    d[i] = i * i
print(d)   

#5.Write a Python program to create a dictionary from a string.
string = "marolix technology"
cnt_characters = {}
for i in string:
    if i in cnt_characters:
        cnt_characters[i] += 1
    else:
        cnt_characters[i] = 1
print(cnt_characters)

#6. Write a Python program to sum all the items in a dictionary.
d1 = {'a': 100, 'b': 200, 'c':300}
l =[]
for i in d1:
    l.append(d1[i])
print(sum(l))    


#7.Write a Python program to combine two dictionary by adding values for common keys.
d1 = {'a': 100, 'b': 200, 'c':300}  
d2 = {'a': 300, 'b': 200, 'd':400}  
new_dict = d2
for i, j in d1.items():  
    if i in d2:  
        new_dict[i] = j + d2[i]  
    else:   
        new_dict[i] = j  
print(new_dict)

#8.Write a Python program to access dictionary key's element by index.
dictionary = {'0': "Physics", '1': "Math",'2' : "Chemistry"}
for i in dictionary.keys():
    print(dictionary[i])

#9.Write a Python program to remove a key from a dictionary.
dic = {"Fruit":"apple", "cars":"Audi","Brand":"Puma"}  
del dic["Brand"]
print(dic)


#10.Write a Python script to merge two Python dictionaries.d
d1 = {'a': 100, 'b': 200, 'c':300}  
d2 = {'d': 300, 'e': 400, 'f':500} 
d1.update(d2)
print(d1)