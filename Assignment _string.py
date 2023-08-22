#Using membership operator (in)
s1 = "hello python"
s2 = "python"
print(s2 in s1)

#Using membership operator (not in)
a1 = "hello python"
a2 = "python"
print(a1 not in a2)

#Removing spaces from a string
s = "My name is Chandrika"
print(s.replace(" ",""))

#Comparing two strings
string_1 = "PYTHON"
string_2 = "Java"
string_3 = "python"
print(string_1 == string_2)
print(string_1 == string_3.upper())
print(string_1 == string_3)

#Finding sub-string in main string
main_string = "python is a popular language"
sub_string = "popular"
print(sub_string in main_string)

#find sub-string index
main_string_1 = "python is a popular language"
sub_string_1 = "popular"
print(main_string_1.find(sub_string_1))

#using Replace function
word = "I Love Python"
print(word.replace("Love Python","Hate Java"))

#using split function
word_1 = "My 2nd Assignment"
print(word_1.split())

#using join function
z = "python has huge libraries"
print("-".join(z.split()))




