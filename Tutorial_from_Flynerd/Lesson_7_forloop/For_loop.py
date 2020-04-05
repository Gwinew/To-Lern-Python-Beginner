# "FOR" loop
#
# We know variable, we can take data from user, show results and also perform diffrent instructions depends from conditions but we miss something in us program.
# The loop function - it is take something function to repeat.
#
# FOR loop
#
# Syntax which is in all programs language.
#
# We assume that we want ask 3 users for name and say hello to each other by name. We can do that:
#===============================
# name=input("What is your name?")
# print("Hi", name)
# name=input("What is your name?")
# print("Hi", name)
# name=input("What is your name?")
# print("Hi", name)
# ==============================
# But the better looks is:
# for user in range(0,3):
#   name=input("What is your name?")
#   print("Hi", name)
#
# We can call everyone in sequence and copy the same code but we not must.
# Problem is show when users grow to a big number.
#
# for user in range(0,50)
#
#
# range(start, stop, step)
#
# We can use range() function for 3 way:
# - The most basic way is range(0, end) - create sequence from "0" to apply number. We can write is short as range(5) - that is mean that start and step take default value start=0, step=1.
# - Giving start, we can decide from what index Python is starting loop e.g. range(3,10) - range(start, end) allows define start and ending range.
# - But range in full write is range(start, end, step) - step is parameters to define what steps it is calculate.
#
# Create sequence never have end od range!
# This is mean that range(0,5) we read: "Generate range from "0" to "5" but don't work on "5".
#
for i in range(0, 5):
    print("value: ", i)
#
# This code show: 0,1,2,3,4 (show 5 digit from 0 but doesn't value 5).
# We can start from in middle:
for i in range(2,5):
    print("step:",i)

# And
for i in range(0,10,2):
    print("step:",i)
#
# range() function is a list in fact. range() function doesn;t create new list but return range - separately type in Python.
# Range make sequence elements one by one i the same time and it is way to don't keep the full data in memory.
a=range(10)
print(a)
#
#
# Iterating through the list
#
# We can use range() function to operate on data in lists.
names=["Ania","Kasia","Jan","Piotr","Pawel"]
for i in range(5):
    print("Hi", names[i])
# But it is cleary to read:
for name in names:
    print("Hi", name)
#
# What different in this two option?
#
# Solution to enter to elements in list.
# First example using the fact that every elements have index in the list (from "0" to the correctly number).
# The secound example use directly response from all name in list.
#
#===================================
# To summary:
# for user in list_of_users:    # "user" is name of variable which control loop; "list_of_users" is a range where we are iterating
#    log_in()                   # This instruction inside the loop
#    welcome(user)              # This instruction inside the loop
# print("Finished")             # This part of code is outside from loop and execute one time
#===================================
#
# FOR loop have:
# - key word: for
# - variable name
# - in
# - value which we will interating
# - part of code inside a loop
#
# We can use FOR loop for tuples, iterator, string or dictionary.
#
# Iterating in tuple:
for i in (1,2,3,4):
    print("step:",i)
#
# Iterating in string:
for i in "ala have a cat":
    print("step:",i)
#
# Iterating in dictionary:
name={"Adam":"Malware","Agnes":"Sign","Jon":4}
for i in name:
    print("krok:", i)
#
#
# Loop in loop
#
# Triangle:
# print("#")
# print("##")
# print("###")
# print("####")
# print("#####")
#
# Whith FOR instruction:
for i in range(1,6):
    print(i*"#")
#
# We want to build 3 traingle - create a christmas tree:
#for i in range(3):
#    print("#")
#    print("##")
#    print("###")
#    print("####")
#    print("#####")
#
# Or using FOR:
for i in range(3):
    for j in range(1,6):
        print(j*"#")
#
