# While Loop
#
# Long story short - WHILE loop make loop until one specifi condition is execute.
#
#
# Making loop in Python
#
# Let's remember:
#
# name=input("What is your name?")
# print("Hi", name)
# name=input("What is your name?")
# print("Hi", name)
# name=input("What is your name?")
# print("Hi", name)
#
# It is the same:
#
# for user in range(0,3):
#    name=input("What is your name?")
#    print("Hi", name)
#
# And in WHILE:
#
# couunter=0
# while counter != 3:
#    name=input("What is your name?")
#    print("Hi", name)
#    counter +=1
#
# WHILE loop is working by grow us "counter" for one step and ending to "2" (becouse is starting from "0")
#
# Check this to add to show numeric value in next to next iteration:
#
# counter=0
# while counter != 3
# name(input(str(counter)+". What is your name?")
# print("Hi", name)
# counter +=1
#
# result:
#
# 0. What is your name? Maria
# Hi Maria
# 1. What is your name? Adam
# Hi Adam
# 2. What is your name? Kar
# Hi Kar
#
#
# WHILE loop in Python
#
# We met for and while loops in Python.
# In another language e.g. C++ we have: DO WHILE, in Python DO WHILE doesn't occur.
#
# WHILE is starting instruction block which is execute as long as condision is fulfilled.
#
# After the loop execute condition is checked and if condition is a true, code in block is execute. If condition is false - code inside a block isn't execute. Iterpreter go forward.
#
# a=5
# while a>4:
#    a=int(input("Give a number bigger than 4: "))
#    print("Gives a number a=",a)
# print("Your number isn't biggest than 4")
#
# Assumed if we want buy a book but then when it price is fall under 30 PLN. Python is help us with this, a speciality decreasing loop - book price.
#
book = 59
while book > 30:
    print("We wait to discount")
    book = book*0.8
    print("Discount 20%, actualy price: ",round(book,2), "PLN")
    print("------------------------")
print("\nI go to bookstore!")
#
#
# Python - Infinite loop
#
# If Condition will be always fulfilled then loop execute to the infinite time.
# This is why instruction WHILE True instruction is infinite loop.
#
# while True:
#    print("Hello World!")
#
# Conditional instruction 1 performs the same function, since one is True for Python.
#
# while 1:
#    print(bool(1))
#
# bool() is function which we use when we want to change number value to boolean value.
print(bool(1))
print(bool(0))
#
#======================
# while user_id <100            # Condition to be execute
#    special_promo()            # Instruction execute inside a loop
#    send_email(user)           # Instruction execute inside a loop
# print("Finished!")            # This part of code is outside a loop and is execute once
#=======================
#
# WHILE loop have:
# - word while
# - condition
# - block of code which be execute in loop
#
#
# break/continue instruction
#
# Sometimes we want end of actually integration or all prevoius loop - without next check condtition.
# Python allowe for as two instruction: break and continue that are responsible for immedietely aborting the current iteration.
# 
# - break - end working loop. Interpreter come to next part of instruction - following the loop block.
# - continue - end current loop iteration. Interpreter return to loop begining and condition is check again to define if loop will execute again or ended this and go forward.
#
#
# Break instruction:
#
# Loop starts
#       |
#       |
#      \ /         False
# ---> Condition? ---
# |     |           |
# |     | True      |
# |    \ /     Yes  |
# |   break ---------
# |     |           |
# |     | No        |
# |    \ /         \ /
# ---- We stay     Loop is ending
#       in loop
#
#
num=10
while num<20:
    num +=1
    if num == 15:
        break
    print("Actually number is", num)
print("I am out of loop")
#
# Show a value : 10,11,12,13,14 and in 15th break instruction is working and go out of loop.
#
# The same result but using a for instruction:
for num in range(10,20):
    if num == 15:
        break
    print("Actually number is", num)
print("I am out of loop")
#
#
# Continue instruction
#
# Loop starts
#       |
#       |
#      \ /         False
# ---> Condition? ---
# |     |           |
# |     | True      |
# | Yes\ /          |
# ---- continue     |
# |     |           |
# |     | No        |
# |    \ /         \ /
# ---- We stay     Loop is ending
#       in loop
#
#
num=10
while num <20:
    num += 1
    if num == 15:
        continue
    print("Actually number is", num)
print("I am out of loop")
#
# In this case, script show value from 11 to 20 without 15.
