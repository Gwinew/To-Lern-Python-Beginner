# Write a script calculating factorial value. Ask user to a number.
#
num=int(input("Write a number to calculating factorial value\n"))
start=1
temp=1
while start <= num:
    end=temp*start
    temp=end
    start+=1
print("{}!={})".format(num,end))
