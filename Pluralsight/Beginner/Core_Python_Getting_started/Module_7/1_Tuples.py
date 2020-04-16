# Tuple:
# Immutable sequences of arbitrary objects.

t = ('Norway', 4.953, 3)
print(t[0])
print(len(t))
for item in t:
    print(item)

print(t + (338186.0,265e9))
print(t*3)
a=((220,284),(1184,1210),(2620,2924),(5020,5564),(6232,6368))
print(a[2][1])  # result 2924 - first [] is a first tuple and second [] is a inside tuple
h= (391)
print(h,type(h))
k=(391,)
print(k,type(k))

e=()
print(e,type(e))

p=1,1,1,4,6,19
print(p,type(p))
####

def minmax(items):
    return min(items), max(items)
print(minmax([83,33,84,32,85,31,86]))
#
# Tuple unpacking:

lower, upper = minmax([83,33,84,32,85,31,86])

print(lower)        # Because min(items) is defined as first
print(upper)        

(a,(b,(c,d)))=(4,(3,(2,1)))
print(a,b,c,d)
##################
a = "jelly"
b = "bean"
a,b=b,a
print(a)
print(b)
########

print(tuple([561,1105,1729,2465]))
print(tuple("charmichael"))
print(5 in (3,5,17,257,65537))
print(5 not in (3,5,17,257))
