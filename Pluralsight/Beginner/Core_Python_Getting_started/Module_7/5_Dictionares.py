# Dictionares:
#
# 
urls = {'Google': 'http://google.com',
        'Pluralsight':'http://pluralsight.com',
        'Sixty North' : 'http:/sixty-north.com'}
print(urls['Pluralsight'])

names_and_ages = [ ('Alice', 32), ('Bob', 48), ('Charlie', 28), ('Daniel', 33)]
print(names_and_ages,type(names_and_ages))
d = dict(names_and_ages)
print(d, type(d))
phonetic = dict(a='alpha', b='bravo',c='charlie', d='delta', e='echo', f='foxtrot')
print(phonetic, type(phonetic))
##############
# Create a independ dictionary:
# Copy way

d=dict(goldenrod=0xDAA520, indigo=0x4B0082, seashell=0xFFF5EE)
e=d.copy()
print(e)
f=dict(e)
print(f)

g=dict(wheat=0xF5DEB3, khaki=0xF0E68C, crimson=0xDC143C)
f.update(g)
print(f)                # Add g-dictionary to the end of f-dictionary, if you use a existing key than you update a value of this key without create a new key.

for key in f:
    print(f'{key} => {f[key]}')

for value in f.values():
    print(value)
    
for key in f.keys():
    print(key)

#######################

for key, value in f.items():
    print(f'{key} => {value}')

#######################
    # DELETE

del f['wheat']
print(f)

#######################
# Add
r=dict(goldenrod=[1,2,3])
f.update(r)
f['goldenrod']+=[4,5,6]
print(f)

from pprint import pprint as pp
pp(f)
