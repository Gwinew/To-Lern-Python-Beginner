# Write a program using a while loop with 10 next natural number and show sum precious value.
# Expect result: 1,3,6,10,15,21,28,36,45,55.
x=0
while x<10:
    x += 1
    if x == 1:
        temp=x
        print(x)
    else:
        y = temp + x
        temp = y
        print(y)
