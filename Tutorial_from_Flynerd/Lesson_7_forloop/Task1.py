# Write progrom for next 10 value natural number and show sum prevoius value:
# Expected value: 1,3,6,10,15,21,28,36,45,55
for i in range(1,11):
    if i==1:
        x=i
        temp=x
        print(x)
    else:
        x=temp+i
        temp=x
        print(x)
#
temp=0
for i in range(1,11):
    x=temp+i
    temp=x
    print(x)
