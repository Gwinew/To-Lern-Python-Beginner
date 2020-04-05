# Numeric sort
#
# Three any numeric number write to three variable.
# Find the bigest number.
# Show number from the bigest to the lowest.
#
# This way is long way version.
number=input("Write three number and seperate ','-sign\n")
numlist=number.split(",")
x=int(numlist[0])
y=int(numlist[1])
z=int(numlist[2])

if x > y and x > z:
    maximum=x
elif y > x and y > z:
    maximum=y
else:
    maximum=z

print("The maximum number is {}".format(maximum))
#
if x < y:
    temp=x
    x=y
    y=temp
if x < z:
    temp=x
    x=z
    z=temp
if y < z:
    temp=y
    y=z
    z=temp
else:
    x=x
    y=y
    z=z
print(x,y,z)
