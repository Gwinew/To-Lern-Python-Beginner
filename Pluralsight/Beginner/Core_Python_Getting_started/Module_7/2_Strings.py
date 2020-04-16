a=len("llalslewfnuvbvsjvbjsdsdvubayuvavebauyvg")
print(a)
s= 'New'
s+="found"
s+='land'
print(s)

##############
# str.join()
#
# - Concatention with + result in temporaries
# - str.join() insert a separator betweem a collection of strings.
# - Call join() on the separator string

colors = ';'.join(['#45ff23','#2321fa','#1298a3'])
print(colors)
print(colors.split(';'))
alll=''.join(['high','way','man'])
#
#
d='unforgetable'.partition('forget')
print(d)

departure, separator, arrival = "London:Edinburgh".partition(":")
print(departure, arrival)

origin, _, destination = "seatle-Boston".partition('-')
#
#################
# String formatting:
#
print('Current position {latitude} {longitude}'.format(latitude='60N', longitude='5E'))
print("Galactic position x={pos[0]}, y={pos[1]}, z={pos[2]}".format(pos=(65.2,23.1,82.2)))

import math
print("Math constans: pi={m.pi}, e={m.e}".format(m=math))
print("Math constans: pi={m.pi:.3f}, e={m.e:.3f}".format(m=math))

# PEP 498: Literal String Interpolation
# - Commonly called f-strings

f"one plus one is {1+1}"

value = 4*20
print(f'The value is {value}')

import datetime
print(f'The current time is {datetime.datetime.now().isoformat()}.')

print(f"Math constans: pi={math.pi:.3f}, e={math.e:.3f}")

