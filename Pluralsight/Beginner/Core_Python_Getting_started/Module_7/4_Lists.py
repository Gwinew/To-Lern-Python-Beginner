# Lists:

# Negative indices:
# - Index from the end of sequences using negative numbers.
# - The last element is at index -1
r=[1,-4,10,-16,15]
print(r[len(r)-1])      # result is 15 because len(r)=5 but r[5-1]=r[4]=15

print(r[-0])

#
# Slicing:
#
# - Extended form of indexing for referring to a portion of a list or other sequence.
# Syntax: a_list[start:stop]

print(r[1:3])
print(r[1:-1])
print(r[2:])

t=r
print(t is r)
s = r[:]
print(s is r)
print(r==s)

u = r.copy()
print(u is r)

v = list(r)

#

a = [[1,2],[3,4]]
b=a[:]
print(a is b)
print(a == b)
print(a[0],b[0])
print(a[0] is b[0])
a[0]=[8,9]
print(a[0],b[0])
a[1].append(5)
print(a[1],b[1])
print(a,b)      # Because a[0] is change all value but in a[1] is using .append() function - it is not replace a value, it is add value.

###########

c=[21,37]
d=c*4
print(d)
s = [[-1,+1]]*5
print(s)
s[2].append(7)
print(s)

#############
# list.index()
#
# - Find the location of an object in a list.
# - Returns the index of the firs list elemtn which is equal to the argument.
# Flynerd*
w = "The quick brown fox jumps over the lazy dog".split()
print(w)
i=w.index('fox')
print(i)
print(w[i])


############
# del
#
# - Remove an element from a list by index.
# - Syntax: del a_list[index]

u='jackdaws love my big sphinx of quartz'.split()
print(u)
del u[3]
print(u)
u.remove('jackdaws')
print(u)
del u[u.index('quartz')]
# u.remove('pyramid') # error
#

############
# list.insert()
# - Insert an item into a list
# - Accepts an item and the index of the new item
#

a = 'I accidentally the whole universe'.split()
print(a)
a.insert(2,"destroyed")
print(a)
print(' '.join(a))

##########
m=[2,1,3]
n=[4,7,11]
k=m+n
print(k)
k+=[18,29,47]
k.extend([76,129,199])
print(k)


############
# list.reverse() and list.sort()

g=[1,11,21]
g.reverse()
print(g)

d=[17,41,29]
d.sort()
print(d)

d.sort(reverse=True)
print(d)

# Key Parameter to list.sort():
# - Can be any callable object that accepts a single parameter.
# - Items passed to callable and sorted on its return value.

h= 'Not perplexing do handwriting family where I illegibly know doctors'.split()
print(h)
h.sort(key=len)
print(h)
print(' '.join(h))
#
#
# Reversing and sorting into copies.
# reserved() and sorted() are out-of-place equivalent to list.reverse() and list.sort()

x=[4,9,2,1]
y=sorted(x)
print (y,x)
p = [9,3,1,0]
q = reversed(p)     
print(q)            # <list_reverseiterator object at 0x0000000002FFA588>
print(list(q))
