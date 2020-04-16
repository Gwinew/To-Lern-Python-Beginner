def square(x):
    return x * x
print(square(5))

def launch_missiles():
    print("Missiles launched!")
##########################

def nth_root(radicand, n):
    return radicand ** (1/n)

print(nth_root(16,2))



###########################
def even_or_odd(n):
    if n % 2 == 0:
        print("even")
        return
    print("odd")

w = even_or_odd(30)
d = even_or_odd(25)
print(w,d)


###########################

# For special functions we use __feature__ it is good practice
#
#
# dunder:
#
# Our way of pronouncing special names
# A protmanteau of 'double underscore'
#
# Insted of 'underscore underscore name underscore underscore' we'll say 'dunder name'


