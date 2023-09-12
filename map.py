#map fn with lambda
num=[2,3,4,5,6]
sq=list(map(lambda x:x**2,num))
print(sq)

#map fn
l1=[2,3,4,5,6,7,8]
l2=list(map(lambda x:x+x,l1))
print(l2)

#map fn by taking two lists
l1=[2,3,4,5,6]
l2=[7,8,9,10,11]
l3=list(map(lambda x,y:x+y,l1,l2))
print(l3)

#map with lambda to get double of list
l1=[5,6,7,8,9,22,44]
lst=list(map(lambda x:x*2,l1))
print(lst)