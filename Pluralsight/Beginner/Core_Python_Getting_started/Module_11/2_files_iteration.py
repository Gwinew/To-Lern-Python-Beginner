# Files Iteration
#
# in cmd command we use
# python files.py wasteland.txt
#
#############################
#
# The Racaman Sequence:

import sys
from itertools import count, islice


def sequence():
    """Generate Recaman's sequence."""
    seen = set()
    a = 0
    for n in count(1):
        yield a
        seen.add(a)
        c = a - n
        if c < 0 or c in seen:
            c = a + n
        a = c

def write_sequence(filename, num):
    """Write Recaman's seqience to a text file."""
    f = open(filename, mode='wt', encoding='utf-8')
    f.writelines(f'{r}\n'
                 for r in islice(sequence(), num + 1))
    f.close()

if __name__=='__main__':
    write_sequence(filename=sys.argv[1],
                   num=int(sys.argv[2]))

##############################
#
# Sequence reader
"""Read and print an integer series."""
import sys

def read_series(filename):
    f = open(filename, mode='rt', encoding='utf-8')
    series = []
    for line in f:
        a = int(line.strip())
        series.append(a)
    f.close()
    return series

def main(filename):
    series = read_series(filename)
    print(series)
#
# in cmd:
# python series.py recaman.dat
# then we add:
# echo "oops" >> recaman.dat
# Then again:
# python series.py recaman.dat
# we have a ValueError: invalid literal for int() with base 10: 'oops'
# We repait that:
import sys

def read_series(filename):
    try:                                                    # Add try and finally
        f = open(filename, mode='rt', encoding='utf-8')
        return [int(line.strip()) for line in f]
    finally:        
        f.close()
    return series

def main(filename):
    series = read_series(filename)
    print(series)

########################################
