age=int(input("How old are You?"))
responsible=input("Do You be responsible? Y/N")

if age>100:
                  print("This is really your age?")
elif age >=18 and responsible =="Y":
                  print(" You are adult")
elif responsible !="Y":
                  print("Work on responsibility")
else:
                  print("You have a bit of legal age")
