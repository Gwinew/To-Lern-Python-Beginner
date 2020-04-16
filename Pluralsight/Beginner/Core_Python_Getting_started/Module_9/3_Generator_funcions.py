# Generator functions
#
# - Iterables defined by functions
# - Lazy evaluation
# - Can model sequences with no definite end
# - Composable into pipelines
#
###################
# yield:
#
# Generator functions must include at least one yield statement.
#
# They may also include return statements.
###################
#
#
def gen123():
    yield 1
    yield 2
    yield 3

g = gen123()
print(g)            # <generator object gen123 at ....>
print(next(g))
print(next(g))
print(next(g))
# print(next(g))    # StopIteration
for v in gen123():
    print(v)

h = gen123()
i = gen123()

print(h)
print(i)
print(h is i)       # False

next(h)             # 1
next(h)             # 2
next(i)             # 1

def gen246():
    print('About to yield 2')
    yield 2
    print('About to yield 4')
    yield 4
    print('About to yield 6')
    yield 6
    print('About to return')

g=gen246()
print(next(g))          # 2
print(next(g))          # 4
print(next(g))          # 6
# print(next(g))        # StopIteration
#
#######################################
#
# Maintaining State in Generators:
#
# 
