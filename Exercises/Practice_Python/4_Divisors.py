"""Create a program that asks the user for a number
    and then prints out a list of all the divisors of that number.
    (If you don't know that a divisor is, it's a number that divides
    evenly into another number.
    For example, 13 is a divisor of 26 bacuse 26/13 has no remainder.)
"""

num = int(input('Write a number to find a divisors:\n'))

ran = range(1,num+1)

divisor =[]

for i in ran:
    if num % i == 0:
        divisor.append(i)

print(divisor)


# The smallest diviosor

divisor=[]

from math import sqrt
def prime(x):
    if x <2 :
        return False
    for i in range(2,int(sqrt(x))+1):
        if x % i==0:
            return False
    return True



prime_numbers =[i for i in range(int(sqrt(num))+1) if prime(i)]

for a in prime_numbers:
    if num % a == 0:
        divisor.append(a)
        

print(divisor)
