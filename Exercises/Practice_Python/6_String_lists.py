"""Ask the user for a string and print out whether this string is a palindrome
    or not.
    (A palindrome is a string that reads the same forwards and backwards.)
"""
name = input('Write a word:\n')
name_l=name
name_s=name
name=name.lower()
name_list = list(name)
name_list.insert(0,' ')
name_r_list=name_list[:0:-1]
name_r = ''.join(name_r_list)
if name == name_r:
    print('This is Palidrome')
else:
    print('This is not a Palidrome')
#

name_l = name_l.lower()
name_list_l = list(name_l)
name_list_l.reverse()
name_r_l = ''.join(name_list_l)


if name_l == name_r_l:
    print('This is Palidrome')
else:
    print('This is not a Palidrome')

##
name_s = name_s.lower()
name_rs = name_s[::-1]

if name_rs == name_s:
    print('This is Palidrome')
else:
    print('This is not a Palidrome')

from timeit import timeit

code_1 ="""
name = 'Maram'
name = name.lower()
name_list = list(name)
name_list.insert(0,' ')
name_r_list=name_list[:0:-1]
name_r = ''.join(name_r_list)
if name_r == name:
    True
else:
    False
"""

code_2 ="""
name = 'Maram'
name = name.lower()
name_list_l = list(name)
name_list_l.reverse()
name_r_l = ''.join(name_list_l)
if name_r_l == name:
    True
else:
    False
"""

code_3 ="""
name = 'Maram'
name=name.lower()
name_rs = name[::-1]

if name_rs == name:
    True
else:
    False
"""

print('code 1: ', timeit(code_1))
print('code 2: ', timeit(code_2))
print('code 3: ', timeit(code_3))

