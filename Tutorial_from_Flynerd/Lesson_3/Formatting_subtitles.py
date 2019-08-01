# -*- coding: utf-8 -*-

#Formating Subtitles

# We have two standard type to formating subtitles:
# The first is the old formatting used by python 2.0+
# The secound and last is new formatting used by python 3.0+
#
# 
# We have some few way to formating floating record:
# %f. ; {:f} ; round(x,y) - when x is argument and y is number of digits after the decimal point
# for example (for x=2/3):
x=4.0/3.0
print(x)
print("x is: %f." % (x))
print("x is {:f}" .format(x) )
print("x is", round(x,6))

# 
