# Conditional Statements
#
# Conditional Statements (Control Statements) are one of basic rule in evry program language. It is working exactly as name sugest - instruction or instrucktion block working only when specify condition (or set conditions) is complete.
# 
#
# Checking condition
#
# We start from somthing obvious for us and also obvious for computer - comparison.
#
# Comparison True or False?
#
print("0<1 is {}".format(0<1))
print(0>1)
print(0<=1)
print(1==0)
print(1==1)
print(1!=0)
print(1!=1)
#
# Greater-than sign, less-than sign is obvious for sure. If we want to comparison two value we need to use ==. != is we check statement "this not equal". 1 isn't 0 - that is way to be true.
#
# Boolean operator
#
# and - it is mean that two value is must be true
# or - it is mean that one from two value must be true
#
x=10
print(x<10)
print(x>1 and x<13)
print(x<1 and x<13)
print(x>1 or x<13)
print(x !=10 or x>13)
print(x>1 and x<13 or x != 10)
#
#
print(x>1 and (x<13 or x !=10))
print((x>1 and x<13) and x!=10)
#
# This is not all comparison which return True and False.
#
x=10
print(x is 10)
print(x is not 13)
print(x is '10')    # Becouse '10' is string
print(x in [1,12,10])
print(x in [1,12,'txt'])
print(x not in [1,12,'txt'])
print('str' is 'str')
print('str' is 'string')
print('str' in 'string')
#
# is - check if two value is identical
# in - chek if variable is include in another object
# not - add negation
#
#
# Is 'is' the same as '=='?
#
# 'aa' == 'aa' True
# 'aa' is 'aa' True
#
# 'aa' == 'a'*2 True
# 'aa' is 'a'*2 True
#
# x='a'
# 'aa' == x*2 True
# 'aa' is x*2 False ????
x='a'
print('aa' == x*2)
print('aa' is x*2)
# It is false becouse 'a'*2 is a new string 'aa' but if we use the variable 'x' than we don't know the value will be the same - 'x' is different data another data base.
# But this is work in small digit:
x=10
print(x is 10)
# But thid is didn't work in big number:
print(1000 == 10**3)
print(1000 is 10**3) # True but when we use x=10 than we have false
print(1000 is x**3)
#
# It is one more thing, numerical values can expressed as a a logical value True False.
# It is assumed that True is 1, False is 0.
#
#
# "if" instructions
#
# Control statement is used to check if the given condition expression is true.
# Depence from condition expression is true or not that start directly part od code.
#
# An example block diagram:
#=========================================
# Is the condition fulfilled? -> No
#           |                    |
#          \ /                  \ /
#           Yes                 Command 3
#           |                   Command 4
#          \ /                   |
#           Command 1            |
#           Command 2            |
#           |                    |
#           |<--------------------
#          \ /
#==========================================
# if ( condition ):
#    command1
#    command2
# else:
#    command3
#    command4
#
# Instruction "if (condition):" delivers information from interpreter and means "if"...
# if (condition) - if condition is true, execute command 1 and command 2, otherwise execute command 3 and command 4.
#
# Look at a space before command - it is tab (or 4 multiply "space")
#
#
# In script: adult.py
#=================
# print('How old are You?')
# age = int(input())
#
# if(age>=18):
#   print("You are adult")
# else:
#   print("You have a bit of legal age\nExactly you have {} years to be adult".format(18-age))
#==================
# 
#
# Conditional statement: if...elif...else
#
# What if we want add a condition?
# We can use next "if" or we use "elif" (else if).
#
# To the previous code add:
# if (age>100)
#    print("This is realy your age?")
#
# next change "if" if to "elif":
# elif(age>100):
#    print("This is really your age?")
#
# Script adult_if.py
#=====================
# age = int(input('How old are You?'))
#
# if(age>100):
#    print("This is realy your age?")
# if(age>=18):
#   print("You are adult")
# else:
#   print("You have a bit of legal age\nExactly you have {} years to be adult".format(18-age))
#==================
#
# Script adult_elif.py
#======================
# age = int(input('How old are You?'))
#
# if(age>100):
#    print("This is realy your age?")
# elif(age>=18):
#   print("You are adult")
# else:
#   print("You have a bit of legal age\nExactly you have {} years to be adult".format(18-age))
#==================
#
# You can see that next 'if' checked condition everytime but elif - code it executed  when 'if' is false and 'elif' is true.
#
# We can change the condition and using boolean operator AND:
#====================================
# age = int(input('How old are You?'))
#
# if(age>=18 and age < 100):
#   print("You are adult")
# else:
#   print("Age wrong")
#====================================
# We can create simple visual code:
#====================================
# age = int(input('How old are You?'))
#
# if(18<= age < 100):
#   print("You are adult")
# else:
#   print("Age wrong")
#======================
#
# We can also create expanded code:
#==================================
# age=int(input("How old are You?"))
# responsible=input("Do You be responsible?" Y/N")
#
# if age>100:
#    print("This is really your age?")
# elif age >=18 and responsible =="Y":
#    print(" You are adult")
# elif responsible !="Y":
#    print("Work on responsibility")
# else:
#    print("You have a bit of legal age")
