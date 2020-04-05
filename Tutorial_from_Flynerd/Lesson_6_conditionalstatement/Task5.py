# Pythagorean law
#
# 1. Ask user to write triangle length A, B, C and check it is possible to build triangle with this value.
# 2. Is it pythagorean triple?
# 3. Special cases is egyptian triple with length ratio 3:4:5. Check it pythagorean triple is egyptian triple.
# 4. Include this not necessery a input value start from "a".
data=input("Please, write triangle length seprate ','-sign\n")
data=data.split(',')
a=int(data[0])
b=int(data[1])
c=int(data[2])

if c<b:
    temp=c
    c=b
    b=temp
if c<a:
    temp=c
    c=a
    a=temp
if b<a:
    temp=b
    b=a
    a=temp
triple1=a+b
triple2=c
if triple1 < triple2:
    print("This isn't triangle")
else:
    print("This is triangle")
    pit1=a**2+b**2
    pit2=c**2
    if pit1==pit2:
        print("This is pythagorean triple")
        a_1=a/3
        b_1=b/4
        c_1=c/5
        if a_1==b_1==c_1:
            print("This is also egyptian triple")
