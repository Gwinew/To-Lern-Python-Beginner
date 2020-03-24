<<<<<<< Updated upstream
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
# d - digit  - natural number
# f - float  - floating point number
#
# We have some few way to formating floating record:
# %f. ; {:f} ; round(x,y) - when x is argument and y is number of digits after the decimal point
# for example (for x=2/3):
x=4.0/3.0
print(x)
print("x is: %f." % (x))
print("x is {:f}" .format(x) )
print("x is", round(x,6))

# The first two options to formating records are formating strings - with this options you can formating every number or strings. It is something like translate digit format to string format.
# The last option to formating records is reseve to work only with numbers.
#
# When we don't using the formating records for numbers like "float" then in original Python take this numbers and formating this in "double".
# Double have 15 numbersof digits after the decimal point. Float have 6.
#
# String Formating 
#
#
# As you can see, modifier .2f is take round to the two digits after dot. If we want take one digit then we use .1f modifier.
#
# Old example
print("The world record for 100m was bitten %s and amounted to less %.1f seconds - wow!" %('16 August 2009', 9.58))
# New example
print("The world record for 100m was bitten {} and amounted to less {} seconds - wow!" .format('16 August 2009', 9.58))
#
#
# Table
#
# Using specific recording lengths we can create a table with specific width.
# For Old example from Flynerd website:
width = 42
print("-" * width)
print("|  Time  |      Runner      |    Data    |")
print("*" * width)
print("| %6.3f | %16s | %10s |" % (9.58, "Usain Bolt", "16.08.2009"))
print("| %6.3f | %16s | %10s |" % (9.69, "Tyson Gay", "20.09.2009"))
print("| %6.3f | %16s | %10s |" % (9.69, "Yohan Blake", "23.09.2012"))
print("| %6.3f | %16s | %10s |" % (9.74, "Asafa Powell", "2.09.2008"))
print("-" * width)
#
# This record say:
# %6.3f - 6 signs for records float number including 3 digit for after dot.
# %16s - 16 signs for strings
# %10s - 10 signs for strings
#
# width - total tabel width
#
# New example from Flynerd website:
width = 42
print("-" * width)
print("|  Time  |      Runner      |    Data    |")
print("*" * width)
print("| {:6.3f} | {:16s} | {:10s} |" .format(9.58, "Usain Bolt", "16.08.2009"))
print("| {:6.3f} | {:16s} | {:10s} |" .format(9.69, "Tyson Gay", "20.09.2009"))
print("| {:6.3f} | {:16s} | {:10s} |" .format(9.69, "Yohan Blake", "23.09.2012"))
print("| {:6.3f} | {:16s} | {:10s} |" .format(9.74, "Asafa Powell", "2.09.2008"))
print("-" * width)
#
# Differece between these two version is the location of record in the given space. In old version, the record is on the right side and in the new one on the left.
#
print("%06.3f" %(9.58))
print("{:06.3f}".format(9.58))
#
#
# Raw - Old version
#
# %r is raw record. It means than in this one record we can input anything we want - digits, strings, floats.
# For example in correct records.
currency = "dolar"
us = 1
pln = 4.08244915
print("Actualy %d %s cost %.2f PLN" %(us, currency, pln))
#
# Using %r is:
print("Actualy %r %r cost %r PLN" %(us, currency, pln))
#
#
# Change the place in sentence
#
# This option is doesn't exist in old version.
# We can using the number inside formating to choose record.
print("{} have {}".format("Alice","cat"))
print("{1} have {0}".format("Alice","cat"))
#
# Elements are numbering from "0", that's why Alice is on position "0" and cat on "1".
=======
# -*- coding: utf-8 -*-

#Formating Subtitles

# We have two standard type to formating subtitles:
# The first is the old formatting used by python 2.0+
# The secound and last is new formatting used by python 3.0+
#
# In the old formatting we use sign "%" inside sentence in place where we want put the argument and outside of sentence where we need to define the argument.
# We cannot use "%" alone, we need use it with correctly type like "%s", "%f" etc.
#
# In the new formatting we use "{}" instead %. We can put "{}" alone or with type inside like "{:f}, {:s} etc.
#
# Type of subtitles:
# s - string - inscription
# d - digit  - natural number
# f - float  - floating point number
#
# We have some few way to formating floating record:
# %f. ; {:f} ; round(x,y) - when x is argument and y is number of digits after the decimal point
# for example (for x=2/3):
x=4.0/3.0
print(x)
print("x is: %f." % (x))
print("x is {:f}" .format(x) )
print("x is", round(x,6))

# The first two options to formating records are formating strings - with this options you can formating every number or strings. It is something like translate digit format to string format.
# The last option to formating records is reseve to work only with numbers.
#
# When we don't using the formating records for numbers like "float" then in original Python take this numbers and formating this in "double".
# Double have 15 numbersof digits after the decimal point. Float have 6.
#
# String Formatting 
#
# Formatting Strings/ subtitles/ sequence sign is mean put content to inside subtitle which we are presenting like list of argument.
# There Are two ways to write commend: Old (Python 2.0) and New (Python 3.0). Python 2.0 was the old version of programming language and it was obsolete but often used by old company. In oposite, new companies use new version of python.
# In this topic I shows difference between old and new version but the important things is lerning corectly version 3.0 or above.
#
# Old string example
print("1 in english: %s \n2 in english: %s" %('one','two'))
# New string example
print("1 in english: {} \n2 in english: {}" .format('one','two'))
#
# Number
#
# Old digit number example
print("Digit %d precedes %d" %(7,8))
# New digit number example
print("Digit {} precedes {}" .format(7,8))
#
#Old float number example
print("The world record for 100 meters was %f and %s set it" %(9.58,'Usain Bolt'))
#New float number example
print("The world record for 100 meters was {} and {} set it" .format(9.58,'Usain Bolt'))
#
#If the float number has a many digit after dot then we need using a number limiting modyfier.
#
#Old float number with limiting modifier example
print("The world record for 100 meters was %.2f and %s set it" %(9.5877,'Usain Bolt'))
#New float number with limiting modifier example
print("The world record for 100 meters was {:.2f} and {} set it" .format(9.5877,'Usain Bolt'))
>>>>>>> Stashed changes
