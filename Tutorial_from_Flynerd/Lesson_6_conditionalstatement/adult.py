print('How old are You?')
age = int(input())

if(age>=18):
    print("You are adult")
else:
    print("You have a bit of legal age|nExactly you have {} years to be adult".format(18-age))
