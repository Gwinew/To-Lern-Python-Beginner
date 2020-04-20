# File Managment:
#
# open():
#
# - Open a file for reading or writing
# - file: the path to the file (required)
# - mode: read, write, or append, plus binary or text
# - encoding: encodinf to use in text mode

# Binary Mode:
#
# 010101001 --decode-> read()
# 010100101 <-encode-- write()
#
# Default Encoding:
import sys
sys.getdefaultencoding()
print(sys.getdefaultencoding())         # 'utf-8'

# docs.python.org/3/library/codecs.html#standard-encodings
#
# Writing text:

f = open('wasteland.txt', mode='wt', encoding='utf-8')

# open () Modes:
#
# 'r'   -   open for reading
# 'w'   -   open for writing
# 'a'   -   open for appending
#
# selector / meaning
#
# 'b'   -   binary mode
# 't'   -   text mode

print(help(f))

f.write('What are the roots that clutch, ')

f.write('what branches grow\n')

f.write('Out fo this stony rubbish?')

f.close()
#############################
#
# Reading Text:
#
g = open('wasteland.txt', mode='rt', encoding='utf-8')
print(g.read(32))
print(g.read())
print(g.read())
print(g.seek(0))
# Seek cannot move to arbitary offset - Only 0 and values from tell() are allowed
print(repr(g.readline()))               # repr() take a raw result - it means show special signs as \n etc.
print(g.readline())
print(g.readline())
g.seek(0)
print(g.readlines())
g.close()
###############################
#
# Appending Text:
#
h = open('wasteland.txt', mode='at', encoding='utf-8')
h.writelines(
    ['Son of man, \n',
     'You cannot say, or guess, ',
     'for you know only,\n',
     'A heap of broken images, ',
     'where the sun beats\n'])
h.close()
