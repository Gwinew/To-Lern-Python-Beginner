"""
Implement a function that takes as input three variables,
and returns the largest of the three. Do this without using the Python max() function!

The goal of this exercise is to think about some internals that Python normally
takes care of for us. All you need is some variables and if statements!
"""

a = 12
b = 24
c = 1
def max_of_three(a,b,c):
    max = 0
    if a>b and a>c:
        max = a
    if b>a and b>c:
        max = b
    else:
        max = c
    return max
print(max_of_three(a,b,c))
