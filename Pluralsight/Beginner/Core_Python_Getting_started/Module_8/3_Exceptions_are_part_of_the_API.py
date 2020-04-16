# Use Standard Exception Types:
#
# Standard Types - Python provides standard exceptions types for signalling common errors
# Invalid argument values - Use ValueError for arguments of the right type but with an invalid value
# Exception constructors - Use raise ValueError() to raise a new ValueError
##############################
#
#  Exceptions and Protocols:
#
# - Sequences should raise IndexError for out=of-bounds indexing.
# - Exceptions must be implemented and documented correctly.
# - Existing built-in exceptions are often the right ones to use.

# Follow existing patterns:
#
# The more your code follows established patterns, the easier it will be for others to use.
# Lookup Failure in Mappings
def lookup(key):
    if not find_key(key):
        raise KeyError()
    return value(key)

# Common Exception Types:
#
# IndexError:
#
# An Integer index is out of range

z= [1,4,2]      # if we call z[4] we have: IndexError: list index out of range

# ValueError:
#
# An obcject is of the correct type but has an inappropriate value.

# int('jim')   # ValueError: invalid literal for int() with base 10: 'jim'
#

# KeyError
#
# A lookup in a mapping failed.

codes = dict(gb=44, us=1, no=47, fr=33, es=34)
# codes['de']           # KeyError: 'de'
