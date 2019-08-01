# -*- coding: utf-8 -*-

#Formating Subtitles

# We have two standard type to formating subtitles:
# The first is the old formatting used by python 2.0+
# The secound and last is new formatting used by python 3.0+
#
# In the old formatting we use sign "%" inside sentence in place where we want put the argument and outside of sentence where we need to define the argument.
# We cannot use "%" alone, we need use it with correctly type like "%s", "%f" etc.
#
# In the new formatting we use "{}" insted %. We can put "{}" alone or with type inside like "{:f}, {:s} etc.
#
# Type of subtitles:
# s - string - inscription
# d - digit - 
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
