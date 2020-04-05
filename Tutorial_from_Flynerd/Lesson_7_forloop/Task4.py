# Write a program which execute task from user n-times. With every start loop show a information:
# if number is a multiply of 3
# if number is a multiply of 4
# print "hurra" if number divide for 3 and 4
# Show "*" if any conditions aren't fulfilled.
n=int(input("Write a number of loops\n"))
n=n+1
for i in range(1,n):
    if i%3==0:
        if i%4==0:
            print("Hurra! {}".format(i))
        else:
            print("Number {} is a multiple of 3".format(i))
    elif i%4==0:
        print("Number {} is a multiple of 4".format(i))
    else:
        print("*")
