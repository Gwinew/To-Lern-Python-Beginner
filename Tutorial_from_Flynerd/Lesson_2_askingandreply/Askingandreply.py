# Ask and Reply AND how to run Python in CMD
#____
#If it doesn't work automatically, add the python option manually:
#   Open computer preferences
#   Open Advanced system setting
#   Open in Advanced Enviroment Variables...
#   Find Path and open this
#   Copy python destination path and add (use ' after the last path) path
#   OK OK OK and this is work
#Use 'python' to run Python on CMD or PowerShell or...
#
#Type "help()" for interactive help or "help(object)"for help about object (e.g. help(print)).
#Type "quit()" for quit from python in the console.
#____
#If you want run the script from command console you must using 'python' before path to file:
#>>> python C:\User\...\python.py
#or
#>>> python .\...\python.py
#or
#You must be in current folder where the file is in inside
#python python.py
#____
#The "input()" function is used to save data to an argument. After entering it itself, we get value entered immediately after this command.
#Remember, "input()" is a sting.
#
#for egxample:
#>>>
#input()
#Something               ##You fill this line
#'Something'             ##You get this value
#<<<
#
#You can as it was said before, take this function and save as like argument.
#
#for example:
#>>>
#Tea=input()
#Earl grey               ##This is like Tea='Earl grey'
#<<<
#
#And using this for another function:
#
#print('The best Tea is', Tea)
Tea=input('Put in your favorite tea - ')
print('The best Tea is', Tea)
#
#Remember: You can overwrite "Tea".
#
#____________
#
#Unfortunately 'int' isn't works with 'str'('input()' is a string). You must converter 'str' to 'int'(or another number type e.g. 'float') if you want working with numbers.
#Only need to using 'int()'. For example:

Number=input('Enter a number - ')
print(int(Number)+3)

#You can also use:

Number=input('Enter a number2 - ')
Number=int(Number)       ##In this case we are using the last argument to save to a new argument
print(Number+3)

#Or treat it as a number immediately using:

Number=int(input('Enter a number3 - '))
print(Number+3)


# -*- coding: utf-8 -*-
#This is to code with polish symbols like ą, ę, ć etc.



