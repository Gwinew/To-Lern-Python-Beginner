# Generator Expressions:
#
# expr(item) for item in iterable
#

million_squares = (x*x for x in range(1,1000001))
print(million_squares)
print(list(million_squares)[-10:])
#
print(list(million_squares))            # []

#
sum(x*x for x in range(1, 1000001))

print(x for x in range(1001) if is_prime(x))
