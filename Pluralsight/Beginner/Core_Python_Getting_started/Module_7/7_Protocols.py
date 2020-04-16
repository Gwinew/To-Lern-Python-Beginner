# Protocols:
#
# - A set of operations that a type must support to implement the protocol.
# - Do not need to be defined as interfaces or base classes.
# - Types only need to provide functioning implementations.

# Protocol          # Implementing collections

# Container         # str, list, dict, range, tuple, set, bytes
# Sized             # str, list, dict, range, tuple, set, bytes
# Iterable          # str, list, dict, range, tuple, set, bytes
# Sequence          # str, list, range, tuples, bytes
# Mutable Sequence  # list
# Mutable Set       # set
# Mutable Mapping   # dict

# Protocol: Container
#
# item in container
# item not in container
#####################
# Protocol: Sized
#
# len(container)
#
#####################
# Protocol: Iterable
#
# Yield items one by one as they are requested
#
# for item in iterable:
#   print(item)
#
#####################
# Protocol: Sequence
#
# item = sequence[index]
# i = sequence.index(item)
# num=sequence.count(item)
# r = reserved(sequence)
#
# iterable, sized and contained
######################
# Protocol: Others
#
#
