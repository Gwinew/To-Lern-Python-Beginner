from exceptional import convert
print(convert('one three three seven'.split()))

# print(convert('around two grillion'.split())) # Error KeyError: 'around'
# After add except KeyError.

print(convert('three four'.split()))

print(convert('eleven'.split()))

# print(convert(512))       # Error TypeError: 'int' object is not iterable
# After add TypeError

print(convert(512))
#
###########################
# Programer errors:
#
# - IndentationError
# - SyntaxError
# - NameError
#
# These should almost never be caught
#############################
# Accessing Exception Objects
#
# exceptional_ver_after3
