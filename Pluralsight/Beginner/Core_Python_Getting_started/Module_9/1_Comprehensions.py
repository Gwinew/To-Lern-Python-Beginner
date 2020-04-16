# Comprehensions
#
# Concise syntax for describing lists, sets, and dictionaries.
# Reable and expressive.
# Close to natural language.
#
######################
# List Comprehensions:
#
words = 'Why sometimes I have belived as many as six impossible things before breakfast'.split()
print(words)
print([len(word) for word in words])
#
# List Comprehension Syntax:
# [expr(item) for item in iterable]
#
# Equivalent Syntax:
#
lenghts = []
for word in words:
    lenghts.append(len(word))
print(lenghts)

from math import factorial
f=[len(str(factorial(x))) for x in range(20)]
print(f, type(f))

######################
# Set Comprehensions:
#
from math import factorial
s= {len(str(factorial(x))) for x in range(20)}
print(type(s))
print(s)

######################
# Dict Comprehensions:
#
# {
# key_expr(item):value_expr(item)
# for item in iterable
# }
country_to_capital = {'United Kingdom': 'London',
                      'Brazil': 'Brasilia',
                      'Morocco': 'Rabat',
                      'Sweden': 'Stockholm' }
capital_to_country = {capital: country for country, capital in country_to_capital.items()}
from pprint import pprint as pp
pp(capital_to_country)

#
#
words = ['hi', 'hello', 'foxtrot', 'hotel']
print({x[0]: x for x in words})             # 'h' is overwrite
#######################
# Complex Expression:
#
import os
import glob
file_sizes = {os.path.realpath(p): os.stat(p).st_size for p in glob.glob('*.py')}
pp(file_sizes)
########################
# Filtering Comprehensions:
#
from math import sqrt
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x))+1):      # Pierwiastek
        if x % i == 0:
            return False
    return True
print([x for x in range(101) if is_prime(x)])

prime_square_divisiors = {x*x: (1,x,x*x) for x in range(20) if is_prime(x)}
pp(prime_square_divisiors)
##########################
# 
#
########################
# 
