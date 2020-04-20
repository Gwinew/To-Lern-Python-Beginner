"""Take a list, say for example this one:
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

    and write a program that prints out
    all the elements of the list that are less than 5.

    Extras:
        1. Instead of printing the elements one by one, make a new list that has
            all elements less than 5 from this list in it and print out this new list.
        2. Write this in one line of Python.
        3. Ask the user for a number and return a list that constains only elements
            from the original list a that are smaller than that number given by the user.

    """
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
i=0
while a[i] < 5:
    print(a[i])
    i+=1

for i in a:
    if a[i] >= 5:
        break
    print(i)
# Extras:

get = []
for i in a:
    if a[i] > 5:
        break
    get.append(a[i])
print(get)


b = [i for i in a if i < 5]
print(b)

c = int(input('Write a number:\n'))

d = [ i for i in a if i < c]
print(d)
