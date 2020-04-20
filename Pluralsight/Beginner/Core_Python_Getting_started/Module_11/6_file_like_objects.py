# File-like objects
#
# - Objects that behave like files
#
# - A semi-formal protocol
#
# - File behaviors are too varied for a fully-specified protocol.
#
# - Use an EAFP approach with file-like objects when necessary.

def words_per_line(flo):
    return[len(line.split()) for line in flo.readlines()]

with open('wasteland.txt', mode='rt', encoding='utf-8') as real_file:
    wpl = words_per_line(real_file)

print(wpl)
print(real_file)

from urllib.request import urlopen

with urlopen('http://sixty-north.com/c/t.txt') as web_file:
    wpl=words_per_line(web_file)

print(wpl)
print(type(web_file))


from fridge import raid
raid('bacon')
raid('deep fried pizza')
