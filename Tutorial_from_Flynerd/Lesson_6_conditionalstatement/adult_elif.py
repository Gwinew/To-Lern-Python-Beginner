age = int(input('How old are You?'))

if(age>100):
    print("This is realy your age?")
elif(age>=18):
    print("You are adult")
else:
    print("You have a bit of legal age\nExactly you have {} years to be adult".format(18-age))
