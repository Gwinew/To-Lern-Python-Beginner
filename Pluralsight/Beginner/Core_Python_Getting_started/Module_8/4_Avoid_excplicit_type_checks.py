import sys

DIGIT_MAP = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine' : '9'
    }

def covert(s):
#    if not isinstance(s, list):             # Check argument type
#        raise TypeError(                    # Raise Type Error but we have operation on one type.
#            "argument must be a list")

    x = -1

    try:                                
        number=''
        for token in s:
            number +=DIGIT_MAP[token]
        return int(number)
    except (KeyError, TypeError) as e:              # Catch TypeError
        print(f'Conversion error: {e!r}',           # Re-raise it
              file=sys.stderr)

        raise                                       

from math import log

def string_log(s):
    v = convert(s)
    return log(v)

# Avoid Catching TypeError
#
# - Increase function reusability
# - Let TypeError arise on their own
