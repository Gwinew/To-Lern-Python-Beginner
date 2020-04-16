# Process file: LBYL

import os

p = '/path/to/datafile.dat'

if os.path.exists(p):
    process_file(p)
else:
    print(f'No such file as {p}')
