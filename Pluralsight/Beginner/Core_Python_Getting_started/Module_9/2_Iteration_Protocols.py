# Iteration Protocols:
#
# - iterable - Can be passed to iter() to produce an iterator
# - iterator - Can be passed to next() to get the next value in the sequence.
#
iterable = ['Spring', 'Summer', 'Autumn', 'Winter']
iterator = iter(iterable)
print(next(iterator))   # 'Spring'
print(next(iterator))   # 'Summer'
print(next(iterator))   # 'Autumn'
print(next(iterator))   # 'Winter'
# print(next(iterator))   # StopIteration

#############################

#############################
# Stopping iteration with an Exception
#
# A single end:
#   Sequences only have on ending, after all, so reaching it is exceptional
#
# Infinite sequences:
#   Finding the end of an infinite sequence would be truly exceptional
#
###############################
def first(iterable):
    iterator=iter(iterable)
    try:
        return next(iterator)
    except StopIteration:
        raise ValueError("iterable is empty")
print(first(['1st','2nd','3rd']))
print(first(['1st','2nd','3rd']))

print(first(set())) 
