"""This weel's exercise is going to be revisiting an old exercise (exercise 5),
except require the solution in a different way.

Take two lists, say for example these two:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that return a list that contains only the elements
tat are common between the lists (without duplicates).
Make sure your program works on two lists of different sizes.
Write this in one line of Python using at least one list comprehension.

    Extras:
        - Radomly generate two lists to test this."""

# 1 - base exercise
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = []
[c.append(x) for x in a if x not in c] + [c.append(y) for y in b if y not in c]
c.sort()
print(c)


# 2 - another way - set
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

d = list(set(a).union(set(b)))
d.sort()
print(d)

# Extras

from random import randrange

e_num = randrange(1,20)
f_num = randrange(1,20)
while e_num == f_num:
    f_num = randrange(1,20)

e = []
f = []
for i in range(e_num):
    e.append(randrange(100))
for j in range(f_num):
    f.append(randrange(100))
e.sort()
f.sort()

# checked first solution:

g = []
[g.append(x) for x in e if x not in g] + [g.append(y) for y in f if y not in g]
g.sort()
print(g)

# checked second solution:

h = list(set(e).union(set(f)))
h.sort()
print(h)
import sys
print(sys.version)
