# -*- coding: utf-8 -*-
#
# Types and Variables
#
# ----------------------------------
# Types:
#
# -Numbers
# -String
# -Bool (logical type)
# -List
# -Tuple (krotka in polish)
# -Dictionary
#
#
# Numbers
#
# -int   - integer (l. całkowita in polish)
# -float - floating point number (l. zmiennoprzecinkowa in polish)
#
# For example, int is number "4" but "4.4" is number with point.
#
# Curious thing is the number to exponentiation like 62.3E+6, it is mean 62.3*10^6.
#
# When we want to check the type given value, we can use simple command:
print(type(4))
print(type(4.4))
print(type(4.4E+6))
print(type(4E+10))
#
# Type int can contain a infinite number of integer numbers.
#
#
# Strings
#
# - single quote mark
#   We can write sentense in single quote mark e.g. 'Hello world'.
#
# - double quote mark
#   The same situation like in single quote mark e.g. "Hello world".
#
# - triple quote mark
#   When you want to put multi-line text then you need to use ''' or """.
#   Inside a triple quote you can use single and double quoite.
quote='''This is milti-line text
which have quote
"Always code as if the guy who ends up maintaining your code will be a
violent psychopath who knows where you live"
-John Wood'''
print(quote)
#
# - Strings are be immutability
#   It is mean, after create text you can not modify it directly.
#
# - Strings Formatting
#   A lot of things is in lesson 3, but we could show one nuance.
#   Command "print" have dissapear sign "\n". We can delate this:
print('diss',end='')
print('apear')
#   We can add "blank sign" on between.
print('diss', end=' ')
print('apear', end='')
#
# For this elemets we have few command to print:
# end - is using the sign on the last place in print
# sep - separate is command usind the sign between a value.
# file - it is make print something in a new file
print('This is important message', file=open('important.txt', 'w'))
#
# - Strings can be raw
#   We can write text without special sign, we need to this raw sign befor text.
txt=r"We use \n to create a new line and \t to create tab."
print(txt)
#
#
# Logical Type - Bool
#
# Logical value - True/False are keep in logical type - bool.
print(type(True))
print(type(False))
#
#
# Lists and Tuples
#
# Lists and tuples are complex data types.
#
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
# - Tuples
# Tuples are unchenged lists. We can not modify the elements contained in the tuple.
# Tuple is like string it is immutability. Tuples use round brackets.
krotka=(3,5,"coffe",True)
print(krotka)
print(type(krotka))
#
# We can show element in tuple according to their index "krotka[2]" but we can not possibility to directly modification "krotka[2]=12" - we get error!
#
#
# Dictionary
#
# Dictionary is very useful data types. In different programming language appears as "hash table", "associative table", "hash map".
# It stores data in pairs as "key : value", of which the key must be of the immutability type and unique within the dictionary (the key cannot be repeated!)
#
# For example:
lexicon={"coffe":"black","tea":"green","sugar cube":5,0:"zero"}
print(lexicon["tea"])
print(lexicon[0])
lexicon[1]="one"
print(lexicon)
lexicon={"coffe":"black","tea":"green","sugar cube":5,0:"zero",1:"one"}
print(type(lexicon))
#
# Dictionary is disordered structure therefore we cannot call dictionary elements by index.
# If there is a key with the calue "0", we get the dictionary value as in the example before, which in element in the dictionary pair 0:"zero".
#
# Good to know if we try assigne value to thosen't exist key then automaticly add key with that value.
#
print(lexicon.keys())
print(lexicon.values())
print("tea" in lexicon)
print(list(lexicon.keys()))
print(type(list(lexicon.keys())))
#
# ---------------------------------
# Variables
#
# Some value is need sometimes to use later, that's way we want to store somewhere.
# So far we use variable data but we need to name it and systematize.
# name='Ada Lovelace"
# name is name of variables
# 'Ada Lovelace' is value of variables
#
# Variable is this what the exactly that is mean - is value could be changed.
# This is programistic construct and this used for storege data.
# Variable data is store in computer memory and when we want to get this value we need use the key for call.
#
# How properly named variable data in Python?
#
# Variable data need to identify. How? Simply, by name.
# This is few rules to named variable data:
#
# - first sign must be letter from alphabet, small or large letter (ASCII or Unicode - that is mean, you can use polish letter but this is not recommended).
#   or underscore "_".
#
# - The rest could be assembled of letter, underscore and numbers (0-9)
# - the variable names are "case-sensitive" - important thing is the size of letter is metter.
#   That's way "myvariable","myVariable" and "MyVariable" is 3 different name.
#
# The variable thosen't exist without value. The Value have a type.
my_variable=5
type(my_variable)
print(my_variable)
#
# The curious thing, we can imput value to few variable in one line.
varA, varB, varC=4,14,"coffe"
print(varA,varC,varB)
#
# ---------------------------------
# Comment
#
# We can use "#" to comment the line and use ''' to comment in multiline.
my_name="maks" # Variable store my name
my_age=31# Variable store my age
'''This is
multiline comment.
This is great'''

