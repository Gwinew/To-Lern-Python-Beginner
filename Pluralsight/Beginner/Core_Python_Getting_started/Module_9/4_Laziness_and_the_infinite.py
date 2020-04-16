# Laziness and the Infinite
#
# Generators only do enough work to produce requested data.
#
# This allows generators to model infinite (or just very large) sequences.
#
# Examples of such sequences are:
# - sensor reading
# - mathematical sequences
# - Content of large files
########################
#
def lucas():
    yield 2
    a = 2
    b = 1
    while True:
        yield b
        a, b = b, a+b
for x in lucas():
    print(x)

# Use CTRL+C to end of the loop = KeybordInterrupt
