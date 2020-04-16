# Process file: EAFP

p = '/path/to/datafile.dat'

try:
    process_file(p)
except OSError as e:
    print(f'Error: {e}')
