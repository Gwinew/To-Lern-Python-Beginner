# Set:
#
# - Unordered collection of unique elements.
# - Sets are mutable
# - Elements in a set must be immutable

p = {6, 28, 496, 8128, 33550336}
print(p, type(p))
d = {}
print(type(d))

e =set()
print(e)

s=set([2, 4, 16, 64, 4096, 65536, 262144])
print(s)

t=[1,4,2,1,7,9,9]
set(t)
print(set(t))

for x in {1,2,4,8,16,32}:
    print(x)
q = {2, 9,6,4}
print(3 in q)       # False

k= {81,108}
k.add(54)
print(k)
k.add(12)
print(k)
k.add(108)
k.update([37, 128, 97])
print(k)

k.remove(97)
# k.remove(98)          # Error
k.discard(98)

print(k)


j = k.copy()
print(j)

m=set(j)
print(m)

########
# Algebra:

blue_eyes = {'Olivia','Harry','Lily','Jack','Amelia'}
blond_hair = {'Harry','Jack','Amelia', 'Mia', 'Joshua'}
smell_hcn = {'Harry','Amelia'}
taste_ptc = {'Harry', 'Lily', 'Amelia', 'Lola'}
o_blood = {'Mia','Joshua','Lily','Olivia'}
b_blood = {'Amelia', 'Jack'}
a_blood = {'Harry'}
ab_blood = {'Joshua','Lola'}
union_ex1 = blue_eyes.union(blond_hair)
print(union_ex1)
print(blue_eyes.union(blond_hair) == blond_hair.union(blue_eyes))
intersec_ex1 = blue_eyes.intersection(blond_hair)
print(intersec_ex1)
print(blue_eyes.intersection(blond_hair) == blond_hair.intersection(blue_eyes))

diff_ex1 = blond_hair.difference(blue_eyes)
print(diff_ex1)
diff_ex2 = blue_eyes.difference(blond_hair)
print(diff_ex2)
print(blue_eyes.difference(blond_hair) == blond_hair.difference(blue_eyes))

sym_diff_ex1 = blond_hair.symmetric_difference(blue_eyes)
sym_diff_ex2 = blue_eyes.symmetric_difference(blond_hair)
print(sym_diff_ex1)
print(sym_diff_ex2)
print(sym_diff_ex1 == sym_diff_ex2)


issub_ex1 = smell_hcn.issubset(blond_hair)
print(issub_ex1)            # True smell_hcn is in blond_hair

issupersub_ex1 = taste_ptc.issiperset(smell_hcn)
print(issupersub_ex1)       # True because smell_hcn is in taste_ptc

isdisjoi_ex1 = a_blood.isdisjoint(o_blood)
print(isdisjoi_ex1)         # True because there are different values in both groups
