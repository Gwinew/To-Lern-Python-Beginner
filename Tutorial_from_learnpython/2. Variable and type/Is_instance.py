# isisntance function (information from PYnative):
#
# This function is used to check whether the object or varaible is an instance of the specified class type ord data type.
#
# isinstance( object, type)
#
# Using Python isinstance(), you can do the followings:
# - Check the type of a Python variable if a given type
# - Verify whether a variable is a number or string
# - Check if an object is an instance of a specified class
# - Check whether variable or object is of dict type, list type, set type, tuple type
#
#
# The ininstance() syntax and parameter:
#
# inisntance(object, classinfo)
#
# The ininstance() function checks if the object argument is an instance or subclass of classinfo class argument.
#
# instance Parameters:
# - The isinstance() takes two arguments, and both are mandatory.
# - object: The object/instance or variable to check. The object can be any class object or any variable name.
# - classinfo: Class info is type name, class name or tuple of types and classes. For example, in, str, list, dict, or any user-created class.
#
# Return Value from isinstance():
#
# If an object or variable is of a specified type, then isinstance() return true otherwise false.
#
#
# Python isinstance with multiple types:
#
# We can also check the instance with multiple types. when we use many types then we check use "OR" operator.
firstnum=80
secondnum=55.7
result = isinstance(firstnum,(int,float))
print(firstnum,'is an instance of int or float?',result)
result= isinstance(secondnum,(int,float))
print(secondnum,'is an instance of int or float?',result)
#
# isinstance() with Python Class
#
# A isinstance() function test object is of a specified class type. isisntance() is working as a comparison operator because it compares the object with the specified class type.
#
# The isinstance result will be true if the object is an instance of the given class type:
#
class Employee:
    def __init__(self, name, salary):
        self.name=name
        self.salary=salary
class Person:
    def __init__(self,name,sex):
        self.name=name
        self.sex=sex
emp=Employee("Emma",10000)
per=Person("Brent","male")
print("Checking emp object is an instance of Employee")
if isinstance(emp,Employee):
    print("Yes! given object is an instance of class Employee\n")
else:
    print("No! given object is not an instance of class Employee")

print("Checking per object is an instance of Employee")
if isinstance(per,Employee):
    print("Yes! given object is an instance of class Employee\n")
else:
    print("No! given object is not an instance of class Employee")
