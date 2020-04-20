"""Take two lists, say for example these two:
    a = [ 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [ 1, 2,3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    and write a program that returns a list that contains only
    the elements that are common between the lists (without duplicates).
    Make sure your program works on two list of fifferent sizes.

    Extras:
        1. Randomly generate two lists to test this.
        2. Write this in one line of Python (don't worry if you can't
            figure this out at this point - we'll get to it soon)

"""


a = [ 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = []

for i in a:
    if not i in c:
        c.append(i)
    for  j in b:
        if not j in c:
            c.append(j)
print(c)


# Extras
import random

a = []
b = []

x = random.randint(1,13)
y = random.randint(1,20)

while x == y:
    y = random.randint(1,20)


for i in range(0,x+1):
    n=random.randint(1,100)
    a.append(n)
for i in range(0,y+1):
    l=random.randint(1,100)
    b.append(l)

c = []

for i in a:
    if not i in c:
        c.append(i)
    for  j in b:
        if not j in c:
            c.append(j)
c.sort()
print(c)


#


d = list(set(a).symmetric_difference(set(b)))+list(set(a).intersection(set(b)))
d.sort()
print(d)

