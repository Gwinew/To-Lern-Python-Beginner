# Names
#
# Make collection with names men and women. Ask user to write his name.
# Check if name is men or women and show this information.
# If name isn't on the list what show communication "We don't have this name" and user need to write about this name, this is men or women. Add name to list.
#
M="Men"
W="Women"
print(type(W))
names={"Agnieszka":W, "Maksymilian":M}
name=input("Write your name\n")
if name in names.keys():
    print("You are {}".format(names[name]))
else:
    print("Your name it isn't in collectin")
    MW=input("Write your sex: M/W\n")
    if MW == 'M' or MW == 'm':
        sex=M
    if MW == 'W' or MW == 'w':
        sex=W

    names[name]=sex
print(names)
