# Create a table of multiple.
width=17
print("-"*width)
for i in range(1,11):
    for j in range(1,11):
        print("| {:2} x {:2} = {:3} |".format(i,j,i*j))
    print("-"*width)
