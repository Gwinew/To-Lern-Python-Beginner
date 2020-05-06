"""
Write a program (function!) that takes a list and return a new list
that contains all the elements of the first list minus all the duplicates.

    Extras:
        - Write two different function to do this:
            one using a loop and constructing a list,
            and another using sets.
        - Go back and do Exercise 5 using sets, and write the solution
            for that in a different function.
"""
a = [1, 1, 2, 2, 3, 4, 5, 6, 6, 7, 8, 4, 9]


def remove_duplicates(listtrd):
    newlist = []
    [newlist.append(i) for i in listtrd if i not in newlist]
    return newlist


def conventional_removal_duplicates(listtr):
    newlist_trd = []
    for i in listtr:
        if i not in newlist_trd:
            newlist_trd.append(i)
    return newlist_trd


def set_duplicates(settrd):
    settrd.sort()
    return list(set(settrd))


print(a)
print(remove_duplicates(a))
print(conventional_removal_duplicates(a))
print(set_duplicates(a))

from timeit import timeit

code_1="""
a = [1, 1, 2, 2, 3, 4, 5, 6, 6, 7, 8, 4, 9]
def remove_duplicates(listtrd):
    newlist = []
    [newlist.append(i) for i in listtrd if i not in newlist]
    return newlist
y = remove_duplicates(a)
"""

code_2="""
a = [1, 1, 2, 2, 3, 4, 5, 6, 6, 7, 8, 4, 9]
def conventional_removal_duplicates(listtr):
    newlist_trd = []
    for i in listtr:
        if i not in newlist_trd:
            newlist_trd.append(i)
    return newlist_trd
y = conventional_removal_duplicates(a)
"""

code_3="""
a = [1, 1, 2, 2, 3, 4, 5, 6, 6, 7, 8, 4, 9]
def set_duplicates(settrd):
    settrd.sort()
    return list(set(settrd))
y = set_duplicates(a)
"""

print('code_1', timeit(code_1))
print('code_2', timeit(code_2))
print('code_3', timeit(code_3))
