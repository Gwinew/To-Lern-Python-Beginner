# id()
# Returns a unique integer identifier for an object that is constant for the life of the object.
#
a = 496
print(id(a))
b=1729
print(id(b))
b=a
print(id(b))
print(id(a) == id(b))
print(a is b)
print(a is None)
t=5
print(id(t))
t+=2            # 5 + 2 = 7
print(id(t))
