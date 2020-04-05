# The Script ask user for a age. If user is before 18 then program show information "User is not adult" and return how many years left to be adult.
# Adult user show " User is adult". Check age isn't over 100 and show "happy 200 Years!".
age=int(input("How old are You?"))

if age >= 18:
    print("User is adult")
if age >100:
    print("Happy 200 years!")
else:
    print("User is not adult - You have {} years to be majority".format(age))
