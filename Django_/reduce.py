#reduce Function to add
from functools import reduce
l1=[2,3,4,5,6,7,8,9,10]
l2=(reduce(lambda x,y:x+y,l1))
print(l2)

from functools import *
list1 = [1,2,3,4,5,6,11,32]
list2 = (reduce(lambda x,y:x*y,list1))
print(list2)

#reduce fn with 3 parameters:
from functools import reduce
l1=(7,8,9,10,14)
print(reduce(lambda y,z:y+z,l1,4))