# - Lists
# Lists are keep different elements separate comma place in square brakcet.
# Elements on that lists could have different types.
lista=[3,5,"tea",False]
print(lista)
print(type(lista))
#
# Lists allow to elements modification, we can replace elements on the list.
# Lists are indexed from "0" - that is mean that when we want to get first elements we need write "lista[0]".
# If we want to replace first element on lists we use "lista[0]=4"
#
# We can create lists in the lists:
listsinlist=[[3,5],"tea",[True, False],['coffe', 'coke']]
print(listsinlist)
print(type(listsinlist),
      type(listsinlist[0]))
#
# We can add position to the end of list:
listsin=listsinlist+["Adam",3] # Or we can change the inside value use in that case: listsinlist=listsinlist+...
print(listsin)
# or:
listsinlist.append(["Adam",3])# but when we use listsinlist.append("Adam",3) then we add singly value not a list of value
print(listsinlist)
#
# We can also add the all value of lists (not only lists) to the list:
Aba=[1,2,3,4,5]
bcb=[6,7,8,9]
Aba.extend(bcb)
print(Aba)
#
# And removing:
del(listsin[2])
print(listsin)
#
# Operating on the list when we want to copy values is not simple.
x=['a','b','c']
y=x
y[1]='z'
print(x) # It is show: a, z, c
# When we want to create really indepedens copy:
x=['a','b', 'c']
y=list(x)
y[1]='z'
print(x) # It show a,b,c. We can create a new copy:
y=x[:]
print(y)
#
# When we want to change something in the list we can use:
listsinlist[1]="coffemilk"
print(listsinlist)
# We can also:
listsinlist[1:3]="black coffe","modering place"
print(listsinlist)
#
#=====================================================================
#
# Function on the list
#
# max()
value=[1.71,1.82,1.72,2.01,1.54]
print(max(value))
# We can save this to the new variable and using later this:
maxvalue=max(value)
#
# round()
round(1.71,1)   # The result we have 1.7
round(1.71)     # The result is 2, because we do not specify a second parameter
# if we want to watch some help knowing then we use help(round)
#
#======================================================================
#
# Methods on the list
#---------------------------
# for example methods:
#
# float:
# bit_length()
# conjugate()
#----------------------------
# list:
fam=['liz', 1.73, 'emma', 1.68,'mom', 1.71, 'dad', 1.89]
fam.index("mom")    # result: 4
fam.index(1.73)     # result: 1 
fam.count(1.73)     # result: 1 # because 1.73 occurs is once
#
# we can use .index()to show place where is a value from one place to another place
num=[1,2,3,4,1,2,3,4,1,3,4,2,1,2]
num.index(3,4,7) # result: 6
#
#======================================================================
#
# Package:
#
# When we want to using some package then we need to execute command import:
import numpy
# When we want using the function from numpy:
print(numpy.array([1,2,3]))
# But we can import library as another variable:
import numpy as np
print(np.array([1,2,3]))
# And a 3th way to import, import a specific function
from numpy import array
print(array([1,2,3]))
print(array(fam))
