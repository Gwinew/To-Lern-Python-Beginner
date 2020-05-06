"""
Write a program (using functions!) that asks the user for
a long string containing multiple words.
Print back to the user the same string, except with
the words in backwards order. For example, say I type the string:

- My name is Michele

Then I would see the string:

 - Michele is name My

 shown back to me.
"""

def reverse(string):
    liststring = string.split()
    liststring.reverse()
    string_reverse = ' '.join(liststring)
    return string_reverse

def reverse_s(strings):
    listofstring = strings.split()
    listofstring = listofstring[::-1]
    string_rev = ' '.join(listofstring)
    return string_rev

def reverse_d(stringsd):
    return ' '.join(stringsd.split()[::-1])

def reverse_v3(x):
  y = x.split()
  return " ".join(reversed(y))

x = str(input('Write a text\n'))
print(reverse(x))
print(reverse_s(x))
print(reverse_d(x))
print(reverse_v3(x))

from timeit import timeit

code_1 = """
x = 'Text is a long string uppon the world this'
def reverse(string):
    liststring = string.split()
    liststring.reverse()
    string_reverse = ' '.join(liststring)
    return string_reverse
reverse(x)
"""
code_2 = """
x = 'Text is a long string uppon the world this'
def reverse_s(strings):
    listofstring = strings.split()
    listofstring = listofstring[::-1]
    string_rev = ' '.join(listofstring)
    return string_rev
reverse_s(x)
"""

code_3 = """
x = 'Text is a long string uppon the world this'
def reverse_d(stringsd):
    return ' '.join(stringsd.split()[::-1])
reverse_d(x)
"""

code_4 = """
a = 'Text is a long string uppon the world this'
def reverse_v3(x):
  y = x.split()
  return " ".join(reversed(y))
reverse_v3(a)
"""

print('code_1', timeit(code_1))
print('code_2', timeit(code_2))
print('code_3', timeit(code_3))
print('code_4', timeit(code_4))
