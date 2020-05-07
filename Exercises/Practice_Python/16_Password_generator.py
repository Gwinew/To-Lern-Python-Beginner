"""Write a password generator in Python.
Be creative with how you generate passwords -
- strong passwords have a mix of lowercase letters, uppercase letters,
numbers and symbols. The passwords should be random,
generating a new password every time the user asks for a new password.
Include your runtime code in a main method.

    Extra:
        - Ask the user how strong their password to be.
        For weak password, pick a word or two from a list.
"""
from random import randrange, sample, choice
import string

def easy_password():
    x = ['cat', 'mouse', 'time', 'death', 'metal']
    name = []
    for i in range(0,3):
        name.append(x[randrange(0,len(x),1)])
    name = ''.join(name)
    name = sample(name, len(name))
    for i in range(len(name)):
        y = randrange(100)
        if y >= 50:
            name[i] = name[i].upper()
    name = ''.join(name)
    return name

def medium_password():
    x = ['cat', 'mouse', 'time', 'death', 'metal']
    y = []
    name = []
    for i in range(randrange(2,5)):
        y.append(str(randrange(10,99)))
    for i in range(0,3):
        name.append(x[randrange(0,len(x),1)])
    name = ''.join(name)
    name = list(name)
    for i in range(len(name)):
        d = randrange(10,75)
        if d >= 50:
            name[i] = name[i].upper()
    for i in range(len(y)):
        name.append(y[i])
    name = ''.join(sample(name, len(name)))
    return name

def strong_password():
    num_one = randrange(1,100)
    num_two = randrange(1,100)
    num_three = randrange(1,50)
    num_four = randrange(1,50)
    a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','r','s','t','u','w','v','x','y','z']
    b = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','R','S','T','U','W','V','X','Y','Z']
    c = ['1','2','3','4','5','6','7','8','9','0']
    d = ['!','@','#','$','%','^','&']
    only = 50/(num_one+num_two+num_three+num_four)
    list_num_one = int(num_one*only)
    list_num_two = int(num_two*only)
    list_num_three = int(num_three*only)
    list_num_four = int(num_four*only)
    s_password = []
    for i in range(list_num_one):
        s_password.append(a[randrange(len(a))])
    for i in range(list_num_two):
        s_password.append(b[randrange(len(b))])
    for i in range(list_num_three):
        s_password.append(c[randrange(len(c))])
    for i in range(list_num_four):
        s_password.append(d[randrange(len(d))])
    s_password = ''.join(sample(s_password, len(s_password)))
    return s_password

print(easy_password())
print(medium_password())
print(strong_password())
num = int(input("Choose a password level:\n1. - Easy\n2. - Medium\n3. - Strong\n"))
if num == 1:
    print(easy_password())
if num == 2:
    print(medium_password())
if num == 3:
    print(strong_password())

# from Practice Python
s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
passlen = 8
p =  "".join(sample(s,passlen))
print (p)

# Another option

def pw_gen(size = 8, chars=string.ascii_letters + string.digits + string.punctuation):
	return ''.join(choice(chars) for _ in range(size))

print(pw_gen(int(input('How many characters in your password?'))))
