# files.py
import sys

f=open(sys.argv[1], mode='rt', encoding='utf-8')
for line in f:
#    print(line)                # We don't use this because create a new empty line
    sys.stdout.write(line)
f.close()
